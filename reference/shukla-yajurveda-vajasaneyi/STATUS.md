# Status: shukla-yajurveda-vajasaneyi

Updated: 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1 (DharmicData, Madhyandina). 40 of 40 adhyayas extracted, 1,975 verses, 3,309 lines.

The checker reports 24 errors, all stray Latin `j`/`k` letters kept exactly as in S1 (logged line by line in ISSUES.md). No other errors. No published translations found. Chapters 1-10 now carry AI-drafted, independently AI-reviewed layers (sandhi split, Hindi, English); chapters 16-40 have none yet.

| Part | Chapter | Sanskrit lines | Source | Hindi | English | Check | Notes |
|---|---|---|---|---|---|---|---|
| 00 | 01 | 57 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 02 | 52 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 1 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 03 | 81 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 2 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 04 | 55 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 4 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 05 | 73 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 4 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 06 | 57 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 6 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 07 | 97 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 6 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 08 | 130 | S1 | reviewed AI draft | reviewed AI draft | errors (Latin) | 1 line(s) with stray Latin letter (checker error, see ISSUES.md) |
| 00 | 09 | 71 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 10 | 61 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 11 | 132 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 12 | 179 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 13 | 105 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 14 | 68 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 15 | 107 | S1 | reviewed AI draft | reviewed AI draft | pass |  |
| 00 | 16 | 78 | S1 | -- | -- | pass |  |
| 00 | 17 | 176 | S1 | -- | -- | pass |  |
| 00 | 18 | 114 | S1 | -- | -- | pass |  |
| 00 | 19 | 155 | S1 | -- | -- | pass |  |
| 00 | 20 | 127 | S1 | -- | -- | pass |  |
| 00 | 21 | 96 | S1 | -- | -- | pass |  |
| 00 | 22 | 41 | S1 | -- | -- | pass |  |
| 00 | 23 | 101 | S1 | -- | -- | pass |  |
| 00 | 24 | 50 | S1 | -- | -- | pass |  |
| 00 | 25 | 87 | S1 | -- | -- | pass |  |
| 00 | 26 | 45 | S1 | -- | -- | pass |  |
| 00 | 27 | 91 | S1 | -- | -- | pass |  |
| 00 | 28 | 94 | S1 | -- | -- | pass |  |
| 00 | 29 | 117 | S1 | -- | -- | pass |  |
| 00 | 30 | 29 | S1 | -- | -- | pass |  |
| 00 | 31 | 44 | S1 | -- | -- | pass |  |
| 00 | 32 | 32 | S1 | -- | -- | pass |  |
| 00 | 33 | 171 | S1 | -- | -- | pass |  |
| 00 | 34 | 109 | S1 | -- | -- | pass |  |
| 00 | 35 | 34 | S1 | -- | -- | pass |  |
| 00 | 36 | 37 | S1 | -- | -- | pass |  |
| 00 | 37 | 43 | S1 | -- | -- | pass |  |
| 00 | 38 | 55 | S1 | -- | -- | pass |  |
| 00 | 39 | 24 | S1 | -- | -- | pass |  |
| 00 | 40 | 34 | S1 | -- | -- | pass |  |

## Layers (chapters 1-15)
- Files `text/ch00.NN-sandhi.md`, `-hindi.md`, `-english.md` for NN = 01 to 15, same IDs and line count as the Sanskrit. Each unit's translation sits on its first line, `~` on the rest.
- Made by an AI draft pass, then an independent AI review, then fixes (automatic and by hand). Not read by a human. Many forms are obscure and marked low confidence in `layers-work/p00/chNN/chunkK_final.json` notes.
- Chapters 16-40: not started (see `layers-work/STATUS.md`). The quiz feed (`build_feed.py`) is not built because part 00 is not fully covered.

## Next
- Get S2 (Sanskrit Library TEI XML) or S3 (GRETIL) downloaded by the owner to cross-check and to resolve the `j` letters and numbering notes.
- Decide whether to continue layers for chapters 11-40, and find real Hindi and English translations to check the AI drafts against.
- Parser: tools/parse_s1.py (re-run reproduces text/ exactly).
