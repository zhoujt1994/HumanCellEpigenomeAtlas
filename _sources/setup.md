# Environment & build

## Compute environments

The analysis spans two families of tools that don't share a single dependency set, so
the original work used **two conda environments**. Match the interpreter to the
notebook's modality (each chapter notes which one it needs).

### `allcools` — DNA methylation notebooks

Used by all mCG / mCH notebooks (Fig. 1–3, 5, 6). Built around
[ALLCools](https://lhqing.github.io/ALLCools/).

```bash
conda create -n allcools python=3.8
conda activate allcools
pip install "ALLCools==1.1.1" scanpy==1.10.2 anndata==0.9.2 \
            pysam==0.22.1 pyBigWig scikit-learn==1.3.2 scipy==1.10.1 \
            seaborn joblib pynndescent
```

### `hic` — chromatin-contact notebooks

Used by the loop / compartment / domain notebooks (Fig. 4, parts of Fig. 1, 5, 6).
Needs [cooler](https://cooler.readthedocs.io/) and
[scHiCluster](https://zhoujt1994.github.io/scHiCluster/) (the `hicluster` CLI for
`merge-cool`, `domain`, `loop`, imputation).

```bash
conda create -n hic python=3.12
conda activate hic
pip install cooler==0.10.4 "ALLCools" scHiCluster scanpy anndata pysam \
            pyBigWig scikit-learn scipy seaborn cooltools
```

```{admonition} Which env?
:class: tip
Rule of thumb: if the setup cell / imports pull in `cooler`, `schicluster`, or read
`*.cool` files, use the **`hic`** env; otherwise use **`allcools`**. A few integrative
notebooks (Fig. 4 `loop_rna`, Fig. 5, Fig. 6) touch both — run them in `hic` (which
also has ALLCools installed).
```

### Extra tools for specific supplementary panels

| Tool | Panels |
|------|--------|
| [dcHiC](https://github.com/ay-lab/dcHiC) (R) | Fig. 4E / S24 differential compartments |
| [pycisTarget / SCENIC+](https://scenicplus.readthedocs.io/) | Fig. 2O, S13E, S21B, Fig. 5H motif enrichment |
| [HOMER](http://homer.ucsd.edu/homer/) | Fig. 3 / S21 motif enrichment |
| [LDSC](https://github.com/bulik/ldsc) | Fig. S29 heritability partitioning |
| `bedtools` | DMR / loop / peak overlaps throughout |

## Building the book

```bash
pip install jupyter-book
cd HumanCellEpigenomeAtlas
jupyter-book build .
# open _build/html/index.html
```

The book is configured with **execution off** (`_config.yml`): it renders the code and
the reference figure images without running the notebooks, so you can build it without
the multi-terabyte data. To actually reproduce a panel, open the notebook, set
`ENTEX_ROOT` (see the [Reproduction guide](reproduce.md)), and run it in the right
environment.

## Repository layout

```
HumanCellEpigenomeAtlas/
├── _config.yml            # Jupyter Book config (execution off)
├── _toc.yml               # table of contents
├── intro.md               # landing page
├── setup.md               # this page
├── data.md                # data availability
├── reproduce.md           # path convention + no-overwrite guard
├── repro_guard.py         # the write guard imported by every notebook
├── figures/               # reference PNGs of the published figures
├── fig1/  …  fig6/         # one folder per main figure: chapter .md + notebooks
```
