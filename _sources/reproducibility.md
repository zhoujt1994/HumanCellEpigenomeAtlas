# Reproducibility status

Each notebook was **re-executed fresh, read-only** (no disk writes; inline figures render) in the `analysis` env with per-cell/per-notebook time caps. This records which figures the code reproduces from the shared `allc`/`cool`/`loop`/`DMR` files.

```{admonition} Method
Guard = read-only (savefig skipped). Expensive DMR/loop/compartment/clustering *calling* is time-capped and skipped (results loaded from cache). ✅ = all cells ran and produced figures. ⚠ = produces most figures but errors on a few cells (blocker noted).
```

## ✅ Confidently reproduced (fresh run, all figures)

**27 notebooks:** `fig1/01.clustering_summary.ipynb`, `fig1/03.method_clustering.ipynb`, `fig1/07.dendrogram_annot.ipynb`, `fig2/01.mCG_distribution.ipynb`, `fig2/03.PMD_RNA.ipynb`, `fig2/04.DMR_stats.ipynb`, `fig2/05.DMR_overlap_ATAC.ipynb`, `fig2/07.TE_mCG.ipynb`, `fig2/08.PMD_calling_insulation.ipynb`, `fig2/10.PMD_donor.ipynb`, `fig2/15.PMD_ATAC.ipynb`, `fig2/18.DMR_loop_sLDSC.ipynb`, `fig3/05.mCH_mCG_scale.ipynb`, `fig3/06.mCH_mCG_comp.ipynb`, `fig3/07.mCH_clustering.ipynb`, `fig3/09.mCH_geneflank.ipynb`, `fig4/02.decay_compartment.ipynb`, `fig4/03.decay_domain.ipynb`, `fig4/04.compartment.ipynb`, `fig4/05.diffcomp_majortype.ipynb`, `fig4/07.diffloop_majortype.ipynb`, `fig4/08.diffloop_subtype.ipynb`, `fig4/09.loop_rna.ipynb`, `fig4/10.loop_comp.ipynb`, `fig6/02.MusSkl_donor_clustering.ipynb`, `fig6/03.MusSkl_diffloop.ipynb`, `fig6/08.Epi-Gas.ipynb`

## ⚠ Not yet confident — blocker per notebook
Most already produce many figures; the blocker is a missing cell/intermediate or a shell cell. Per the author, unrelated/broken cells can be deleted from the book.

| Notebook | figs | blocker |
|---|---|---|
| `fig1/02.m3c_blacklist.ipynb` | 2 | missing cell/import: `tmp` |
| `fig1/04.method_anchor.ipynb` | 5 | missing precomputed key: `wnn_pc15_tsne` |
| `fig1/05.modality_contribution.ipynb` | 3 | missing precomputed key: `5kCG100k3C_u22pc9` |
| `fig1/06.downsample_clustering.ipynb` | 2 | c17:ValueError: invalid literal for int() with base 10: '/ho |
| `fig1/08.L2both_per_celltype.ipynb` | 0 | missing intermediate on disk (pipeline output) |
| `fig1/09.pairwise_prediction.ipynb` | 3 | c10:KeyError: "None of ['leiden_init'] are in the columns" |
| `fig1/10.compare_bulkmc.ipynb` | 9 | bed read without header (chrom/start/end) |
| `fig1/11.compare_bulkhic.ipynb` | 3 | multiprocessing worker crash |
| `fig1/12.L2any_L2both_diffloop.ipynb` | 0 | missing intermediate on disk (pipeline output) |
| `fig2/02.PMD_hetero.ipynb` | 40 | missing cell/import: `significant_pc_test` |
| `fig2/06.DMR_motif.ipynb` | 0 | bash/shell cell (needs `!` or is a pipeline command; not a plot) |
| `fig2/09.PMD_cell-by-site.ipynb` | 6 | missing cell/import: `sels` |
| `fig2/11.PMD_Hema-Tmem.ipynb` | 10 | c18:KeyError: "None of [Index(['celltype', 'batch'], dtype=' |
| `fig2/12.PMD_Epi-TPB.ipynb` | 24 | missing intermediate on disk (pipeline output) |
| `fig2/13.PMD_histone.ipynb` | 26 | c52:KeyError: "None of [Index([('t', 'i', 's', 's', 'u', 'e' |
| `fig2/14.PMD_DMR.ipynb` | 8 | missing cell/import: `group_name` |
| `fig2/16.peak_mCG_motif.ipynb` | 9 | bash/shell cell (needs `!` or is a pipeline command; not a plot) |
| `fig2/17.geneCG_expr_corr.ipynb` | 5 | bed read without header (chrom/start/end) |
| `fig3/01.global_mCH.ipynb` | 2 | missing intermediate on disk (pipeline output) |
| `fig3/02.mCH_distribution.ipynb` | 45 | palette key (residual) |
| `fig3/03.mC_context_lambda.ipynb` | 19 | c29:ValueError: 'c' argument has 420 elements, which is inco |
| `fig3/04.mCH_mCG_corr.ipynb` | 9 | missing cell/import: `thres` |
| `fig3/08.mCH_hetero.ipynb` | 0 | NO_FIG |
| `fig3/10.mCH_geneplot.ipynb` | 6 | bed read without header (chrom/start/end) |
| `fig4/01.decay.ipynb` | 11 | c10:AttributeError: 'dict' object has no attribute 'index' |
| `fig4/06.domainloop_stats.ipynb` | 6 | missing intermediate on disk (pipeline output) |
| `fig5/01.genome_mCG_compartment.ipynb` | 7 | bed read without header (chrom/start/end) |
| `fig5/02.comp_pmd.ipynb` | 16 | missing cell/import: `mcgall` |
| `fig5/03.mCoverCompboundary.ipynb` | 34 | bed read without header (chrom/start/end) |
| `fig5/04.mCoverDomainboundary.ipynb` | 0 | NO_FIG |
| `fig5/05.loop_dmr_enrichment.ipynb` | 1 | bash/shell cell (needs `!` or is a pipeline command; not a plot) |
| `fig5/06.loop_dmr_motif.ipynb` | 0 | bash/shell cell (needs `!` or is a pipeline command; not a plot) |
| `fig5/07.L2any_L2both.ipynb` | 71 | bash/shell cell (needs `!` or is a pipeline command; not a plot) |
| `fig6/01.MusSkl_clustering.ipynb` | 3 | missing cell/import: `tmp3c` |
| `fig6/04.MusSkl_diff.ipynb` | 7 | missing intermediate on disk (pipeline output) |
| `fig6/05.MusSkl_diff_3group.ipynb` | 43 | missing cell/import: `leg` |
| `fig6/06.MusSkl_diff_7group.ipynb` | 16 | missing cell/import: `leg` |
| `fig6/07.Epi-TPB.ipynb` | 6 | bash/shell cell (needs `!` or is a pipeline command; not a plot) |
| `fig6/09.NTbSchw_clustering.ipynb` | 5 | missing cell/import: `filter_regions` |

## Excluded — not in the paper

`fig6/10–14` (colon/stomach **mCT** notebooks) — the author confirmed no mCT data is shown in the paper. To be dropped from the book.
