# Reproducibility status

Every figure notebook re-executed **fresh, read-only** in the `analysis` env from the shared `allc`/`cool`/`loop`/`DMR` files. The book renders each notebook's **saved** panel outputs, so panels display even where a fresh re-run stops on a later cell.

**29 of 42 figure notebooks re-run fully CLEAN.** The rest render their panels but stop later on a fresh run — see [`NONCONFIDENT.md`](NONCONFIDENT.md) for the itemized reasons (missing data / external paths vs deeper code issues).

## ✅ Re-run CLEAN (29)

`fig1/01.clustering_summary`, `fig1/02.m3c_blacklist`, `fig1/03.method_clustering`, `fig1/07.dendrogram_annot`, `fig1/10.compare_bulkmc`, `fig1/11.compare_bulkhic`, `fig2/01.mCG_distribution`, `fig2/03.PMD_RNA`, `fig2/04.DMR_stats`, `fig2/05.DMR_overlap_ATAC`, `fig2/10.PMD_donor`, `fig2/15.PMD_ATAC`, `fig2/16.peak_mCG_motif`, `fig2/18.DMR_loop_sLDSC`, `fig3/02.mCH_distribution`, `fig3/03.mC_context_lambda`, `fig3/05.mCH_mCG_scale`, `fig3/06.mCH_mCG_comp`, `fig3/07.mCH_clustering`, `fig3/09.mCH_geneflank`, `fig4/02.decay_compartment`, `fig4/07.diffloop_majortype`, `fig4/09.loop_rna`, `fig4/10.loop_comp`, `fig5/02.comp_pmd`, `fig5/03.mCoverCompboundary`, `fig5/05.loop_dmr_enrichment`, `fig6/02.MusSkl_donor_clustering`, `fig6/07.Epi-TPB`

## ⚠ Panels render; fresh re-run blocked later (13)

`fig1/04.method_anchor`, `fig1/08.L2both_per_celltype`, `fig2/02.PMD_hetero`, `fig2/07.TE_mCG`, `fig2/13.PMD_histone`, `fig3/04.mCH_mCG_corr`, `fig4/01.decay`, `fig4/06.domainloop_stats`, `fig5/01.genome_mCG_compartment`, `fig5/07.L2any_L2both`, `fig5/08.pycistarget_loopDMR`, `fig6/06.MusSkl_diff_7group`, `fig6/09.NTbSchw_clustering`

See `NONCONFIDENT.md` for each blocker and which panel (if any) it leaves blank.
Two recovered notebooks (`fig6/00`, `fig3/10`) and `fig2/12` (Fig 6I/6J) render from fresh bakes.
