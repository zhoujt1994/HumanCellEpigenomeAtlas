# Reproducibility status

Every notebook was **re-executed fresh, read-only** (no disk writes; inline figures render) in the `analysis` env, reading data from the shared `allc`/`cool`/`loop`/`DMR` files. **30 of 67 figure notebooks reproduce all their panels** so far.

```{admonition} Legend
✅ CLEAN = all cells ran, figures produced (reproduced from scratch). The 5 mCT notebooks (`fig6/10–14`) are excluded — not in the paper.
```

## ✅ Reproduced (30)

`fig1/01.clustering_summary.ipynb`, `fig1/03.method_clustering.ipynb`, `fig1/07.dendrogram_annot.ipynb`, `fig2/01.mCG_distribution.ipynb`, `fig2/03.PMD_RNA.ipynb`, `fig2/04.DMR_stats.ipynb`, `fig2/05.DMR_overlap_ATAC.ipynb`, `fig2/07.TE_mCG.ipynb`, `fig2/08.PMD_calling_insulation.ipynb`, `fig2/10.PMD_donor.ipynb`, `fig2/15.PMD_ATAC.ipynb`, `fig2/18.DMR_loop_sLDSC.ipynb`, `fig3/03.mC_context_lambda.ipynb`, `fig3/05.mCH_mCG_scale.ipynb`, `fig3/06.mCH_mCG_comp.ipynb`, `fig3/07.mCH_clustering.ipynb`, `fig3/09.mCH_geneflank.ipynb`, `fig3/10.mCH_geneplot.ipynb`, `fig4/02.decay_compartment.ipynb`, `fig4/03.decay_domain.ipynb`, `fig4/04.compartment.ipynb`, `fig4/05.diffcomp_majortype.ipynb`, `fig4/07.diffloop_majortype.ipynb`, `fig4/08.diffloop_subtype.ipynb`, `fig4/09.loop_rna.ipynb`, `fig6/02.MusSkl_donor_clustering.ipynb`, `fig6/03.MusSkl_diffloop.ipynb`, `fig6/06.MusSkl_diff_7group.ipynb`, `fig6/07.Epi-TPB.ipynb`, `fig6/08.Epi-Gas.ipynb`

## Data-prep, no saved panel (2)
`fig3/08.mCH_hetero.ipynb`, `fig5/04.mCoverDomainboundary.ipynb`

## ⚠ Blocked (35) — one blocker each; most already produce many figures

| Notebook | figs | blocker |
|---|---|---|
| `fig1/02.m3c_blacklist.ipynb` | 2 | missing cell/import: `tmp` |
| `fig1/04.method_anchor.ipynb` | 5 | missing key: `wnn_pc15_tsne` |
| `fig1/05.modality_contribution.ipynb` | 3 | missing key: `5kCG100k3C_u22pc9` |
| `fig1/06.downsample_clustering.ipynb` | 2 | c18:ValueError: invalid literal for int() with bas |
| `fig1/08.L2both_per_celltype.ipynb` | 0 | missing intermediate on disk |
| `fig1/09.pairwise_prediction.ipynb` | 3 | c11:KeyError: "None of ['leiden_init'] are in the  |
| `fig1/10.compare_bulkmc.ipynb` | 9 | bed read without header |
| `fig1/11.compare_bulkhic.ipynb` | 3 | worker crash |
| `fig1/12.L2any_L2both_diffloop.ipynb` | 0 | missing intermediate on disk |
| `fig2/02.PMD_hetero.ipynb` | 40 | missing cell/import: `significant_pc_test` |
| `fig2/06.DMR_motif.ipynb` | 0 | shell/pipeline cell (not a plot) |
| `fig2/09.PMD_cell-by-site.ipynb` | 6 | missing cell/import: `sels` |
| `fig2/11.PMD_Hema-Tmem.ipynb` | 10 | c19:KeyError: "None of [Index(['celltype', 'batch' |
| `fig2/12.PMD_Epi-TPB.ipynb` | 24 | missing intermediate on disk |
| `fig2/13.PMD_histone.ipynb` | 26 | c52:KeyError: "None of [Index([('t', 'i', 's', 's' |
| `fig2/14.PMD_DMR.ipynb` | 8 | missing cell/import: `group_name` |
| `fig2/16.peak_mCG_motif.ipynb` | 9 | shell/pipeline cell (not a plot) |
| `fig2/17.geneCG_expr_corr.ipynb` | 5 | bed read without header |
| `fig3/01.global_mCH.ipynb` | 2 | missing intermediate on disk |
| `fig3/02.mCH_distribution.ipynb` | 45 | palette key |
| `fig3/04.mCH_mCG_corr.ipynb` | 9 | missing cell/import: `thres` |
| `fig4/01.decay.ipynb` | 10 | missing cell/import: `L1colors` |
| `fig4/06.domainloop_stats.ipynb` | 6 | missing intermediate on disk |
| `fig4/10.loop_comp.ipynb` | 3 | missing cell/import: `sel` |
| `fig5/01.genome_mCG_compartment.ipynb` | 7 | bed read without header |
| `fig5/02.comp_pmd.ipynb` | 16 | missing cell/import: `mcgall` |
| `fig5/03.mCoverCompboundary.ipynb` | 34 | bed read without header |
| `fig5/05.loop_dmr_enrichment.ipynb` | 1 | shell/pipeline cell (not a plot) |
| `fig5/06.loop_dmr_motif.ipynb` | 0 | shell/pipeline cell (not a plot) |
| `fig5/07.L2any_L2both.ipynb` | 71 | shell/pipeline cell (not a plot) |
| `fig5/08.pycistarget_loopDMR.ipynb` | ? |  |
| `fig6/01.MusSkl_clustering.ipynb` | 3 | missing cell/import: `tmp3c` |
| `fig6/04.MusSkl_diff.ipynb` | 7 | missing intermediate on disk |
| `fig6/05.MusSkl_diff_3group.ipynb` | 43 | missing cell/import: `leg` |
| `fig6/09.NTbSchw_clustering.ipynb` | 5 | missing cell/import: `filter_regions` |

## Excluded — not in the paper
`fig6/10–14` (colon/stomach mCT) — no mCT data shown in the paper.
