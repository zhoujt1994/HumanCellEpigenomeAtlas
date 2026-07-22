# Human Body Single-Cell Atlas of 3D Genome Organization and DNA Methylation

Analysis code and a figure-by-figure reproduction guide for
**Zhou, Wu, Liu, et al., "Human Body Single-Cell Atlas of 3D Genome Organization and
DNA Methylation."**

We profiled 3D genome structure and DNA methylation for **86,689 single nuclei across 16
human tissues** (snm3C-seq), identifying **35 major and 206 cell subtypes**.

This repository is organized as a **[Jupyter Book](https://jupyterbook.org/)**: each main
figure (Fig. 1–6) is a chapter that maps every panel — including the Extended Data figures
S1–S32 — to the notebook and cells that produce it.

## Quick start

```bash
git clone https://github.com/zhoujt1994/HumanCellEpigenomeAtlas.git
cd HumanCellEpigenomeAtlas

# build the book (renders code + reference figures; does not execute notebooks)
pip install jupyter-book
jupyter-book build .
open _build/html/index.html
```

To actually **reproduce a panel**, open its notebook, set `ENTEX_ROOT` to your copy of the
data, and run it in the right conda environment. See:

- **`setup.md`** — the two conda environments (`allcools` for methylation, `hic` for
  chromatin contacts) and extra tools.
- **`data.md`** — where every input dataset lives (Zenodo, Hugging Face, GCS, GEO).
- **`reproduce.md`** — the single editable path (`ENTEX_ROOT`) and the **no-overwrite
  write guard** (`repro_guard.py`) that stops a re-run from clobbering your files.
- **`gaps.md`** — panels that are hand-made, or whose plotting cell is missing.

## Reproduction safety

Every notebook begins with a setup cell that (1) centralizes absolute paths into
`ENTEX_ROOT` / `REF_ROOT`, (2) `chdir`s to the original working directory, and (3) imports
`repro_guard`. The guard patches all common write calls so that **a write whose target
already exists is skipped** (you'll see `[repro_guard] skip existing: …`) and only missing
outputs are (re)generated. This is important because many "figure" notebooks were written
to *generate* shared data and would otherwise overwrite it.

## Repository layout

```
├── intro.md · setup.md · data.md · reproduce.md · gaps.md   # front matter
├── _config.yml · _toc.yml                                   # Jupyter Book
├── repro_guard.py                                           # no-overwrite guard
├── figures/                                                 # reference PNGs of the paper figures
├── fig1/ … fig6/     # one folder per main figure: <figN>.md chapter + notebooks
└── LICENSE
```

## Data & code archive

- **Code (Zenodo):** [10.5281/zenodo.19394035](https://doi.org/10.5281/zenodo.19394035)
- **Single-cell mCH / contacts (Hugging Face):**
  `zhoujt1994/HumanCellEpigenomeAtlas_sc_allc`,
  `zhoujt1994/HumanCellEpigenomeAtlas_sc_contact`
- Pseudobulk allc / cool / loops, DMRs, PMDs, and compartments — see `data.md`.

## Citation

If you use this atlas, please cite the paper (and the Zenodo code archive). See `LICENSE`
for terms.
