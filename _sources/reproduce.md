# Reproduction guide

This page explains the two conventions every notebook in this book follows so you can
re-run them safely.

## 1. One editable path at the top of every notebook

The original analysis used absolute paths like
`/large_storage/zhoulab/zhoujt/project/ENTEx/…`. Each notebook now begins with a
single **setup cell** that centralizes those into two variables and changes into the
original working directory, so every downstream relative path resolves unchanged:

```python
# === Reproduction setup (edit these two paths for your machine) ===
import os, sys

# This repository (so `import repro_guard` works):
BOOK_ROOT  = os.environ.get("BOOK_ROOT",  os.path.dirname(os.getcwd()))
# The ENTEx data/project root that holds allc/, clustering/, DMR/, analysis/, ...:
ENTEX_ROOT = os.environ.get("ENTEX_ROOT", "/large_storage/zhoulab/zhoujt/project/ENTEx")

sys.path.insert(0, BOOK_ROOT)
os.chdir(f"{ENTEX_ROOT}/analysis")   # original working directory of the analysis
import repro_guard                    # no-overwrite guard (see §2)
indir = f"{ENTEX_ROOT}/"             # notebooks refer to data as f"{indir}..."
```

To run on your own machine you edit (or `export`) just **`ENTEX_ROOT`** — nothing else
in the notebook body needs to change. All the `f"{indir}clustering/..."`,
`clustering_summary/*.pdf`, etc. paths then resolve from the same place they did
originally.

## 2. The no-overwrite write guard

```{admonition} Your files are protected
:class: tip
The setup cell imports **`repro_guard`**, which patches every common write call
(`to_csv`, `to_hdf`, `write_h5ad`, `savefig`, `np.save`, `joblib.dump`,
`cooler.create_cooler`, builtin `open('w')`, and shell redirects in `os.system`). The
rule is simple:

* **If the target file already exists → the write is skipped** (you'll see
  `[repro_guard] skip existing: <path>`), so nothing is clobbered.
* **If it does not exist → the write proceeds**, creating any missing parent folders.
```

This matters because these notebooks were written to *generate* the shared data, not
just plot it. **41 write statements point back into the shared project tree** — e.g.
`clustering/merged/5kCG100k3C_summary.h5ad`, `L1color.tsv`, `cluster_meta.tsv`,
`group_meta.tsv`, DMR/PMD beds. Without the guard, re-running a "figure" notebook could
silently overwrite inputs that other notebooks depend on. With the guard on (the
default), those writes are skipped because the files already exist, and you still get
every figure that is *missing* regenerated.

If you deliberately want to regenerate an intermediate from scratch, either delete the
stale file first, or opt in explicitly:

```python
import repro_guard
repro_guard.activate(overwrite=True)   # DANGER: allows overwriting existing files
```

## 3. Run order and shared-file collisions

A handful of notebooks are **pipelines** that must run before the figure notebooks that
consume their outputs, and a few pairs write the *same* intermediate filename. These
are called out in each figure chapter's "Run order & cautions" note. The most important:

- **Fig. 1:** `09.pairwise_prediction` generates `cluster_meta.tsv`, `group_meta.tsv`
  and the allc/cool merge lists consumed by 07, 08, 10, 11, 12 and downstream figures —
  run it first.
- **Fig. 4:** `04.compartment → 05.diffcomp_majortype → (07, 08)`; `07 → 10` (notebook
  10 rewrites `diff_loop/all/merged_loop.hdf`); `08 → 09`.
- **Fig. 5:** `03.mCoverCompboundary` and `04.mCoverDomainboundary` both write
  `mCG_distribution/L1_chrom5k_mCG.hdf` / `..._mCH.hdf`; `01` and `04` both write
  `mCG_distribution/L1_global_mCG.tsv.gz`. Run one, or the guard will skip the second.
- **Fig. 6:** `09.NTbSchw_clustering` ends with stale copied cells that target the
  `Mus-Skl/` products — these are removed in the book copy (see the Fig. 6 chapter).

## 4. A note on cell numbers

Cell indices cited in the figure chapters (e.g. "c34") are **indicative pointers to the
notebook body**, not exact positions — find the panel by its `savefig` name / content. Note
the book prepends **two cells** to every notebook (a title cell and the environment-setup
cell), so a panel at body-cell *N* renders at position *N + 2*. Where an exact cell still
needs confirming, it is listed in `REVIEW_NEEDED.md`.

## 5. Two compute environments

Methylation notebooks use **ALLCools**; chromatin-contact notebooks use **cooler /
scHiCluster**. See **[Environment & build](setup.md)** for the two conda environments.
