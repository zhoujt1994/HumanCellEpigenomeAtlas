# Coverage & gaps

This page consolidates every panel that is **not fully reproducible from a released
notebook as-is**, so you know where code is missing, only computes data (no plot), or is
hand-made. Everything not listed here maps to a notebook cell in its figure chapter.

## A. Panels with no producing code (hand-made)

| Panel | Status |
|-------|--------|
| Fig 1A | Tissue schematic + cell counts — drawn in Illustrator. |

## B. Panel IS in the paper, but its plotting cell is not in `code_share`

The analysis/compute is present (tables written), and the panel is published — but the cell
that *draws* it isn't in the released notebooks. **The most important category to recover.**

| Panel | Notebook (compute) | What's published / what's missing here |
|-------|--------------------|------------------------------|
| Fig 2O | fig2/06.DMR_motif | Published motif-NES heatmap; SCENIC+ NES tables (Table S2) exist, **heatmap cell not in code_share**. |
| Fig S13E | fig2/06.DMR_motif | Same as 2O (peak vs non-peak DMR motif heatmap). |
| Fig 5H | fig5/06.loop_dmr_motif | Published loop-DMR motif enrichment; cisTarget/SCENIC+ run, **plot cell not in code_share**. |
| Fig 6A | fig5/07.L2any_L2both | Published ARI barplot (per major type); ARI values computed (c18–c19), **barplot cell not located**. |
| Fig 6G | fig6/06.MusSkl_diff_7group | Published motif **dot plot** (NES/‌#hits); cisTarget compute present, **dot-plot cell not pinned**. |

## C. Computed but plotted inline only (no `savefig` — add one to regenerate)

| Panel | Notebook | Note |
|-------|----------|------|
| Fig S2E | fig1/05.modality_contribution | consistency matrices shown inline. |
| Fig S16A/B | fig3/03.mC_context_lambda | context clustermaps inline. |
| Fig S23B | fig3/10 or fig3/02 | mCH↔DEG-expression correlation; exact source unconfirmed. |
| Fig S3A | fig4/09.loop_rna | DEG vs diff-loop cosine clustermap. |
| Fig S24B | fig4/03.decay_domain | domain-boundary contact frequency. |
| Fig S27B | fig5/05.loop_dmr_enrichment | diff-loop odds ratios by quantile. |
| Fig S28A/B | fig5/07.L2any_L2both | **published scatter grids** (3C/mC/Joint cluster correlations); computed in fig5/07 — confirm the savefig is present. |

## D. Not located in `code_share` — likely elsewhere in the analysis tree

You (the author) will know whether these exist; candidates live under
`/large_storage/zhoulab/zhoujt/project/ENTEx/analysis/` (the messy originals) or
`/large_storage/zhoulab/zhoujt/project/ENTEx/`.

| Panel | Note |
|-------|------|
| Fig S3A/B | DEG↔loop (A) and DEG↔mCG-at-DMR (B) cosine, across **colon/stomach/skin/heart** subtypes; `fig4/09` only does the breast analog. Multi-tissue producer not in code_share. |
| Fig S4 | Per-tissue **ATAC + snm3C joint-embedding** t-SNE (Seurat integration). Not `fig2/05`. Producer not in code_share. |
| Fig S6A/B/C | Subtype-donor mCG/loop correlation heatmaps + donor/subtype/majortype violins. `fig1/09` attribution unconfirmed. |
| Fig S32E–H | **Enteric (Epi-Ent)** & **Gastric (Epi-Gas)** DMR·loop·DEG heatmaps. `08.Epi-Gas` only makes t-SNEs; producer not in code_share. |
| Fig 6A barplot | ARI values in `fig5/07`; the bar chart render itself not located. |
| Fig 2O / S13E / 5H / 6G dot plots | Published motif dot plots (NES/‌#hits); SCENIC+ compute present, dot-plot render not in code_share. |

## E. README mapping corrections (this book vs the original `code_share/README.md`)

| Original claim | Correction |
|----------------|------------|
| Fig 1/01 → S4 | `01` has no ATAC code; **S4 is Fig 2 / 05.DMR_overlap_ATAC**. |
| Fig 2 S9 → nb08/09 | S9A/B are in **fig2/02.PMD_hetero** (c48, c20); 08/09 are calling/validation pipelines. |
| Fig 2 S10 → nb11/12 | S10D/E are in **fig2/02** (c64, c62); S10A–C in **fig2/10.PMD_donor**. |
| Fig 3 3C/S17–S18 → nb04 | **3C/S19 = fig3/05**; **S17–S18 = fig3/02**; **nb04 = S21**. |
| Fig 3 3D–E → nb02 | **3D–E = fig3/09.mCH_geneflank** (nb02 feature heatmaps are inline-only). |
| Fig 3 S21 → nb06 | **S21 = fig3/04**; nb06 (`mCH_mCG_comp`) has no matching S-figure. |

## F. Legend-text caveats

The extracted manuscript legends are truncated for **Fig. 1 (after A)**, **Fig. 3 (after
E)**, **Fig. 4 (after F)**, **Fig. 6 (after E)**, and **Fig. S32 (after A)**, plus finer
letters of **S12/S14**. Panel-letter assignments in those ranges are inferred from
notebook content and the README, and are marked ⚠ in the chapters. The *content* is
present in code; only the exact letter↔cell binding is unverified.

---

```{admonition} What to do with this list
:class: tip
Category **B** (missing plot cells) is the highest-value to fix before release — the
analysis already ran, only the final `savefig` is gone. Category **C** just needs a
`savefig(...)` added. Category **D** needs the author to point at the original notebook.
```
