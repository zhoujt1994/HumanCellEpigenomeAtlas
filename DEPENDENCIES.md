# Cross-notebook data dependencies (structural / bootstrapping)

Most generators sit before their consumers (fixed where they didn't, e.g. `fig6/02.mc3c_ARI`
now follows `fig6/02` which writes the embed it reads). A few dependencies are **iterative /
cross-figure** and cannot be linearized without breaking the paper's figure order — they are
documented here so a reproducer knows to run the generator first:

- **`clustering/03.tissue_refine` ← `fig1/01.clustering_summary`** — the tissue-refine step reads
  `clustering/merged/5kCG100k3C_summary.h5ad`, which is the *final* clustering summary. This is the
  iterative-clustering bootstrap (annotations from the finished summary feed the refinement).
- **`fig4/09.diffcomp_majortype` ← `fig5/01.genome_mCG_compartment`** — reads
  `mCG_distribution/L1_chrom100k_mCG.hdf` / `L1_chrom100k_mCH.hdf` (per-major-type 100 kb mC),
  generated in the Fig 5 compartment notebook. A shared intermediate across Fig 4/Fig 5.
- **`fig6/01.MusSkl_donor_clustering` ← `fig6/03.MusSkl_diff_7group`** — reads
  `Mus-Skl/5kCG100k3C_embed.h5ad`; the MusSkl donor-vs-diff analysis is iterative (same bootstrap
  pattern as the main clustering).
