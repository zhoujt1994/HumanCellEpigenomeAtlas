# Human Body Single-Cell Atlas of 3D Genome Organization and DNA Methylation

This Jupyter Book documents the analysis code that reproduces every figure in
**"Human Body Single-Cell Atlas of 3D Genome Organization and DNA Methylation"**
(Zhou, Wu, Liu, et al.).

> **Abstract.** Higher-order chromatin structure and DNA methylation are critical
> for gene regulation, but how these vary across the human body remains unclear.
> We performed multi-omic profiling of 3D genome structure and DNA methylation for
> **86,689 single nuclei across 16 human tissues**, identifying **35 major and 206
> cell subtypes**. We revealed extensive changes in CG and non-CG methylation across
> almost all cell types and characterized 3D chromatin structure at an unprecedented
> cellular resolution. Extensive discrepancies exist between cell types delineated by
> DNA methylation and genome structure, indicating that the role of distinct
> epigenomic features in maintaining cell identity may vary by lineage.

## How this book is organized

Each chapter corresponds to one main figure of the paper (Fig. 1–6) and bundles the
associated Extended Data / Supplementary figures (Fig. S1–S32). Within a chapter you
will find:

- a short **overview** of the biology and the analysis;
- an embedded **reference image** of the published figure so you can see the target;
- a **panel → notebook → cell** table telling you exactly which notebook (and roughly
  which cells) produce each panel;
- the **notebooks themselves**, lightly edited so paths are configurable and so that
  re-running them can never overwrite your existing data (see below).

| Chapter | Main figure | Topic |
|---------|-------------|-------|
| [Fig. 1](fig1/fig1.md) | Single-cell atlas | Joint mCG + 3D-genome clustering, cell-type annotation, benchmarking |
| [Fig. 2](fig2/fig2.md) | CG methylation | PMDs / methylation compartments, DMRs, ATAC overlap, TF motifs |
| [Fig. 3](fig3/fig3.md) | Non-CG methylation | Global mCH, trinucleotide context, gene-body mCH, mCH subtypes |
| [Fig. 4](fig4/fig4.md) | Chromatin contacts | Contact decay, compartments, domains, differential loops |
| [Fig. 5](fig5/fig5.md) | mCG vs 3D genome | Compartment/methylation correlation, DMRs at loops |
| [Fig. 6](fig6/fig6.md) | Discrepant cell types | mCG- vs contact-defined subtypes across tissues |

## Before you start

Read these three chapters first — they explain the compute environment, where to get
the data, and how the reproduction safeguards work:

- **[Environment & build](setup.md)** — conda environments and how to build the book.
- **[Data availability](data.md)** — where every input dataset lives.
- **[Reproduction guide](reproduce.md)** — the path convention and the no-overwrite
  write guard that protects your files when you re-run a notebook.

```{admonition} Reproducibility, honestly
:class: note
These notebooks were **cleaned from the original working analysis**. Cells were
sometimes run out of order or selectively during the study, and a few panels were
finished in Illustrator. Where a panel has no producing code we say so explicitly in
the per-chapter gap notes. If a cleaned notebook looks wrong, the original (messier)
notebook it was derived from lives under
`/large_storage/zhoulab/zhoujt/project/ENTEx/analysis/` (see the mapping in each
chapter).
```
