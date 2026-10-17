# VERIFY log: shukla-yajurveda-vajasaneyi

## 2026-10-17 inventory
- Base: `text/ch00.01.md` to `ch00.40.md` (Devanagari, `ID | text`), source S1 (DharmicData). No second edition available.
- `tools/parse_s1.py` is the extraction parser written in stage 1 (kept, not a book file); `reference/tools/check_extraction.py` is the stage-1 checker; `raw/` holds the S1 JSON.
- `taittiriya-samhita/` has no text (blocked, no reachable source); excluded from this run.

## 2026-10-17 word check
- word_check.py: 28,710 tokens, 15,079 distinct. 883 "stray" rows: 859 are U+1CEA (the Vedic sign ᳪ, legitimate here, a checker false alarm), 23 Latin `j`, 1 Latin `k`, 6 en dashes (U+2013), 1 U+00AC. 33 typo candidates. 2,102 metre rows.
- Second edition: not available, skipped.
- Before packing for the AI pass I set aside the full tables (`checks/stray_all.tsv`, `checks/metre_all.tsv`) and packed only the 24 stray rows left after removing ᳪ, the typo candidates and a 1-in-40 sample of ordinary verses. Reason: the metre check counts aksharas for verse lines, but most Yajurveda mantras are prose (yajus), so 2,102 flagged lines are expected, not errors; ᳪ rows are noise.

## 2026-10-17 AI proofreading
- 3 packs, 149 items, all answered. 29 proposals. Sample error rate 4/92 (4.3%). See ISSUES.md and checks/PROOFREAD.md. `text/` untouched.
- plan_work.py: 55 chunks, 1,975 units, about 0.7 million draft output tokens plus about the same for the review. Not started; waiting for the owner to choose the scope.

## 2026-10-17 layers, chapters 1-10
- 10 chapters, 427 units: AI draft (sonnet), independent AI review, `apply_review.py --add-source`, remaining items settled by hand and logged in `layers-work/p00/chNN/changes_K.json`. Reviewers found errors in every chunk (about 30-80 issues each), mostly glossary breaks, added words and wrong grammar labels; all patchable ones are fixed, unclear readings carry notes and low confidence.
- Written with `write_layers.py`; `layers-work/GLOSSARY.md` holds the fixed renderings. Not human-read.
- Chapters 11-40: pending. `build_feed.py` not run.

## 2026-10-17 layers, chapters 11-15
- Same pipeline as chapters 1-10 (AI draft, independent AI review, fixes applied automatically and by hand, logged in `changes_K.json`). 15 chapters now have layers (about 835 units). Not human-read. Chapters 16-40: pending; `build_feed.py` not run.
