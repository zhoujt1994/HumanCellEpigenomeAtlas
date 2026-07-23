# Coverage & gaps

Every published panel that is **not fully reproducible from a released notebook as-is**.
Derived from [`PANEL_MAP.md`](PANEL_MAP.md) (all 230 savefig outputs matched to panels by
reading the figure PDFs + legends + rendered plots). Everything not listed here maps to a
notebook cell in its figure chapter.

## A. Hand-made — no producing code

| Panel | Status |
|-------|--------|
| Fig 1A | Tissue schematic + cell counts — drawn in Illustrator (the color/count key is emitted by `fig1/01` c43). |

Skip it.

## B. Published, compute present, but the **plotting cell is missing** from the release

The analysis runs and the panel is published, but the cell that *draws* it is not in these
notebooks — the highest-value category to recover.

| Panel | Notebook (compute) | Missing |
|-------|--------------------|---------|
| Fig 2O / Fig S13E | `fig2/06.DMR_motif` | TF-motif NES heatmap / dot plot; SCENIC+ NES tables (Table S2) are written, the heatmap cell is not in the release. |

Skip for now.

| Fig 6A | elsewhere (`clustering/merged/L2_hiconly/summary`) | mC-vs-3C ARI barplot; ARI computed, barplot cell not in the fig notebooks. |

You should resolve that now?

| Fig 6D | `fig6/01.MusSkl_clustering` | Donor-corrected 3×3 confusion matrix; nb01's table has the **pre-donor** counts, the published version is generated elsewhere. |

You can just sum up the per donor counts.

| Fig 6G | elsewhere | Loop-DMR motif dot plot (NES/#hits). |

Skip for now.

| Fig 6I | `fig6/07.Epi-TPB` (c28 related) | Subtype-DMR mCG + DEG heatmap (3,774 DMR); nb07 c28 is a related but different (3534/96686-DMR) heatmap. |
| Fig 6J | elsewhere | Flanking-mCG line plots. |

Those are in PMD analysis. Search the analysis directory further.

| Fig S32D–H | elsewhere | Schwann DMR/loop heatmaps; enteric/gastric DMR·loop·DEG heatmaps (`fig6/08.Epi-Gas`, dropped, only made t-SNEs). |



## C. Computed but plotted **inline only** — add a `savefig` to regenerate

| Panel | Notebook | Note |
|-------|----------|------|
| Fig S16A/B | `fig3/03.mC_context_lambda` | mCH-vs-Lambda fold-change / z-scored mCH clustermaps shown inline. |
| Fig 3I / Fig S23B | not in `fig3/` | mCH↔DEG-expression correlation (violins + corr-vs-distance-to-TSS); no producing cell in the fig3 notebooks. |
| Fig S3A/B | `fig4/09.loop_rna` (breast only) | DEG↔loop / DEG↔mCG-at-DMR cosine across colon/stomach/skin/heart; multi-tissue producer not in the release. |

**Recovered in this build** (were inline/commented, now saved): **Fig 5H** (`fig5/08` c53,
Homer loop-DMR dot plot — `savefig` re-enabled) and **Fig 5I** (`fig5/07` c26,
DMR↔diff-loop correlation violin — `savefig` added).

## D. Version drift / confirm

| Panel | Notebook | Note |
|-------|----------|------|
| Fig S24B | `fig4/01` c46/c50 | Notebook plots 4 columns; published S24B shows 5 (adds a "Strength" column). |
| Fig 6E | `fig6/06` c64/c67 | MYH7 fast/slow browser is byte-identical across nb04/05/06; attributed to nb06 (the published-companion notebook). |
| Fig S4 / S6 | elsewhere | S4 = per-tissue ATAC+snm3C joint embedding; S6 = subtype-donor mCG/loop correlation + violins. No source in the fig notebooks. |

## Notes on panels that are **covered** (avoid the old README mis-attributions)
- **Fig S2E** = `fig1/04` c23 (not a gap); **Fig 1F** dendrogram = `fig1/07` c22.
- **Fig 2 S9A/B** = `fig2/02` (not the 08/09 calling pipelines); **S10D/E** = `fig2/02`, **S10A–C** = `fig2/10`.
- **Fig 3C/S19** = `fig3/05`; **S17/S18** = `fig3/02`; **3D/3E** = `fig3/09`; **S21** = `fig3/04`.
- **S29A/B** = `fig2/18`; **S27A** = `fig5/05`; **S30/S31** support **Fig 1F**, not Fig 6.
- Produced elsewhere in the analysis tree (not the released fig notebooks): **S27B, S28**.
