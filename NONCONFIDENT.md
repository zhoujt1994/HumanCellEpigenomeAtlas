# Not-confidently-reproducible notebooks — to discuss

The book **displays** every panel it can (saved outputs). This page lists notebooks whose
**fresh re-run** still stops before completing, split into (A) genuinely-missing data /
external paths that need your input, and (B) deeper code issues where the first blocker was
fixed but a later one remains. For each, the panels *before* the blocker still render; a
panel *after* it is blank until resolved.

## A. Missing data / external path — needs author input

| Notebook | Blocker | Panel impact |
|----------|---------|--------------|
| `fig1/04.method_anchor` | `obsm['wnn_pc45_tsne']` absent — the WNN joint embedding was never saved | Fig S2C/D/E render (earlier cells); the WNN-vs-Concat QC after it does not |
| `fig1/08.L2both_per_celltype` | `FileNotFoundError` opening a per-celltype `L2/{ct}/…embed.h5ad` | **Fig S5 blank** (per-tissue subtype tSNE) |
| `fig4/01.decay` | Fig 4A/4B reproduce cleanly. **Fig S24B removed** — its code was entangled leftover (CEMBA cell types + a non-existent `saddle_*_mergerawpca.npy`); needs proper wiring to the compartment saddle-strength output. Not wtian-related. | 4A/4B render; S24B dropped |
| `fig4/06.domainloop_stats` (c11) | `FileNotFoundError` on a domain/loop `.h5ad` | some of Fig 4D/S25 render; the rest blank |
| `fig5/07.L2any_L2both` (c21) | `FileNotFoundError` on an `.h5ad` | **Fig 5I** (the violin, after c21) blank |
| `fig5/08.pycistarget_loopDMR` (c15) | missing `loop_peak_motif/majortype_merged_loop_TF_all.hdf` | **Fig 5H** (Homer dot-plot) blank |

## B. Deeper code issue — first blocker fixed, later one remains

| Notebook | Remaining error | Note |
|----------|-----------------|------|
| `fig2/07.TE_mCG` (c18) | `chrom/start/end` bed-header (second one) | Fig 2P/S15 render; a later repeat-mask read fails |
| `fig2/13.PMD_histone` (c49) | `AttributeError: 'list' object …` | Fig S11G/H (svg) render; a later cell fails |
| `fig3/04.mCH_mCG_corr` (c39) | `IndexingError: Unalignable boolean Series` | Fig S21A/B render; a later filter misaligns |
| `fig5/01.genome_mCG_compartment` (c57) | `NameError` (out-of-order, deeper) | Fig 5A/5B/S26A/B render; a later cell fails |
| `fig6/06.MusSkl_diff_7group` (c25) | `NameError: 'leg'` (the reorder didn't fully cover it) | Fig 6E/6F/S32A render; a later variant fails |
| `fig6/09.NTbSchw_clustering` (c11) | `chrom/start/end` bed-header | Fig S32B/C render; a later cell fails |

## S32D (Fig 6) — already agreed skip
Producing code **and** input data both absent (no Schwann DMR/loop calls in the tree); would
need a from-scratch pipeline run or a coauthor's copy.

---
_Everything not listed here re-runs clean or renders all its panels. Category-A items need
you to point at the missing file / regenerate the intermediate; Category-B are fixable with
more time but were deprioritized._
