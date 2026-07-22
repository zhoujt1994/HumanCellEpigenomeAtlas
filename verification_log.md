# Verification log

Records of code actually **run** against the shared data and checked against the paper.
This confirms the mapping is correct where a ✅ appears. Full execution of all 71
notebooks is a larger effort still in progress (many need the mapping confirmations in
[`REVIEW_NEEDED.md`](REVIEW_NEEDED.md) first, and heavy compute across two environments).

## ✅ Confirmed against the paper

### Atlas headline numbers — `clustering/merged/5kCG100k3C_summary.h5ad`
Run in the `allcools` env (see [`fig2/00.demo_fig2A.ipynb`](fig2/00.demo_fig2A.ipynb),
which is executed with saved outputs in the book):

| Quantity | Code | Paper | |
|----------|------|-------|--|
| Single nuclei | **86,689** | 86,689 | ✅ exact |
| Major types (`L1_annot`) | **35** | 35 | ✅ exact |
| Tissues (`Tissue`) | **16** | 16 | ✅ exact |
| Per-tissue counts | all 16 exact | Fig. 1 labels | ✅ (4 tissue labels are aliases: Esophagus=Esophagus Muscularis Mucosa, Skeletal Muscle=Gastrocnemius Medialis, Skin=Suprapubic Skin, Small Intestine=Ileum Peyer's Patch) |

Per-tissue counts (code = paper): Adrenal 5690, Breast 5299, Esophagus 5949, Lung 5124,
Pancreatic Islet 4700, Peripheral Blood 5780, Placenta 5731, Motor Cortex 8225,
Skeletal Muscle 5569, Skin 4353, Small Intestine 3067, Stomach 5982, Tibial Nerve 4860,
Transverse Colon 5836, Left Ventricle 5697, Right Atrium 4827. **Σ = 86,689.**

### Fig. 2A — global mCG per major type
Reproduced from `mCGFrac` grouped by `L1_annot`, ordered by median mCG. Ordering matches
the published panel biologically:
- **lowest** mCG: Epi TPB (trophoblast), Hema B, Epi Aci — PMD-rich / low-mCG lineages ✅
- **highest** mCG: Neu Inh, Neu Exc (neurons), Hema Tnaive/NK ✅
- median mCG range 0.588–0.813.

Rendered inline in the demo notebook; visually consistent with `figures/fig2.png` panel A.

## ⏳ Not yet run / verified (why)

- The other 70 notebooks read large single-cell allc / cool data and, in several cases,
  pipeline intermediates that live in `analysis/` subtrees (e.g. `ldsc/result/`,
  `PMD/10kb/`, `diff_loop/`). Executing them end-to-end is a multi-hour, two-environment
  job; several also depend on the panel attributions I flagged in `REVIEW_NEEDED.md`.
- **Recommended order:** (1) you confirm the `REVIEW_NEEDED.md` items; (2) I run the
  confident, self-contained figure notebooks first (metadata- and table-driven panels),
  verifying each against the published figure/number; (3) then the heavier pipeline
  notebooks, or small demos where the full input is impractical.

## How each panel will be verified

For a numeric panel: recompute the statistic and match the paper's reported value.
For a plot panel: render it and compare to the corresponding `figures/figN.png` reference
(ordering, cluster structure, sign of correlations, marker positions).
