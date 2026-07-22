"""
repro_guard — a no-overwrite safety layer for reproducing the atlas figures.

The analysis notebooks in this book were written to *generate* the shared data
(``*.h5ad``, ``*.tsv``, ``*.bed``, ``*.hdf``, ``*.cool`` …) as well as the figure
PDFs. When you re-execute a notebook to check reproducibility, you almost never
want it to silently clobber a file that already exists on disk — either a shared
input someone else depends on, or an output you produced in an earlier run.

``repro_guard`` monkey-patches the common write entry points so that:

    * If the destination path ALREADY EXISTS  -> the write is SKIPPED (cached),
      and a ``[repro_guard] skip existing: <path>`` message is printed.
    * If the destination path does NOT exist   -> the write proceeds normally,
      creating the file (and parent directories, for figure output dirs).

This exactly matches the intended workflow: existing files are never overwritten,
but genuinely missing outputs are still regenerated so you can verify a panel.

Usage (already added as the first cell of every notebook)::

    import repro_guard
    repro_guard.activate()          # guard on (default)

To intentionally allow overwriting during a fresh regeneration::

    repro_guard.activate(overwrite=True)     # or repro_guard.deactivate()

Functions patched: pandas ``to_csv/to_hdf/to_pickle/to_parquet/to_excel``
(DataFrame & Series), numpy ``save/savez/savez_compressed/savetxt``,
matplotlib ``Figure.savefig`` + ``pyplot.savefig``, anndata ``AnnData.write`` /
``write_h5ad``, ``joblib.dump``, ``cooler.create_cooler``, the builtin ``open``
(only for ``w``/``a``/``x`` modes), and ``os.system`` (only when the command
contains a ``> file`` / ``>> file`` shell redirect).
"""
import builtins
import functools
import os

_STATE = {"active": False, "overwrite": False, "patched": False}
_ORIG = {}


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def _is_pathlike(x):
    return isinstance(x, (str, bytes, os.PathLike))


def _exists(path, extra_suffixes=()):
    """True if ``path`` (or ``path`` + one of ``extra_suffixes``) already exists."""
    try:
        p = os.fspath(path)
    except TypeError:
        return False
    if os.path.exists(p):
        return True
    for suf in extra_suffixes:
        if not p.endswith(suf) and os.path.exists(p + suf):
            return True
    return False


def _ensure_parent(path):
    try:
        p = os.fspath(path)
    except TypeError:
        return
    d = os.path.dirname(p)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)


def _skip(path):
    print(f"[repro_guard] skip existing: {path}")


# --------------------------------------------------------------------------- #
# generic wrapper factories
# --------------------------------------------------------------------------- #
def _guard_method(orig, path_argno=0, path_kw=None, extra_suffixes=()):
    """Wrap a bound method/function whose output path is a positional/kw arg."""

    @functools.wraps(orig)
    def wrapper(*args, **kwargs):
        if not _STATE["active"] or _STATE["overwrite"]:
            return orig(*args, **kwargs)
        path = None
        if path_kw is not None and path_kw in kwargs:
            path = kwargs[path_kw]
        elif len(args) > path_argno:
            path = args[path_argno]
        if _is_pathlike(path):
            if _exists(path, extra_suffixes):
                _skip(path)
                return None
            _ensure_parent(path)
        return orig(*args, **kwargs)

    return wrapper


# --------------------------------------------------------------------------- #
# activation
# --------------------------------------------------------------------------- #
def _patch_all():
    if _STATE["patched"]:
        return

    # ---- pandas -----------------------------------------------------------
    try:
        import pandas as pd

        for cls in (pd.DataFrame, pd.Series):
            for name, extra in (
                ("to_csv", ()),
                ("to_hdf", ()),
                ("to_pickle", ()),
                ("to_parquet", ()),
                ("to_excel", ()),
                ("to_feather", ()),
            ):
                if hasattr(cls, name):
                    key = (cls.__name__, name)
                    _ORIG[key] = getattr(cls, name)
                    # first positional arg after self is the path
                    setattr(cls, name, _guard_method(_ORIG[key], path_argno=1, extra_suffixes=extra))
    except Exception as e:  # pragma: no cover
        print(f"[repro_guard] pandas not patched: {e}")

    # ---- numpy ------------------------------------------------------------
    try:
        import numpy as np

        _ORIG[("np", "save")] = np.save
        np.save = _guard_method(np.save, path_argno=0, extra_suffixes=(".npy",))
        _ORIG[("np", "savez")] = np.savez
        np.savez = _guard_method(np.savez, path_argno=0, extra_suffixes=(".npz",))
        _ORIG[("np", "savez_compressed")] = np.savez_compressed
        np.savez_compressed = _guard_method(np.savez_compressed, path_argno=0, extra_suffixes=(".npz",))
        _ORIG[("np", "savetxt")] = np.savetxt
        np.savetxt = _guard_method(np.savetxt, path_argno=0)
    except Exception as e:  # pragma: no cover
        print(f"[repro_guard] numpy not patched: {e}")

    # ---- matplotlib -------------------------------------------------------
    try:
        import matplotlib.figure as mfig
        import matplotlib.pyplot as plt

        _ORIG[("Figure", "savefig")] = mfig.Figure.savefig
        mfig.Figure.savefig = _guard_method(mfig.Figure.savefig, path_argno=1, path_kw="fname")
        _ORIG[("plt", "savefig")] = plt.savefig
        plt.savefig = _guard_method(plt.savefig, path_argno=0, path_kw="fname")
    except Exception as e:  # pragma: no cover
        print(f"[repro_guard] matplotlib not patched: {e}")

    # ---- anndata ----------------------------------------------------------
    try:
        import anndata

        for name in ("write", "write_h5ad"):
            if hasattr(anndata.AnnData, name):
                key = ("AnnData", name)
                _ORIG[key] = getattr(anndata.AnnData, name)
                setattr(anndata.AnnData, name, _guard_method(_ORIG[key], path_argno=1, path_kw="filename"))
    except Exception as e:  # pragma: no cover
        pass  # anndata optional

    # ---- joblib -----------------------------------------------------------
    try:
        import joblib

        _ORIG[("joblib", "dump")] = joblib.dump
        joblib.dump = _guard_method(joblib.dump, path_argno=1, path_kw="filename")
    except Exception:
        pass

    # ---- cooler -----------------------------------------------------------
    try:
        import cooler

        _ORIG[("cooler", "create_cooler")] = cooler.create_cooler
        cooler.create_cooler = _guard_method(cooler.create_cooler, path_argno=0, path_kw="cool_uri")
    except Exception:
        pass

    # ---- builtin open (write modes only) ----------------------------------
    _ORIG[("builtins", "open")] = builtins.open
    _orig_open = _ORIG[("builtins", "open")]

    @functools.wraps(_orig_open)
    def _guarded_open(file, mode="r", *args, **kwargs):
        if _STATE["active"] and not _STATE["overwrite"] and _is_pathlike(file):
            m = mode if isinstance(mode, str) else "r"
            if any(c in m for c in ("w", "a", "x")) and _exists(file):
                _skip(file)
                # return a harmless no-op file handle to /dev/null so callers
                # that .write() to it don't crash.
                return _orig_open(os.devnull, "w")
            if any(c in m for c in ("w", "a", "x")):
                _ensure_parent(file)
        return _orig_open(file, mode, *args, **kwargs)

    builtins.open = _guarded_open

    # ---- os.system (shell redirect only) ----------------------------------
    _ORIG[("os", "system")] = os.system
    _orig_system = _ORIG[("os", "system")]

    @functools.wraps(_orig_system)
    def _guarded_system(command):
        if _STATE["active"] and not _STATE["overwrite"] and isinstance(command, str):
            # crude parse of a trailing '> file' / '>> file' redirect
            import re

            m = re.search(r">>?\s*([^\s|;&><]+)", command)
            if m and _exists(m.group(1).strip("'\"")):
                _skip(m.group(1))
                return 0
        return _orig_system(command)

    os.system = _guarded_system

    _STATE["patched"] = True


def activate(overwrite=False):
    """Turn the guard on. ``overwrite=True`` lets writes proceed (danger)."""
    _patch_all()
    _STATE["active"] = True
    _STATE["overwrite"] = bool(overwrite)
    mode = "OVERWRITE ALLOWED" if overwrite else "no-overwrite (existing files are cached/skipped)"
    print(f"[repro_guard] active — {mode}")


def deactivate():
    """Turn the guard off (writes behave as the un-patched originals)."""
    _STATE["active"] = False
    print("[repro_guard] inactive — writes are NOT guarded")


# importing the module activates the guard by default
activate(overwrite=False)
