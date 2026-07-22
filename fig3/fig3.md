# Fig. 3 — Non-CG methylation across cell types

Fig. 3 characterizes mCH: global levels (neuronal vs non-neuronal), trinucleotide
context, spatial scale of methylation signatures, gene-body mCH vs expression, and mCH
subtype structure.

![Fig. 3](../figures/fig3.png)

## Panel → code map

```{admonition} Legend now resolved
:class: note
Verified against the full manuscript legend. Panels F–I were corrected: **3F = `fig3/06`**
(mCH around mCG compartments), not the heterogeneity notebook; **3D/3E = `fig3/09`**;
**3G/3H = `fig3/07`**. See `REVIEW_NEEDED.md` for the remaining cell-pinning question on 3I.
```

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| 3A | [02.mCH_distribution](02.mCH_distribution.ipynb) | c15–c17 | Average mCH per major type, split to show neuronal (far right) vs non-neuronal |
| 3A (aux) | [01.global_mCH](01.global_mCH.ipynb) | c12 | Per-celltype mCH vs lambda-phage mCH (broken-axis) |
| 3B | [03.mC_context_lambda](03.mC_context_lambda.ipynb) | c23 | Average mCH by trinucleotide context, neurons excluded |
| 3C | [05.mCH_mCG_scale](05.mCH_mCG_scale.ipynb) | c24 | Methylation correlation vs genomic distance, type × context |
| 3D | [09.mCH_geneflank](09.mCH_geneflank.ipynb) | c86, c87 | Z-scored mCH at different genomic features per major type |
| 3E | [09](09.mCH_geneflank.ipynb) | c50, c53 (+c47 cCRE) | Z-scored mCH surrounding elements (5 plots incl. cell-type cCREs) |
| 3F | [06.mCH_mCG_comp](06.mCH_mCG_comp.ipynb) | c20 | mCH surrounding mCG compartments >100 kb → `CGcomp_flankCH.pdf` |
| 3G | [07.mCH_clustering](07.mCH_clustering.ipynb) | c33, c34 | t-SNE of all cells using mCH, by major type (center) / global mCH / tissue → `All_100kCH_meta.pdf` |
| 3H | [07](07.mCH_clustering.ipynb) | c46 (subset) | mCH t-SNE of Epi Endocri & Mus Skl by subtype (cropped from the per-type panel, `L1_mCH_seurat_tsne_celltype.pdf`) |
| 3I ⚠ | (mCH↔DEG corr) | — | mCH vs DEG-expression correlation violins in Epi Endcri — **same analysis as S23B; exact cell not pinned (see REVIEW_NEEDED)** |

### Associated Extended Data figures

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| S16A | [03](03.mC_context_lambda.ipynb) | c18 | log2 FC genomic vs lambda mCH by context (**inline; not saved**) |
| S16B | [03](03.mC_context_lambda.ipynb) | c25 | mCH by base context, row Z-scored (**inline**) |
| S17A | [02](02.mCH_distribution.ipynb) | c77 | 50kb pairwise-context correlation, grouped |
| S17B | [02](02.mCH_distribution.ipynb) | c78 | Context correlation across bin sizes |
| S18 | [02](02.mCH_distribution.ipynb) | c88 | 16-context correlation, 6 groups × 7 resolutions |
| S19A | [05](05.mCH_mCG_scale.ipynb) | c24 | Distance-correlation heatmap, type × context |
| S19B | [05](05.mCH_mCG_scale.ipynb) | c25 | Distance-correlation line plots |
| S20 | [02](02.mCH_distribution.ipynb) | c85 | DNMT/writer/eraser/reader expression by major-type group |
| S21A | [04.mCH_mCG_corr](04.mCH_mCG_corr.ipynb) | c37, c38 | log2 FC of genome-annotation proportions, high vs low mCA |
| S21B | [04](04.mCH_mCG_corr.ipynb) | c46, c47 | HOMER motif enrichment p-values, high vs low mCA |
| S22 | [07](07.mCH_clustering.ipynb) | c44 | Per-major-type mCH t-SNE by subtype |
| S23A | [07](07.mCH_clustering.ipynb) | c37 | Pairwise-major-type AUROC/AUPR on 100kb mCH |
| S23B | [09.mCH_geneflank](09.mCH_geneflank.ipynb)? | — | mCH↔DEG-expression correlation vs distance-to-TSS, 6 major types (**same analysis as Fig 3I**; 3I = the Epi Endcri panel). Likely `fig3/09`; cell to pin |

## Notebooks in this chapter

All **`allcools`** env. mCH matrices are read from single-cell CHN ALLC files via tabix.

```{admonition} Gaps & corrections
:class: note
- **README corrections for Fig. 3:** `3C`/S19 come from **`05`** (not `04`); S17–S18 from
  **`02`**; `3D`–`3E` from **`09`** (not `02`, whose feature heatmaps are inline-only);
  **`04`** produces **S21** (high/low-mCA), not S17–18.
- **`06.mCH_mCG_comp` = Fig 3F** (mCH around mCG compartments >100 kb, `CGcomp_flankCH.pdf`) —
  confirmed from the full legend; it is a main-figure panel, not an orphan.
- **`08.mCH_hetero`** (within-type mCH heterogeneity) has **no clear main/ED panel** in the
  legend — likely methods/supporting. Flagged in `REVIEW_NEEDED.md`.
- **Fig 3I / S23B** (mCH↔DEG-expression correlation violins) — the analysis is described in
  the legend but I could not pin a `savefig`; candidate producers `02`/`09`/`10`. Flagged.
- **S16A/B** clustermaps render inline with **no savefig** in the shared code.
- **S23B** exact source unconfirmed (closest: `10`, or `02` c19–c26).
- **⚠ Overwrite hazard:** `08.mCH_hetero` writes to shared `mCG_distribution/*` and
  `PMD/10kb/*` paths **identical to Fig. 2 / 02.PMD_hetero** — with `repro_guard` on those
  writes are skipped, but run order matters if you regenerate.
- Source-tree writes (guarded): `03` → `merged_allc/L2any_mCGnorm.hdf`; `09` →
  `scATAC/cCREs_selct.bed.gz`; `10` → `clustering/merged/5kCG100k3C_subtype_tissue.csv.gz`.
```

**Merge suggestion (not applied):** `09+10` (gene-centric mCH); `04+05+06` (share the
allc→matrix extraction layer); `02+03` (trinucleotide context); `07+08` (100kb-mCH
embedding). `01` (global-vs-lambda QC) stays standalone.
