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

## B. Code errors — under investigation (full-scale re-run in progress)
These errored with NO missing file. Several are almost certainly **downsample artifacts**
(capping a loop to 1 breaks hardcoded cell-type indices — e.g. fig2/02's `-f` path). A
full-scale re-run is running to separate real bugs from artifacts; real ones will be fixed
against the originals in `analysis/`.

`clustering/05,06`, `fig1/06.compare_bulkmc`, `fig1/07.compare_bulkhic`, `fig2/01.mCG_distribution`,
`fig2/04.PMD_ATAC`, `fig2/05.PMD_RNA`, `fig2/10.peak_mCG_motif`, `fig2/13.PMD_DMR`,
`fig3/04.mCH_mCG_comp`, `fig3/06.mCH_clustering`, `fig4/02.decay_compartment`,
`fig5/03.mCoverCompboundary`, `fig5/04.loop_dmr_enrichment`, `fig6/03.MusSkl_diff_7group`,
`fig6/04.NTbSchw_clustering`, `fig6/05.Epi-TPB`.

## Ran clean (32)
clustering/07; fig1/01,02,03,04,05; fig2/03,06,07,09,11,12,15; fig3/02,05,07; fig4/01,03,04,05,06,08,09,10; fig5/01,02,05,07; fig6/01,02,06,07.
