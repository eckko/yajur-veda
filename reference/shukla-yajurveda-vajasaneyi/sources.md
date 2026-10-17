# Sources: shukla-yajurveda-vajasaneyi

| ID | Name | URL | Edition / editor / year | Script | Licence | Covers | Fetched how | Quality note | Role |
|---|---|---|---|---|---|---|---|---|---|
| S1 | DharmicData, Yajurveda/vajasneyi_madhyadina_samhita.json | https://github.com/bhavykhatri/DharmicData | not stated; README says Vedic Heritage Portal (vedicheritage.gov.in) | Devanagari with Vedic accents | repo: ODbL (LICENSE.txt); portal terms unknown | adhyayas 1-40 | git clone (commit 96b3baf), sha256 62cb8585d20e1f47... | verse numbers sequential in 30 of 40 adhyayas; stray ASCII `:`, `|`, `j` (see ISSUES.md) | primary |
| S2 | Sanskrit Library TEI XML (Scharf, after Weber 1849) | https://sanskritlibrary.org/catalogsText/titus/vedic/vs.html | Weber 1849 | unknown | CC BY-NC-SA 3.0 | all | not reachable from the shell | no download link found | cross-check, user download needed |
| S3 | GRETIL / TITUS | https://gretil.sub.uni-goettingen.de/ | Weber-based | IAST | see site | all | blocked from the shell | | cross-check, user download needed |
| S4 | DharmicData, vajasneyi_kanva_samhita_chapters.json | same repo | Kanva recension | Devanagari | ODbL | adhyayas 2-40 only | not extracted: different recension, chapter 1 missing, verse numbers corrupt in sample | | not used |

Shell reach tested: GitHub and PyPI work; GRETIL, TITUS, Sanskrit Library, SARIT, Sanskrit Documents, archive.org and Wikisource are refused.
Planned conversions (to be done by script and recorded here): ASCII `:` to visarga `ः`, ASCII `|` to danda `।`, verse numbers moved from the text into the ID. Stray Latin `j`/`k` are kept out of silent fixes: they go to ISSUES.md.
