# Reproducibility status

Figure notebooks were **code-slimmed** to only panel-producing cells + their prerequisites (variable deps, intermediate-file generators, and cross-notebook write-only generators), then re-executed **fresh, read-only**. Panels render from saved outputs regardless.

**32 of 45 figure notebooks re-run fully CLEAN.** The rest render their panels but stop later on a fresh run — see [`NONCONFIDENT.md`](NONCONFIDENT.md).

## ✅ Re-run CLEAN (32)

`fig1/01.clustering_summary`, `fig1/02.m3c_blacklist`, `fig1/03.method_clustering`, `fig1/04.method_anchor`, `fig1/07.dendrogram_annot`, `fig1/10.compare_bulkmc`, `fig1/11.compare_bulkhic`, `fig2/02.PMD_hetero`, `fig2/03.PMD_RNA`, `fig2/05.DMR_overlap_ATAC`, `fig2/10.PMD_donor`, `fig2/13.PMD_histone`, `fig2/15.PMD_ATAC`, `fig2/18.DMR_loop_sLDSC`, `fig3/02.mCH_distribution`, `fig3/03.mC_context_lambda`, `fig3/05.mCH_mCG_scale`, `fig3/06.mCH_mCG_comp`, `fig3/07.mCH_clustering`, `fig3/09.mCH_geneflank`, `fig3/10.mCH_geneexpr_corr`, `fig4/02.decay_compartment`, `fig4/06.domainloop_stats`, `fig4/07.diffloop_majortype`, `fig4/09.loop_rna`, `fig5/01.genome_mCG_compartment`, `fig5/02.comp_pmd`, `fig5/03.mCoverCompboundary`, `fig5/05.loop_dmr_enrichment`, `fig5/07.L2any_L2both`, `fig6/00.mc3c_ARI`, `fig6/02.MusSkl_donor_clustering`

## ⚠ Panels render; fresh re-run blocked later (13)

`fig1/08.L2both_per_celltype`, `fig2/01.mCG_distribution`, `fig2/04.DMR_stats`, `fig2/07.TE_mCG`, `fig2/12.PMD_Epi-TPB`, `fig2/16.peak_mCG_motif`, `fig3/04.mCH_mCG_corr`, `fig4/01.decay`, `fig4/10.loop_comp`, `fig5/08.pycistarget_loopDMR`, `fig6/06.MusSkl_diff_7group`, `fig6/07.Epi-TPB`, `fig6/09.NTbSchw_clustering`

Blockers detailed in `NONCONFIDENT.md` (missing-data/external-path vs deeper-code).
