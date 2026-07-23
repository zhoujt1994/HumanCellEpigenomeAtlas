# Fig. 5 — Comparison of DNA methylation and 3D genome structure

Fig. 5 relates the two epigenomic layers: genome-wide correlation of chromatin
compartments with mCG/mCH, methylation vs compartment/domain boundaries, and DMR
enrichment at chromatin loops.

![Fig. 5](../figures/fig5.png)

## Panel → code map

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| 5A | [01.genome_mCG_compartment](01.genome_mCG_compartment.ipynb) | c29 | Compartment score vs **mCG** correlation across major types |
| 5B | [01](01.genome_mCG_compartment.ipynb) | c53 | Compartment score vs **mCH** correlation across major types |
| 5C | [02.comp_pmd](02.comp_pmd.ipynb) | c28 | Whole-chr2 stack (Hema Tmem): contact-corr → comp score → per-CpG mCG → methylation compartment → 10kb mCG |
| 5D | [02](02.comp_pmd.ipynb) | c29 | Same stack zoomed to chr2:167–177M |
| 5E | [02](02.comp_pmd.ipynb) | c9 | Cross-cell-type heatmap: compartment score vs methylation compartment, k-means ordered |
| 5F | [03.mCoverCompboundary](03.mCoverCompboundary.ipynb) | c35 | Compartment-switch domain-boundary flank **mCG** (A>B / B>A / Other) |
| 5G | [03](03.mCoverCompboundary.ipynb) | c61 | Same flank **mCH** |
| 5H | [08.pycistarget_loopDMR](08.pycistarget_loopDMR.ipynb) | `TF_loopdmr_methyltype` | Motif **dot plot**: enrichment at loop vs non-loop DMRs per major type ✅ **recovered** (was missing from code_share) |
| 5I | [07.L2any_L2both](07.L2any_L2both.ipynb) | c7 (c10 diff-loop) | L2any-vs-L2both DMR heatmaps per group |

### Associated Extended Data figures

| Panel | Notebook | Cell(s) | What it makes |
|-------|----------|---------|---------------|
| S26A | [01](01.genome_mCG_compartment.ipynb) | c28 | Scatter mCG vs comp score, most ± correlated major types |
| S26B | [01](01.genome_mCG_compartment.ipynb) | c52 | Scatter mCH vs comp score |
| S26C | [03](03.mCoverCompboundary.ipynb) | c37 | Per-cell-type flank mCG heatmap, boundaries sorted by up−down mCG diff |
| S26D | [03](03.mCoverCompboundary.ipynb) | c63 | Per-cell-type flank mCH version |
| S27A | [05.loop_dmr_enrichment](05.loop_dmr_enrichment.ipynb) | c12 | log2 odds-ratio: DMR overlap at loop vs loop-summit anchors ✅ |
| S27B | [05](05.loop_dmr_enrichment.ipynb) | c10, c13 | DMR enrichment at loops by loop-strength percentile (10–100), per major type ✅ published (confirm savefig) |
| S28 | [07](07.L2any_L2both.ipynb) | c16–c34 | mCG-at-DMR vs diff-loop correlation by clustering method (**computed; no savefig — gap**) |

## Notebooks in this chapter

`01`–`04`, `07` use **`allcools`** (+ read compartment/loop hdf); `05` uses `bedtools`;
`06` uses **SCENIC+** (create_cisTarget_databases + motif enrichment). `03`/`04` build
5kb mCG/mCH along domain boundaries.

```{admonition} Run order & overwrite cautions
:class: warning
- **Shared-file collisions:** `03` and `04` both write
  `mCG_distribution/L1_chrom5k_mCG.hdf` / `..._mCH.hdf`; `01` and `04` both write
  `mCG_distribution/L1_global_mCG.tsv.gz`. Run one, or `repro_guard` skips the second.
- **`05` c1 writes into the shared *reference* tree**
  (`{REF_ROOT}/hg38/fasta/hg38.auto.anchor.bed`) — guarded when it exists.
- `04.mCoverDomainboundary` produces **no figure** (data-prep / exploratory duplicate of
  `03` over all boundaries + shuffle background).
```

```{admonition} Gaps & corrections
:class: note
- **Fig 5H** (`06.loop_dmr_motif`): only builds cisTarget DBs and runs SCENIC+ enrichment —
  the motif-enrichment **heatmap-rendering cell is missing** from the release.
- **Fig S27B** and **all of Fig S28** are computed in-notebook but have **no `savefig`**;
  only 5I (`07` c7/c10) and S27A (`05` c12) are written to PDF.
```

**Merge suggestion (not applied):** reconcile `03+04` (80% shared, and they collide on the
5kb HDFs — give the HDFs distinct names). A shared `mcds → binned-mCG` loader is copy-pasted
across `01/03/04`. `05` (bedtools enrichment) and `06` (SCENIC+ motif) stay separate.
