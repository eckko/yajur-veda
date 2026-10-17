# Shukla Yajurveda (Vajasaneyi Madhyandina Samhita): raw extracted source bank

Raw extracted source bank. `text/ch00.NN.md` is the extracted Sanskrit, not a finished edition and not human-proofread. For chapters 1-10 there are also AI-drafted, AI-reviewed layers (`-sandhi`, `-hindi`, `-english`); chapters 11-40 have none yet. Work files are in `layers-work/`.

Read, in order: FORMAT.md (file and line format), toc.md (structure), STATUS.md (what is done), sources.md (where text came from), ISSUES.md (known doubts).

Rules for anyone editing here:
- Text lines come only from sources listed in sources.md; never from memory.
- Do not rename files or change line IDs of finished chapters.
- Record every doubt in ISSUES.md; fix text only in a later, explicit proofreading stage.
- Run `python3 reference/tools/check_extraction.py reference/shukla-yajurveda-vajasaneyi` before every commit.
- Branch pattern: `docs/YYYY-MM-DD/version-N`; push new branches only; the owner merges.

How to continue: open STATUS.md, take the first chapter not marked extracted, follow the skill `/extract-vedic-book-web`.
