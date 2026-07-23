# Reproducibility status

Notebooks re-executed **fresh, read-only** in the `analysis` env from the shared `allc`/`cool`/`loop`/`DMR` files, after the map-driven cleanup. The book renders each notebook's **saved** panel outputs, so a re-run blocker on a *later* cell does not affect the displayed figures — it flags a reproduce-from-scratch gap.

Two recovered notebooks (`fig6/00` Fig 6A+6D, `fig3/10` Fig 3I+S23B) are freshly executed and CLEAN.

## ✅ Re-run CLEAN (22)

`fig1/02.m3c_blacklist`, `fig1/03.method_clustering`, `fig1/07.dendrogram_annot`, `fig1/10.compare_bulkmc`, `fig1/11.compare_bulkhic`, `fig2/01.mCG_distribution`, `fig2/05.DMR_overlap_ATAC`, `fig2/10.PMD_donor`, `fig2/15.PMD_ATAC`, `fig2/16.peak_mCG_motif`, `fig2/18.DMR_loop_sLDSC`, `fig3/03.mC_context_lambda`, `fig3/05.mCH_mCG_scale`, `fig3/06.mCH_mCG_comp`, `fig3/07.mCH_clustering`, `fig3/09.mCH_geneflank`, `fig4/02.decay_compartment`, `fig4/07.diffloop_majortype`, `fig4/09.loop_rna`, `fig5/05.loop_dmr_enrichment`, `fig6/02.MusSkl_donor_clustering`, `fig6/07.Epi-TPB`

## ⚠ Panels render, but a later cell blocks full re-run (20)

| Notebook | blocker |
|---|---|
| `fig1/01.clustering_summary` | out-of-order var |
| `fig1/04.method_anchor` | missing wnn embedding |
| `fig1/08.L2both_per_celltype` | missing intermediate / other-host path |
| `fig2/02.PMD_hetero` | missing import |
| `fig2/03.PMD_RNA` | shell/magic cell |
| `fig2/04.DMR_stats` | shell/magic cell |
| `fig2/07.TE_mCG` | shell/magic cell |
| `fig2/13.PMD_histone` | c48:KeyError: "None of [Index([('t', 'i' |
| `fig3/02.mCH_distribution` | stale name in data file |
| `fig3/04.mCH_mCG_corr` | out-of-order var |
| `fig4/01.decay` | missing intermediate / other-host path |
| `fig4/06.domainloop_stats` | missing intermediate / other-host path |
| `fig4/10.loop_comp` | out-of-order var |
| `fig5/01.genome_mCG_compartment` | bed read w/o header |
| `fig5/02.comp_pmd` | out-of-order var |
| `fig5/03.mCoverCompboundary` | bed read w/o header |
| `fig5/07.L2any_L2both` | missing intermediate / other-host path |
| `fig5/08.pycistarget_loopDMR` | missing intermediate / other-host path |
| `fig6/06.MusSkl_diff_7group` | c13:NameError: name 'leg' is not defined |
| `fig6/09.NTbSchw_clustering` | c11:NameError: name 'filter_regions' is  |

Blocker classes: shell/magic cells, out-of-order variables (author ran cells non-linearly), missing intermediates or a coauthor's hardcoded path, a stale name in a cached data file, and a couple of bed-header reads. Being fixed incrementally.
