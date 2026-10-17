#!/usr/bin/env python3
"""Parse S1 (DharmicData Madhyandina JSON) into text/ch00.NN.md.

Usage: python3 -I tools/parse_s1.py raw/vajasneyi_madhyadina_samhita.json text
Only mechanical changes: verse-number marker removed from the text (kept in
the ID), closing marker delimiter written as the double danda, ASCII ':' to
visarga, ASCII '|' to danda, NFC. Latin letters and everything else stay as
in the source (see ISSUES.md).
"""
import json, re, sys, unicodedata
from pathlib import Path

src, out = sys.argv[1], Path(sys.argv[2])
DEV = str.maketrans("०१२३४५६७८९", "0123456789")
MARK = re.compile(r"[।॥|]{1,2}[ \t]*([०-९0-9](?:[ \t]*[०-९0-9])*)[ \t]*[।॥|]{1,2}")
LET = "abcdefghijklmnopqrstuvwxyz"

def fix(text):
    text = text.replace(":", "ः").replace("|", "।")
    return unicodedata.normalize("NFC", text)

anomalies, total = [], 0
for chap in json.load(open(src, encoding="utf8")):
    n = chap["adhyaya"]
    text, pos, prev, rows, used = chap["text"], 0, 0, [], set()
    for m in MARK.finditer(text):
        seg = text[pos:m.start()]
        pos = m.end()
        lines = [l.strip() for l in seg.split("\n") if l.strip()]
        if not lines:
            anomalies.append(f"{n}: empty verse before marker {m.group(1)}")
            continue
        lines[-1] += " ॥"
        num = int(re.sub(r"\s", "", m.group(1)).translate(DEV))
        if num != prev + 1:
            anomalies.append(f"{n}: marker {num} after {prev}")
        vid = str(num)
        if num in used:
            fixed = prev + 1
            if fixed in used:
                raise SystemExit(f"cannot place repeated marker {num} in {n}")
            anomalies.append(f"{n}: marker printed {num} after {prev}, "
                             f"ID given as {fixed} (printed number repeats)")
            vid = str(fixed)
            num = fixed
        used.add(num)
        prev = num
        rows.append((num, vid, lines))
    rest = [l.strip() for l in text[pos:].split("\n") if l.strip()]
    if rest:
        anomalies.append(f"{n}: {len(rest)} line(s) after the last marker")
    out_lines = []
    for num, vid, lines in rows:
        if vid is None:
            raise SystemExit(f"duplicate verse number {num} in adhyaya {n}")
        for i, line in enumerate(lines):
            if len(lines) > 26:
                raise SystemExit(f"{n}.{num}: more than 26 lines")
            suffix = LET[i] if len(lines) > 1 else ""
            out_lines.append(f"00.{n:02d}.{vid}{suffix} | {fix(line)}")
    total += len(rows)
    (out / f"ch00.{n:02d}.md").write_text("\n".join(out_lines) + "\n", encoding="utf8")
print("verses", total)
print("\n".join(anomalies))
