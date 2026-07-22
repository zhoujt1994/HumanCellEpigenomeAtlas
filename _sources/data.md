# Data availability

The notebooks read from a project tree rooted at `ENTEX_ROOT`
(`/large_storage/zhoulab/zhoujt/project/ENTEx` on the original machine). The table
below maps each **data type** used in the figures to where it is (or will be)
released. Exact download links / accessions are finalized at publication; this page
records the canonical source for each layer.

```{admonition} Placeholder links
:class: warning
Some destinations below are release targets (Zenodo record, Hugging Face datasets,
GEO). Where a concrete URL is not yet public, the *bucket / repository* is named so
you know which layer a file belongs to. Update this page with the final accessions
before the public release.
```

## Single-cell (per-nucleus) data

| Layer | Format | Location |
|-------|--------|----------|
| Single-cell **mCG** (CpG) | ALLC `*.tsv.gz` | `ENTEX_ROOT/allc/*.CGN-Both.tsv.gz` |
| Single-cell **mCH** (CHN) | ALLC `*.tsv.gz` | Hugging Face `zhoujt1994/HumanCellEpigenomeAtlas_sc_allc` |
| Single-cell **chromatin contacts** | contact tables / cool | Hugging Face `zhoujt1994/HumanCellEpigenomeAtlas_sc_contact` |

## Cell-subtype pseudobulk (206 subtypes)

| Layer | Format | Location |
|-------|--------|----------|
| Subtype **mCG** | ALLC | `gs://ecker-may-entex-analysis/merge_allc/CGN-strand-merged-subtype206-cov2/*.tsv.gz` |
| Subtype **mCH** | ALLC | `gs://ecker-may-entex-analysis/merge_allc/121624_subtype_l2both/*/*/*.tsv.gz` |
| Subtype **DMR (hypo)** | BED | `ENTEX_ROOT/DMR/majortype-subtype/hypo/*.bed` |
| Subtype **DMR data** | tar.gz (RegionDS) | `ENTEX_ROOT/DMR/majortype-subtype/*_dmr.tar.gz` |
| Subtype **contacts / loops** | cool / bedpe | file list provided with the release |

## Major-type pseudobulk (35 major types)

| Layer | Format | Location |
|-------|--------|----------|
| Major-type **mCG** | ALLC | `gs://ecker-may-entex-analysis/merge_allc/CGN-strand-merged-l1-cov2/*.tsv.gz` |
| Major-type **mCH** | ALLC | `gs://ecker-may-entex-analysis/merge_allc/112324_L1-cov2/c0/c0/*.tsv.gz` |
| Major-type **PMD / methylation compartment** | BED | `ENTEX_ROOT/analysis/PMD/L1/c*_3state.bed` |
| **Total DMR** (36-group merged) | BED | `ENTEX_ROOT/analysis/DMR/overlap_atac/majortype_36groups/*_merged.bed` |
| Major-type **cool** (imputed contacts) | cool | `gs://ecker-may-entex-analysis/loop/010725-majortype/.../*.cool` |
| Major-type **loops** | bedpe | `gs://ecker-may-entex-analysis/loop/010725-majortype/.../*.loop.bedpe` |
| Major-type **compartment score** | bedgraph | `ENTEX_ROOT/analysis/compartment/L1/*.impute.bedgraph` |

## Code & processed objects

- **Code archive (Zenodo):** DOI [10.5281/zenodo.19394035](https://doi.org/10.5281/zenodo.19394035)
- **Metadata tables** (cell/subtype/major-type annotations, colors) ship in the project
  root: `L1color.tsv`, `tissuecolor.tsv`, `subtype_meta.tsv`, `cluster_meta.tsv`,
  `group_meta.tsv`, `celltype_annot.tsv`, `npc.tsv`, and the joint embedding object
  `clustering/merged/5kCG100k3C_summary.h5ad` (+ `.csv.gz`).

## External / reference datasets used in comparisons

These are third-party datasets pulled in for benchmarking panels; obtain them from the
original sources:

| Used in | Dataset |
|---------|---------|
| Fig. S7 | Loyfer et al. 2023 (sorted-cell WGBS); Schultz et al. 2015 (Roadmap bulk WGBS) |
| Fig. S8 | ENCODE Hi-C cell types (loop strength) |
| Fig. 2N / S13–S14 | matched scATAC-seq peaks |
| Fig. S11 | histone modification tracks; bulk RNA-seq |
| Fig. 4F–G / S3 | Reed et al. 2024 breast scRNA-seq; tissue scRNA-seq references |
| Fig. S2A–B | CEMBA whole-mouse-brain snmC / PBMC references |
| Fig. S16 | lambda-phage spike-in controls (non-conversion) |

## Reference genome

hg38 (GENCODE v30 gene annotation:
`/large_storage/zhoulab/ref/hg38/gencode/v30/gencode.v30.annotation.gene.flat.tsv.gz`).
