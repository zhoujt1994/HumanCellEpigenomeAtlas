# Panel ↔ output-PDF ↔ notebook map (authoritative)

Built by reading every figure PDF (`figure/figN_rev.pdf`, `figS1–S32_rev.pdf`), the legends
in `figure/manuscript.txt`, and every notebook's **rendered** plots, then matching each of the
**230 savefig outputs** to a published panel. This replaces the stale `REVIEW_NEEDED.md`.

**Rule for the book:** keep only cells that produce a published panel **plus their
prerequisites** (compute/pipeline cells they depend on). Everything marked `NONE`
(redundant duplicate, superseded variant, or exploratory/QC) is removed. `cell` = index
among **code cells only**. `{ct}`/`{group_name}`/`{version}`/`{mode}` are per-notebook loop vars.

Confidence is high unless noted. Items flagged **(confirm)** are worth a human glance.

---

## Notebook classification

**KEEP — produces ≥1 published panel:**
`fig1/01,02,03,04,07,08,10,11` · `fig2/01,02,03,04,05,07,10,13,15,16,18` ·
`fig3/02,03,04,05,06,07,09` · `fig4/01,02,06,07,09,10` · `fig5/01,02,03,05,08` ·
`fig6/02,06,07,09`

**PREREQUISITE — no saved panel, but a calling pipeline or compute step a KEEP notebook depends on:**
`fig2/06` (DMR-motif enrichment → Fig 2O/S13E, *plot cell missing*), `fig2/08,09,14` (PMD/DMR calling) ·
`fig4/03,04,05,08` (domain/compartment/diff-loop calling → feed 4C/4E/4F/4G) ·
`fig5/06,07` (loop-DMR motif compute → Fig 5H; `07` renders Fig 5I inline, never saved) ·
`fig6/01,03` (Mus-Skl base clustering/diff-loop, refined by `02`/`06`)

**DROP — no panel and not a prerequisite (exploratory / superseded / not in paper):**
`fig1/05` (modality-contribution QC heatmaps), `fig1/06` (downsample benchmark), `fig1/09` (pairwise-prediction QC), `fig1/12` (writes .npz only) ·
`fig3/08` (duplicates fig2/02 mCG/PMD plots — Fig 2 territory), `fig3/10` (marker-gene mCH tSNE, unpublished) ·
`fig5/04` (mC-over-domain-boundary, superseded by `03`) ·
`fig6/04,05` (non-7group / 3-group DMR-loop, superseded by `06`), `fig6/08` (Epi-Gas tSNEs, not in figure — **confirm**, S32G/H Epi-Gas heatmaps are a gap), `fig6/10,11,12,13,14` (colon/stomach **mCT** — not in this paper)

---

## Fig 1

| panel | output_pdf | notebook | cell |
|---|---|---|---|
| Fig 1A | tissue_legend.pdf | fig1/01 | 43 |
| Fig 1C | browser_example.pdf | fig1/01 | 17 |
| Fig 1D | All_modality_cluster.pdf | fig1/01 | 38 |
| Fig 1E | L1_tissueratio.pdf | fig1/01 | 42 |
| Fig 1F | dendrogram_..._horizontal_even.pdf | fig1/07 | 22 |
| Fig S1A | blacklist_example.svg | fig1/02 | 9 |
| Fig S2A | cemba_5kCG_100kCG_subclass.pdf | fig1/03 | 42 |
| Fig S2C/D | mc_lsi_anchormethod_{g}.pdf | fig1/04 | 6 |
| Fig S2E | TrCo_wnn_concat_leiden.pdf | fig1/04 | 23 |
| Fig S5 | tissue_celltype.pdf | fig1/08 | 22 |
| Fig S7A | cosine_subtype_Loyfer.pdf | fig1/10 | 39 |
| Fig S7B | cosine_subtype_Schultz.pdf | fig1/10 | 71 |
| Fig S8 | Ecorr_subtype_ENCODE.pdf | fig1/11 | 36 |

**Strip (NONE):** fig1/01 c37,39,59,60,61,62,63 (QC/alt-embedding tSNEs; c58 is a dup of the S5 source in fig1/08 → keep fig1/08's), fig1/07 c23 (vertical dup), fig1/11 c35 (Qcorr, not published).
Not sourced in fig1/: S2B, S3, S4, S6.

## Fig 2

| panel | output_pdf | notebook | cell |
|---|---|---|---|
| Fig 2A | L1_cellglobalCG_box.pdf | fig2/01 | 12 |
| Fig 2B | L1_siteCG_heatmap.pdf | fig2/01 | 25 |
| Fig 2C | L1_track.pdf | fig2/01 | 31 |
| Fig 2D+2E | pmd_hist_chr2-70M-85M.pdf | fig2/02 | 61 |
| Fig 2F | L1_siteCG_10kb_kmeans3.pdf | fig2/02 | 62 |
| Fig 2G+S9D | L1_10kb_hist_kmeans3_PuRd.pdf | fig2/02 | 49 |
| Fig 2H | ATAC_peak_3state_stackedbar.pdf | fig2/15 | 18 |
| Fig 2I+S11A | tss_3state_exprgroup_stackedbar.pdf | fig2/03 | 26 |
| Fig 2J+S11B | mCG_geneflank_exprgroup.pdf | fig2/03 | 24 |
| Fig 2K+S11C | tss_3state_fcgroup_pmdnonpmd_stackedbar.pdf | fig2/03 | 44 |
| Fig 2L+S11D | mCG_geneflank_fcgroup_pmdnonpmd.pdf | fig2/03 | 42 |
| Fig 2M | DMR_roadmapDMR_overlap_venn.pdf | fig2/04 | 14 |
| Fig 2N | DMR_ATACpeak_overlap_venn.pdf | fig2/05 | 37 |
| Fig 2P+S15A | TE_tsne.pdf | fig2/07 | 13 |
| Fig S9A | pmd_method_compare.pdf | fig2/02 | 54 |
| Fig S9B | L1_siteCG_multires_pmd_nonpmd_hist.pdf (+ c13 legend) | fig2/02 | 23 |
| Fig S9C | L1_track_ylim.pdf | fig2/01 | 32 |
| Fig S10A/B | {ct}.10kb_hist_donor.pdf | fig2/10 | 16 |
| Fig S10C | {ct}.10kb_hist_confusion.pdf | fig2/10 | 17 |
| Fig S10D | HemaT_10kb_hist_cross.pdf | fig2/02 | 74 |
| Fig S10E | HemaB_10kb_hist_cross.pdf | fig2/02 | 72 |
| Fig S11E | tss_3state_fcgroup_pmdsubtype_stackedbar.pdf | fig2/03 | 31 |
| Fig S11F | mCG_geneflank_fcgroup_pmdsubtype.pdf | fig2/03 | 29 |
| Fig S11G/H | PMD_histone_tissue.svg | fig2/13 | 32 |
| Fig S12A | tss_dist_hcagene.pdf | fig2/04 | 42 |
| Fig S12B | DMR_mCG_heatmap.pdf | fig2/04 | 76 |
| Fig S12C | DMR_hypohypercount_subtype.pdf | fig2/04 | 71 |
| Fig S13A | merged_DMR_ATACpeak_overlap_bar_cap.pdf | fig2/05 | 27 |
| Fig S13B | dendrogram_majortype_{nonpeak,peak}dmr.pdf | fig2/05 | 93,100 |
| Fig S13C | L1_peakdmr_nonpeakdmr_corr.pdf | fig2/05 | 104 |
| Fig S13D | L1_peakdmr_nonpeakdmr_corr_scatter.pdf | fig2/05 | 105 |
| Fig S14A | cCREs_distal2k_flankCG.pdf | fig2/05 | 65 |
| Fig S14C | peak_mCG_violin.pdf | fig2/16 | 18 |
| Fig S14D | hypo_motif.pdf | fig2/16 | 52 |
| Fig S14E | hyper_motif.pdf | fig2/16 | 54 |
| Fig S15B | TE_ARI.pdf | fig2/07 | 12 |
| Fig S29A | L1_dmr_75GWAS_fdr.pdf | fig2/18 | 18 |
| Fig S29B | L1_h2enrich_dmr_diff_75GWAS.pdf | fig2/18 | 24 |

**Strip (NONE):** fig2/01 c26 · fig2/02 c50,69,81,98(dup 2A) · fig2/03 c5,25,30,32,33,38,39,43,45,46,47,50,51 (TSS/DEG variants + volcanoes) · fig2/05 c25,43(dup 2M),94(dup),101(dup) · fig2/07 c19 · fig2/13 c25,26 · fig2/18 c23.
**Gap:** Fig 2O + Fig S13E (DMR TF-motif dot plots) — `fig2/06` computes the enrichment (Table S2) but has no plot cell.

## Fig 3

| panel | output_pdf | notebook | cell |
|---|---|---|---|
| Fig 3A | L1_cellglobalCH_box.pdf | fig3/02 | 18 |
| Fig 3B | L1_context_scatter.pdf | fig3/03 | 24 |
| Fig 3C | autocorr_100kb_res{res}b_L1_context_heatmap.pdf (crop of S19A) | fig3/05 | 26 |
| Fig 3D | L1_geneannot_mCH_heatmap.pdf | fig3/09 | 97 |
| Fig 3E | L1_annot_mCH_heatmap.pdf | fig3/09 | 57 |
| Fig 3F | CGcomp_flankCH.pdf | fig3/06 | 19 |
| Fig 3G | All_100kCH_meta.pdf | fig3/07 | 35 |
| Fig 3H | L1_mCH_seurat_tsne_celltype.pdf (crop of S22) | fig3/07 | 48 |
| Fig S17A | L1_mCcontext_corr_res50k_grouped.pdf | fig3/02 | 84 |
| Fig S17B | L1_mCcontext_corr_resall.pdf | fig3/02 | 85 |
| Fig S18 | L1group_mCcontext_corr.pdf | fig3/02 | 97 |
| Fig S19A | autocorr_..._L1_context_heatmap.pdf | fig3/05 | 26 |
| Fig S19B | autocorr_..._context_L1_line.pdf | fig3/05 | 27 |
| Fig S20 | mCH_group_DNMT_expr.pdf | fig3/02 | 93 |
| Fig S21A | highCA_lowCG_lowCA_lowCG_annot_fc.pdf | fig3/04 | 41 |
| Fig S21B | lowCG_highCA_vs_lowCA_motif_pvalue.pdf | fig3/04 | 49 |
| Fig S22 | L1_mCH_seurat_tsne_celltype.pdf | fig3/07 | 48 |
| Fig S23A | 100kCH_L1_rocpr.pdf | fig3/07 | 40 |

**Strip (NONE):** fig3/01 c13 · fig3/02 c16,17(overwritten),28 · fig3/04 c50 · fig3/05 c20,21,39 · fig3/07 c34(overwritten),54 · fig3/09 c49,96.
**Gap:** Fig 3I, Fig S23B, Fig S16A/B — not produced in fig3/.

## Fig 4

| panel | output_pdf | notebook | cell |
|---|---|---|---|
| Fig 4A | cell_{N}_majortype_decay.pdf | fig4/01 | 13 |
| Fig 4B | cell_{N}_majortype_decay_boxplot.pdf | fig4/01 | 16 |
| Fig 4C | comp{diff,sum}_shortlong_lineplot.pdf | fig4/02 | 21,25 |
| Fig 4D | loop_length_box.pdf | fig4/06 | 14 |
| Fig 4E | majortype_diffloop_comp.pdf | fig4/10 | 22 |
| Fig 4F | diffloop_{gtmp}.pdf | fig4/09 | 52 |
| Fig 4G | EpiBrst_diffloop_deg_heatmap.pdf | fig4/09 | 37 |
| Fig S24A | comp{diff,sum}_dist_heatmap.pdf | fig4/02 | 20,22 |
| Fig S24B | celltype_ratio_compstr_{impute,raw}_corr.pdf (confirm: 4 vs 5 cols) | fig4/01 | 46,50 |
| Fig S25A | loop_stats_bar.pdf | fig4/06 | 16 |
| Fig S25B | domain_length_bar.pdf | fig4/06 | 8 |
| Fig S25C | domain_{raw,impute}_length_box.pdf | fig4/06 | 6,7 |
| Fig S25D | {group_name}_diffloop_apa{,score}.pdf | fig4/07 | 55,57 |

**Strip (NONE):** fig4/01 c14,20,31,52,77,80 · fig4/06 c15 · fig4/10 c23(dup of c22).

## Fig 5

| panel | output_pdf | notebook | cell |
|---|---|---|---|
| Fig 5A | mCG_comp_{mode}_corr.pdf | fig5/01 | 29 |
| Fig 5B | mCH_comp_{mode}_corr.pdf | fig5/01 | 53 |
| Fig 5C | corr_comp_mCG.pdf | fig5/02 | 30 |
| Fig 5D | corr_comp_mCG_zoomin.pdf | fig5/02 | 31 |
| Fig 5E | comp_pmd_comporder_kmeans10_nonbrain.pdf | fig5/02 | 15 |
| Fig 5F | comp_boundary_flankmCG.pdf | fig5/03 | 36 |
| Fig 5G | comp_boundary_flankmCH.pdf | fig5/03 | 63 |
| Fig 5H | (Homer dot-plot, **savefig commented**) | fig5/08 | 53 |
| Fig 5I | (violin, **never saved**) | fig5/07 | 26 |
| Fig S26A | mCG_comp_{mode}_corr_example_scatter.pdf | fig5/01 | 28 |
| Fig S26B | mCH_comp_{mode}_corr_example_scatter.pdf | fig5/01 | 52 |
| Fig S26C | comp_boundary_flankmCG_{ct}.pdf | fig5/03 | 40 |
| Fig S26D | comp_boundary_flankmCH_{ct}.pdf | fig5/03 | 67 |
| Fig S27A | loop_summit_subtypedmr_enrich.pdf | fig5/05 | 13 |

**Strip (NONE):** fig5/02 c10(dup),13,36 · fig5/07 c10,13 · fig5/08 c41 (rejected pycisTarget version).
**Fix:** re-enable the commented savefig for Fig 5H (fig5/08 c53) and add a save for Fig 5I (fig5/07 c26).
**Gaps produced elsewhere:** S27B, S28, S29.

## Fig 6

| panel | output_pdf | notebook | cell |
|---|---|---|---|
| Fig 6B+6C | mC_3C_embed_group_mCG_new.pdf | fig6/02 | 48 |
| Fig 6E | Mus-Skl_fastslow_browser_{gtmp}{,_mczoomin}_{version}.pdf | fig6/06 | 64,67 |
| Fig 6F | {ct}_mc3c_DMR_loop_7group_{version}_fdr_cgkmeans_heatmap.pdf | fig6/06 | 48 |
| Fig 6H | {ct}_modality_tsne.pdf (Epi-TPB) | fig6/07 | 16 |
| Fig 6K | Epi-TPB_DMR_3state_stackedbar.pdf | fig6/07 | 32 |
| Fig S32A | ..._7group_{version}_fdr_cgkmeans_heatmap_percluster.pdf | fig6/06 | 49 |
| Fig S32B | {group_name}_modality_tsne.pdf | fig6/09 | 54 |
| Fig S32C | {group_name}_modality_pc_cluster_confusion.pdf | fig6/09 | 60 |

**Strip (NONE):** fig6/02 c47 · fig6/06 c22,32,37,45,46,72,73,75 (non-published 7group variants) · fig6/07 c17,28 · fig6/09 c105,107.
**Gaps produced elsewhere:** Fig 6A (ARI), 6D (donor confusion, correct counts), 6G (motif), 6I, 6J, S32D–H.
Note: S30/S31 = per-major-type subtype-embedding grids supporting **Fig 1F** (not Fig 6).

---

## Open questions for confirmation
1. **fig6/08 (Epi-Gas):** its tSNEs aren't in the figure, but S32G/H (Epi-Gas DMR/loop heatmaps) exist as a gap — keep as prerequisite or drop?
2. **Fig S24B** (fig4/01 c46/c50): notebook plots 4 columns; published S24B shows 5 (adds a "Strength" column) — version drift.
3. **Gap panels with no notebook source** (need a source or a note in `gaps.md`): 2O, 3I, 5H*/5I* (*inline-only), 6A, 6D, 6G, 6I, 6J, S13E, S16A/B, S23B, S27B, S28, S29(fig5-side), S32D–H.
