# Reproducibility status — regenerated from a full-execution pass (2026-07-26)

Every notebook was executed fresh from the assumed-available inputs (mcds, DMR ds, loop
bedpe+cool, cluster annotation), read-only, `os.system` neutralized, loops downsampled to the
first element. **32 / 61 ran clean; 29 hit an error.** The errors split into (A) genuinely
missing input files and (B) code errors still under investigation (some are downsample
artifacts, being confirmed by a full-scale re-run).

## A. Genuinely missing input data (needs the file, or confirmation it's unavailable)

| Notebook | Missing file(s) | Note |
|---|---|---|
| `clustering/01–04` (pipeline) | `tissue/{t}/data/raw/*.npz` (per-cell 3C, from scHiCluster), `clustering/merged/cell_86689_16tissue_100k3C_autosomal.h5ad` + `…_meta.csv.gz`, `5kCG.h5ad`, `5kCG100k3C_embed.h5ad`, `L1pre/*.h5ad` | Root gap = the per-cell **3C `raw/*.npz`** and the all-cell **`cell_86689…`** matrices. The chain then fails downstream (each step's input is the prior step's output). mCG side is self-contained from the mcds. |
| `fig2/02.PMD_hetero` | `PMD/L1/c35_hist_kmeans4.bed` | c35 = a merged major type; its PMD-hist bed is absent. |
| `fig2/08.DMR_overlap_ATAC` | `DMR/flank_bed/…c33.CGN-Merge.hdf` | flank-mCG hdf for the ATAC-overlap analysis. |
| `fig2/14.PMD_Hema-Tmem` | `PMD_RNA/Hema-Tmem-PBMC/*` (`_dmr.mcds`, `*_gene.bed`, `closest_tss.txt`, `hg38_20kbin.bed`) | These are the outputs of `fig2/13.PMD_DMR`'s external allc-merge step (documented prerequisite); not on disk. |
| `fig3/01.mCH_distribution` | `mCH_distribution/multires/{ct}_hist.npy`, `{ct}_corr_50.npy` | multires mCH intermediates. |
| `fig3/03.mCH_geneflank` | `mCH_geneflank/…CHN-both.tsv` | bigWigAverageOverBed flank output. |
| `fig3/08.global_mCH` | `merged/ALL_lambda.csv.gz` | **Code bug FIXED** (old `/data/ENTEx` path → `{ENTEX_ROOT}`); 2/3 files now resolve, only the lambda spike-in table is genuinely missing. |
| `fig4/07.decay_domain` | `merged_cool_raw/L1/c35.mcool` | raw 100 kb cool for merged type c35. |
| `fig5/06.pycistarget_loopDMR` (Fig 5H) | `loop_dmr_motif/…loopdmr_TF_all.hdf` | pycisTarget/SCENIC+ output (documented — refer to pycisTarget; ship precomputed). |

## B. Code errors — full-scale re-run results (real causes)

**Fixed this pass:**
- `fig4/02.decay_compartment`, `fig5/04.loop_dmr_enrichment` — `'vlag' is not a valid cmap`: added `import seaborn as sns` (seaborn registers `vlag` on import; missed earlier because they use the string `'vlag'` in `imshow`, not `sns.`).

**Data-version mismatch** (code expects columns/variables the current on-disk data no longer has — needs the matching data version, or code updated to the current schema):
- `fig1/06.compare_bulkmc`, `fig3/06.mCH_clustering` — `None of ['chrom','start','end']` (bed-header) + `chrom1k_da_frac`/`celltype_L2_both_abbr` not present.
- `fig2/10.peak_mCG_motif` — mcds has no `peak_da_frac` quantifier.
- `fig2/04.PMD_ATAC`, `fig3/04.mCH_mCG_comp` — `['kmeans3'] not in index` (+ `'Neu Schw'`).
- `fig2/01.mCG_distribution` — palette dict missing key `'c7'` (raw cluster merged into c35/c36).
- `fig2/05.PMD_RNA` — reshape size mismatch.

**Template placeholder:** `fig2/13.PMD_DMR` — `group_name` undefined (like the old fig2/14; needs a group assigned to run standalone).

**Out-of-order / missing prior variable** (fixable by restoring the defining cell/order):
- `fig6/03.MusSkl_diff_7group` — `leg_3c`; `fig6/04.NTbSchw_clustering` — `X_tsne`/`tsne_0`; `fig6/05.Epi-TPB` — `leiden`; `fig2/10` — `data_all`.

**Resource (not a code bug):** `fig1/07.compare_bulkhic`, `fig2/01.mCG_distribution` — `BrokenProcessPool` (heavy `ProcessPoolExecutor`; needs more memory / fewer workers).

**Cache-staleness:** `fig5/03.mCoverCompboundary` — loads a stale on-disk `flankmch.joblib` (70 rows) that overrides the corrected 35-per-major-type compute; a fresh run without the cache produces 35.

**Missing-data cascade:** `clustering/05,06` — need `5kCG_embed.h5ad` which `clustering/02` (data-blocked on the 3C raw npz) never produced.


## Ran clean (32)
clustering/07; fig1/01,02,03,04,05; fig2/03,06,07,09,11,12,15; fig3/02,05,07; fig4/01,03,04,05,06,08,09,10; fig5/01,02,05,07; fig6/01,02,06,07.
