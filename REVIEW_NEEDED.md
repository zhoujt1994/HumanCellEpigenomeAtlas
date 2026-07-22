# Needs your confirmation

Things I am **not confident about** in the figure→code mapping. Please annotate each
(✅ correct / ✏️ fix / ❓ code lives elsewhere). Grouped by how uncertain I am.

---

## 1. Panels you flagged as possibly missing code — what I actually found

You listed: `Fig 2O, Fig 5H, EDFig S1A/B, S3A/B, S4, S6A–C, S13E, S16A/B, S24A/B, S27A/B, S28A/B`.
Here is the status I found for each:

| Panel | My finding | Confirm? |
|-------|-----------|----------|
| **Fig 2O** | ❌ no plot cell — `fig2/06` runs SCENIC+ and writes NES tables (Table S2); heatmap render absent | missing |
| **Fig 5H** | ❌ no plot cell — `fig5/06` builds cisTarget DB + SCENIC+ enrichment; heatmap render absent | missing |
| **S1A** | ✅ found — `fig1/02` c5/c8/c10 (contact maps + blacklist example) | ? |
| **S1B** | ⚠️ decay curves — computed but I could not pin a `savefig`; may be inline or share `fig4/01` decay code | ? |
| **S3A** | ⚠️ `fig4/09` c41 (DEG vs diff-loop cosine) — **no savefig** (inline) | ? |
| **S3B** | ❌ DEG vs mCG-at-DMR — **not found in code_share** | need location |
| **S4** | ⚠️ I attributed to `fig2/05` (ATAC integration t-SNE) — **you flagged this; please verify it's really there or point me elsewhere** | verify |
| **S6A–C** | ⚠️ I attributed to `fig1/09` c13 (subtype-donor mCG/loop correlation) — you flagged; **please verify** | verify |
| **S13E** | ❌ same as 2O (peak vs non-peak motif heatmap) — no plot cell | missing |
| **S16A/B** | ⚠️ `fig3/03` c18/c25 — computed, **no savefig** (inline clustermaps) | ? |
| **S24A** | ✅ `fig4/02` c19/c21 (per-type contact by compartment diff/sum) | ? |
| **S24B** | ⚠️ `fig4/03` c14/c19 (domain-boundary contact freq) — **no savefig** | ? |
| **S27A** | ✅ `fig5/05` c12 (DMR-at-anchor odds ratio) — saved | ? |
| **S27B** | ⚠️ `fig5/05` c10/c13 — computed, **no savefig** | ? |
| **S28A/B** | ⚠️ `fig5/07` c16–c34 — computed, **no savefig** (only 5I is saved) | ? |

**Net:** truly no-code = **Fig 2O, 5H, S13E, S3B** (+ Fig 1A schematic, Fig 6A barplot).
The rest exist but are **plotted inline with no `savefig`** — reproducible by adding one
save call, *if* my cell attribution is right (please confirm the ⚠️ rows).

## 2. Panel letters — now RESOLVED from your full `manuscript.txt` (please sanity-check)

The full legends let me correct my earlier inferences. Key changes applied to the chapters:

- **Fig 1B is the assay *workflow diagram* (Illustrator, no code); Fig 1C is the browser
  shot** (`fig1/01`). I had them merged as "1B/C browser" — fixed.
- **Fig 3F = `fig3/06.mCH_mCG_comp`** (mCH around mCG compartments >100 kb) — I had wrongly
  put 3F on `fig3/08`. This also resolves "nb06 has no figure." 3G/3H = `fig3/07`.
- **Fig 6G = motif enrichment** of loop-DMR-pair groups (Table S3), not a strength summary.
  **6H** = Epi-TPB t-SNE by subtype-donor; **6I** = DMR mCG + DEG expr; **6J** = DMR
  flanking mCG; **6K** = DMR compartment fractions.
- Added **S9C** (`fig2/01` c38, browser diff y-range), **S9D**, **S12C** (`fig2/04` c65),
  **S14C/D/E** definitions.

**Still needs a cell pinned (analysis exists, exact `savefig` unclear):**
- **Fig 3I / S23B** — mCH↔DEG-expression correlation violins (Epi Endcri). Which notebook/cell? (`fig3/02`, `09`, or `10`?)
- **Fig 6G** — motif enrichment of loop-DMR groups (Mus Skl). Is there a plot cell, or is it compute-only like 2O/5H?
- **Fig 6J** — Epi-TPB DMR flanking-mCG panel — I don't see a `savefig` in `fig6/07`.
- **Fig S32D** — Schwann DMR/diff-loop heatmap cell in `fig6/09`.
- **Fig S14C** — mCG-across-ATAC-peaks violin cell in `fig2/16`.
- **`fig3/08.mCH_hetero`** — has no clear main/ED panel in the legend. What figure is it for (or is it methods/unused)?

## 3. Fig 6 assembly (revised after reading the figure — please confirm)

- Final **Fig 6B/C** = **donor-joint t-SNE coordinates** (`02.MusSkl_donor_clustering`)
  colored by the **donor-separate cluster labels/colors**. ✅ per your note.
- **⚠ Which MusSkl_diff variant is published?** Fig 6D is a **3×3** confusion matrix
  (mC/3C × Stem/Fast/Slow) and Fig 6F/6G have **7 columns** (the populated mC/3C combos),
  so the figure uses **7 groups** → **`06.MusSkl_diff_7group`** looks like the published one,
  **not** `04` (8-group). Please confirm. (My first pass wrongly said `04`.)
- **Fig 6A (ARI barplot)** — the barplot **does exist in the paper** (ARI per major type,
  Neu Inh→Epi Aci). ARI values are in `fig5/07` c18–c19; **where is the barplot rendered?**
- **Fig 6G (motif dot plot)** — **exists in the paper** (NES-colored dot plot). The
  cisTarget/SCENIC+ compute is in the MusSkl_diff notebooks; **which cell draws the dot plot?**
- **`09.NTbSchw_clustering`** trailing cells (c77–c93) overwrite `Mus-Skl/` products — I
  recommend deleting them. OK to delete?

## 4. README mapping corrections I applied (please sanity-check)

| Original README | I changed it to |
|-----------------|------------------|
| Fig 1/01 → S4 | S4 is in `fig2/05` (01 has no ATAC code) — **but you flagged S4; may be neither** |
| Fig 2 S9 → nb08/09 | S9A/B in `fig2/02`; 08/09 are calling pipelines |
| Fig 2 S10 → nb11/12 | S10D/E in `fig2/02`; S10A–C in `fig2/10` |
| Fig 3 3C/S17–18 → nb04 | 3C/S19=`fig3/05`; S17–18=`fig3/02`; nb04=S21 |
| Fig 3 3D–E → nb02 | 3D–E=`fig3/09` (nb02 heatmaps inline-only) |

## 4b. EDFig producers NOT found in `code_share` (verified by reading the figures)

These are published Extended Data panels whose **plotting code isn't in the released
notebooks** — please point me to where they live (likely the messy `analysis/` tree):

- **S3A/B** — DEG↔loop and DEG↔mCG-at-DMR cosine similarity across **colon/stomach/skin/
  heart** subtypes. `fig4/09.loop_rna` only does the breast analog. Multi-tissue producer?
- **S4** — per-tissue **ATAC + snm3C joint-embedding** t-SNE (Seurat integration; ST/SkGcn/
  Sk/PBMC/M1C). Not `fig2/05` (that's DMR–peak overlap). Where is the joint embedding done?
- **S6A/B/C** — subtype-donor mCG & loop-strength correlation heatmaps + donor/subtype/
  majortype violins. My `fig1/09` attribution is uncertain.
- **S32E–H** — **Enteric (Epi-Ent)** and **Gastric (Epi-Gas)** DMR mCG / diff-loop / DEG
  heatmaps. `08.Epi-Gas` only makes t-SNEs. Where are the Epi-Ent/Epi-Gas DMR·loop·DEG panels?
- **Dot-plot motif panels 2O / S13E / 5H / 6G** — published dot plots (NES / #hits); SCENIC+
  compute is present, the **dot-plot rendering cell** is not.
- **6A** ARI barplot — published; render cell not located.

(Verified OK by reading the figure: S1 A+B = `fig1/02`; S9 A–D; S12 A–C; S13 A–D = `fig2/05`;
S14 A–E; S23 A + B; S28 A/B = `fig5/07` scatter grids; S32 A = Skl 7-group, B–D = Schwann `fig6/09`.)

## 5. Notebooks whose figure I could not place

- **`fig6/10–14` (colon/stomach mCT notebooks)** — ✅ **RESOLVED: no mCT data is shown in the
  paper**, so these have no published panel. Decision needed: **keep them (labeled "not in
  paper")** or **drop them from the book?** The true producers of **S32E–H** (Epi-Gas /
  Epi-Ent DMR·loop·DEG) are elsewhere — deferred per your note.
- **`fig2/17.geneCG_expr_corr`** — gene mCG vs expression correlation; doesn't match a
  lettered Fig 2 / S9–S15 panel. Supporting analysis? which figure?
- **`fig2/11,12,14`** — lineage DMR/expression heatmaps; feed the RNA comparison (S3-style)?
- ~~`fig3/06.mCH_mCG_comp`~~ — **RESOLVED: this is Fig 3F.**

---

*Everything not in this file, I'm reasonably confident about (see each figure chapter's
panel table and `gaps.md`).*
