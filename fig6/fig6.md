# Fig. 6 — Discrepant methylation- vs contact-defined cell types

Fig. 6 examines cases where clustering by DNA methylation disagrees with clustering by
chromatin contacts. It quantifies the agreement (ARI) per major type, then dissects
skeletal muscle (Mus Skl), trophoblast (Epi TPB), and several other tissues where the
two epigenomic layers define different cell states.

![Fig. 6](../figures/fig6.png)

## Panel → code map

```{admonition} Legend now resolved
:class: note
Verified against the full manuscript legend. Corrections vs my first pass: **6G = motif
enrichment** of loop-DMR-pair groups (Table S3), not a strength summary; **6H** = Epi-TPB
contact/mCG t-SNE by *subtype-donor* (VCT/SCT); **6I** = DMR mCG + DEG expression; **6J** =
DMR flanking mCG; **6K** = DMR compartment fractions. The 6G motif plot and 6I/6J exact
cells are still open — see `REVIEW_NEEDED.md`.
```

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| 6A | [Fig5/07.L2any_L2both](../fig5/07.L2any_L2both.ipynb) c21 (values) + barplot from `clustering/merged/L2_hiconly/summary.ipynb` c12 | — | ARI per major type barplot ✅ **located** (`ax.bar(x, score, color=L1_meta['color'])` → `mc_3c_L2_ARI.pdf`); to add to fig5/07 |
| 6B | [02.MusSkl_donor_clustering](02.MusSkl_donor_clustering.ipynb) | c49 | Mus Skl t-SNE mCG (left) & contact (right) — **donor-joint coordinates, colored by donor-separate cell-group labels** |
| 6C | [02](02.MusSkl_donor_clustering.ipynb) | c49 | Same (donor-joint) coordinates colored by global mCG |
| 6D | [01.MusSkl_clustering](01.MusSkl_clustering.ipynb) | c42 | Confusion matrix mC-subtypes × 3C-subtypes |
| 6E | [04](04.MusSkl_diff.ipynb) / [06](06.MusSkl_diff_7group.ipynb) | c53 (c55 zoom) | Contact + mCG browser at chr14 *MYH7* + zoomed DMR regions i/ii (see variant note) |
| 6F | [04](04.MusSkl_diff.ipynb) / [06](06.MusSkl_diff_7group.ipynb) | c32/c40 | Diff-loop strength (left, 18,646 loops) + mCG of DMRs at anchors (right, 19,647 DMRs), 7 groups, k-means |
| 6G | [Fig5/08.pycistarget_loopDMR](../fig5/08.pycistarget_loopDMR.ipynb) | `TF_overlapped_nes_mus_long` | Motif **dot plot** (NES/‌#hits) per Mus Skl loop-DMR group ✅ **recovered** |
| 6H | [07.Epi-TPB](07.Epi-TPB.ipynb) | c17 | Epi-TPB t-SNE contact (top) / mCG (bottom) by subtype-donor (VCT/SCT) |
| 6I | [07](07.Epi-TPB.ipynb) | c28 (+DEG expr) | mCG of DMRs between subtypes (left) + DEG expression (right) |
| 6J ⚠ | [07](07.Epi-TPB.ipynb) | — | mCG at flanking regions of subtype vs donor DMRs — flank cell not pinned |
| 6K | [07](07.Epi-TPB.ipynb) | c32 | Fraction of subtype- vs mCG-cluster DMRs per methylation compartment |

### Associated Extended Data figure (S32)

Per the full legend, S32 is: A (Mus Skl split), **B–D Schwann**, **E–H gastric (Epi-Gas)
& enteric (Epi-Ent)** DMR mCG / diff-loop / DEG. This reclassifies the mCT notebooks —
see the caution below.

Verified against the figure: A = Skeletal Muscle, B–D = Schwann, **E–F = Enteric**,
**G–H = Gastric** epithelial (each = DMR mCG + Loop Strength + DEG expression).

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| S32A | [04](04.MusSkl_diff.ipynb) / [06](06.MusSkl_diff_7group.ipynb) | c41 | Skeletal-muscle loop strength + DMR mCG (7-group columns) split into k-means groups |
| S32B | [09.NTbSchw_clustering](09.NTbSchw_clustering.ipynb) | c51 | Tibial-nerve Schwann t-SNE mCG / contact by cluster (black = inconsistent) ✅ |
| S32C | [09](09.NTbSchw_clustering.ipynb) | c57 | Correlation matrix of 5 Schwann clusters, mCG (top) / contact (bottom) ✅ |
| S32D ⚠ | [09](09.NTbSchw_clustering.ipynb) | — | Schwann DMR mCG (6460) + diff-loop strength (10845), k-means — cell not pinned |
| S32E–F ⚠ | **Enteric (Epi-Ent)** | — | Enteric DMR mCG + DEG (E), Loop Strength + DEG (F) — **producer NOT in code_share** (analogous to `07.Epi-TPB` + `fig4/09.loop_rna`) |
| S32G–H ⚠ | **Gastric (Epi-Gas)** | — | Gastric DMR mCG + DEG (G), Loop Strength + DEG (H) — `08.Epi-Gas` only makes t-SNEs; **DMR/loop/DEG producer NOT in code_share** |

```{admonition} mCT notebooks are NOT in the published paper
:class: warning
Per the author: **there is no mCT (methylation + transcriptome multiome) data shown in this
paper.** So `10.colon_mct`, `11.colon_mct_mc_donor`, `12.stomach_mct`, `13.stomach_mct_mc`,
`14.stomach_mct_mc_donor` **do not correspond to any published panel** — they are
exploratory analyses kept for completeness, not figure-reproduction notebooks. The true
producers of **S32E–H** (gastric Epi-Gas / enteric Epi-Ent DMR·loop·DEG) are elsewhere and
deferred for now (`REVIEW_NEEDED.md`).
```

## Notebooks in this chapter

Mixed **`allcools`** (mCG/DMR) and **`hic`** (contacts/loops). `03` is a pure
differential-loop-calling pipeline.

```{admonition} How the final Mus Skl panels are assembled (important)
:class: important
The published Fig 6B/C t-SNEs use the **donor-joint embedding coordinates** (from
`02.MusSkl_donor_clustering`) but are **colored/labeled by the donor-*separate* cluster
assignments** (the groups + colors defined per donor). In other words: coordinates come
from the joint run, cluster identity/colors come from the donor-separated run — the two are
overlaid. Keep this in mind when reconciling `01` (initial joint), `02` (donor-joint
coordinates, the final ones), and the group labels used to color them.
```

```{admonition} MusSkl_diff variants — which is the published one? (⚠ revised)
:class: warning
The published **Fig 6D** confusion matrix is 3×3 (mC-Stem/Fast/Slow × 3C-Stem/Fast/Slow),
and **Fig 6F/6G have 7 columns** — the populated mC/3C combinations `Fast/Fast, Slow/Fast,
Stem/Fast, Stem/Stem, Stem/Slow, Fast/Slow, Slow/Slow`. That means the figure uses **7
cell groups**, so **`06.MusSkl_diff_7group` produces the published Fig 6E–G + S32A** — CONFIRMED by the author:
the published heatmap is `Mus-Skl_mc3c_DMR_loop_7group_new_fdr_cgkmeans_heatmap.pdf` (18,646 loops /
19,647 DMRs).
`05.MusSkl_diff_3group` collapses to 3 groups (an alternate). **Please confirm 7-group is
the published version.**
```

```{admonition} Run order & overwrite cautions
:class: warning
- **⚠ `09.NTbSchw_clustering` ends with stale copy-pasted cells (c77–c93) that write to
  `Mus-Skl/...` products** (`5kCG100k3C_embed.h5ad`, `confusion_table.pdf`, etc.). With
  `repro_guard` on, these are skipped if the Mus-Skl files exist, but if you run `09`
  before `01`/`02` on a clean tree they would create wrong Mus-Skl files. **Recommend
  deleting those trailing cells.**
- Source-tree writes (guarded): `02` → `L2/Mus-Skl/5kCG.h5ad`; `11`/`13`/`14` →
  `clustering/tissue/L1/{tissue}/5kCG.h5ad`.
```

```{admonition} Gaps & corrections
:class: note
- **Fig 6A (ARI barplot):** the ARI values are computed in `Fig5/07.L2any_L2both` (c18–c19)
  but **no barplot/savefig cell was found** in any released notebook — the bar-rendering
  code appears to be missing.
- Fig 6 legend F–K and S32 sub-panel text are truncated; H–K / S32 tissue assignments are
  inferred from code.
```

**Merge suggestion (not applied):** `04/05/06` → one notebook parametrized by group count
(`n_group ∈ {3,7,8}`, default 8). `01`/`09` share a clustering scaffold — factor into a
`group_name`-parametrized function and delete `09`'s trailing Mus-Skl block (data-safety
fix). `10–14` share a per-tissue mCT skeleton — merge into a tissue-parametrized notebook.
`03`, `07`, `02` stay standalone.
