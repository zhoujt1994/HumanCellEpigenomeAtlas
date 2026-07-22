# Fig. 1 — Single-cell atlas of DNA methylation and 3D genome structure

Fig. 1 introduces the atlas: 86,689 single nuclei from 16 human tissues profiled by
snm3C-seq, jointly clustered on 5-kb mCG (LSI) and 100-kb chromatin-contact (PCA)
features into 35 major types and 206 subtypes, with the major-type dendrogram.

![Fig. 1](../figures/fig1.png)

## Panel → code map

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| 1A | — | — | 16-tissue schematic + per-tissue cell counts (**Illustrator; no code**) |
| 1B | — | — | snm3C-seq assay workflow diagram (**Illustrator; no code**) |
| 1C | [01.clustering_summary](01.clustering_summary.ipynb) | c9, c14 | Browser shot of mCG + chromatin contacts in Hema Myeloid / Hema Tmem pseudobulk → `browser_example.pdf` |
| 1D | [01](01.clustering_summary.ipynb) | c34, c35 | Whole-atlas t-SNE of all 86,689 cells using mCG (left) vs contacts (right), by major type |
| 1E | [01](01.clustering_summary.ipynb) | c39 (+c40 legend) | Proportion of cells per tissue for the 35 major types (stacked bar) → `L1_tissueratio.pdf` |
| 1F | [07.dendrogram_annot](07.dendrogram_annot.ipynb) | c19 (major types), c20 (subtypes) | Dendrogram of major cell types (top) and subtypes (bottom) |

### Associated Extended Data figures

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| S1A | [02.m3c_blacklist](02.m3c_blacklist.ipynb) | c5, c8, c10 | Contact maps snm3C vs snmC-seq3 across types/donors/mapping; blacklist example |
| S1B | [02](02.m3c_blacklist.ipynb) | (decay) | Contact-decay curves (log10 %Reads vs distance) across the S1A datasets ✅ verified |
| S2A–B | [03.method_clustering](03.method_clustering.ipynb) | c36 | Mouse-brain (A) & PBMC (B): 5kb-mCG LSI vs 100kb-mCG PCA t-SNE |
| S2C–D | [04.method_anchor](04.method_anchor.ipynb) | c5, c20 | Esophagus (C) / colon (D) t-SNE under anchor-filter batch-correction variants |
| S2E | [05.modality_contribution](05.modality_contribution.ipynb) | c10, c14 | Per-major-type mCG vs 3C vs joint clustering consistency (**inline; not saved**) |
| S2 (validation) | [06.downsample_clustering](06.downsample_clustering.ipynb) | c18, c19 | Clustering precision & AUROC vs cells per group |
| S5 | [01](01.clustering_summary.ipynb) / [08](08.L2both_per_celltype.ipynb) | 01:c53 / 08:c21 | Per-tissue joint-embedding t-SNE by subtype (08 = final-annotation version) |
| S6A–C ⚠ | [09.pairwise_prediction](09.pairwise_prediction.ipynb)? | — | Subtype-donor mCG (A) & loop-strength (B) correlation heatmaps + donor/subtype/majortype violins (C). **Attribution unconfirmed** (see REVIEW_NEEDED) |
| S7A–B | [10.compare_bulkmc](10.compare_bulkmc.ipynb) | c39 (Loyfer), c69 (Schultz) | mCG correlation of subtypes vs prior WGBS studies |
| S8 | [11.compare_bulkhic](11.compare_bulkhic.ipynb) | c32, c33 | Loop-strength correlation of subtypes vs ENCODE Hi-C |
| S30 | [01](01.clustering_summary.ipynb) | c57 | Per-major-type t-SNE using **mCG** by subtype → `L1_celltype_mCG.pdf` |
| S31 | [01](01.clustering_summary.ipynb) | c58 | Per-major-type t-SNE using **contacts** by subtype → `L1_celltype_HiC.pdf` |

## Notebooks in this chapter

`01`–`08` and `10`–`11` use the **`allcools`** env; `11`/`12` and the contact browser in
`01` touch cooler (**`hic`** env). Types: *figure* = mostly panels; *pipeline* = mostly
computes shared intermediates; *mixed* = both.

- **01.clustering_summary** *(mixed)* — master atlas object + Fig 1B–F, S5, S30, S31.
- **02.m3c_blacklist** *(figure)* — contact-map QC, S1.
- **03.method_clustering** *(mixed)* — 5kb-LSI vs 100kb-PCA benchmark, S2A–B.
- **04.method_anchor** *(figure)* — anchor-filter batch correction, S2C–D.
- **05.modality_contribution** *(figure)* — modality-consistency matrices, S2E.
- **06.downsample_clustering** *(mixed)* — downsampling validation, S2.
- **07.dendrogram_annot** *(mixed)* — major-type dendrogram, Fig 1F.
- **08.L2both_per_celltype** *(mixed)* — final joint (“L2-both”) subtype labels, S5.
- **09.pairwise_prediction** *(pipeline)* — **the cluster-merge engine**; makes
  `cluster_meta.tsv`, `group_meta.tsv`, allc/cool merge lists, S6.
- **10.compare_bulkmc** *(mixed)* — vs Loyfer 2023 / Schultz 2015 WGBS, S7.
- **11.compare_bulkhic** *(figure)* — vs ENCODE Hi-C loops, S8.
- **12.L2any_L2both_diffloop** *(pipeline)* — differential-loop calling feeding Fig. 5
  (no panel).

```{admonition} Run order & overwrite cautions
:class: warning
- **Run `09.pairwise_prediction` first** — it generates `cluster_meta.tsv`,
  `group_meta.tsv` and the allc/cool merge lists consumed by 07, 08, 10, 11, 12 and
  downstream chapters.
- Notebooks **01, 08, 09** write back into the shared tree
  (`clustering/merged/5kCG100k3C_summary.h5ad`, `L1color.tsv`, `cluster_meta.tsv`,
  `group_meta.tsv`, `L2final_celltype_L2both*.tsv`, merge-list CSVs). With `repro_guard`
  on (the default) these writes are **skipped because the files already exist**, so the
  shared data is safe.
```

```{admonition} Gaps & corrections
:class: note
- **Fig 1A** (tissue schematic) and **Fig 1B** (assay workflow diagram) are hand-drawn in
  Illustrator — no producing code. (Confirmed from the full legend: 1B is the workflow, 1C
  is the browser shot.)
- **Fig S4** (per-tissue ATAC + snm3C **joint-embedding** t-SNE) is a Seurat-integration
  analysis and is **not** produced by `fig1/01` or `fig2/05` (which does DMR–peak *overlap*,
  a different thing). Its producer is **not located in `code_share`** — flagged in
  `REVIEW_NEEDED.md`. (The old README's "Fig 1/01 → S4" is wrong regardless.)
```

**Merge suggestion (not applied):** `01+07+08` (shared summary object) form a natural
“atlas overview” chapter; `03+04+05+06` form a “methods benchmark (S2)” chapter;
`10+11` a “comparison with prior studies (S7–S8)” chapter. Kept separate here to
preserve the original cleaned notebooks.
