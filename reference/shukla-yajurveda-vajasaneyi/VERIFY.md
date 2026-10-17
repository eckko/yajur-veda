# VERIFY log: shukla-yajurveda-vajasaneyi

## 2026-10-17 inventory
- Base: `text/ch00.01.md` to `ch00.40.md` (Devanagari, `ID | text`), source S1 (DharmicData). No second edition available.
- `tools/parse_s1.py` is the extraction parser written in stage 1 (kept, not a book file); `reference/tools/check_extraction.py` is the stage-1 checker; `raw/` holds the S1 JSON.
- `taittiriya-samhita/` has no text (blocked, no reachable source); excluded from this run.

## 2026-10-17 word check
- word_check.py: 28,710 tokens, 15,079 distinct. 883 "stray" rows: 859 are U+1CEA (the Vedic sign ᳪ, legitimate here, a checker false alarm), 23 Latin `j`, 1 Latin `k`, 6 en dashes (U+2013), 1 U+00AC. 33 typo candidates. 2,102 metre rows.
- Second edition: not available, skipped.
- Before packing for the AI pass I set aside the full tables (`checks/stray_all.tsv`, `checks/metre_all.tsv`) and packed only the 24 stray rows left after removing ᳪ, the typo candidates and a 1-in-40 sample of ordinary verses. Reason: the metre check counts aksharas for verse lines, but most Yajurveda mantras are prose (yajus), so 2,102 flagged lines are expected, not errors; ᳪ rows are noise.
