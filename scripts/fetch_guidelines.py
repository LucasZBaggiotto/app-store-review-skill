#!/usr/bin/env python3
"""Fetch the live App Store Review Guidelines into references/_cache/.

Use when you need Apple's exact current wording, or to check whether a rule
changed since this skill was last synced.

    python3 scripts/fetch_guidelines.py           # write the cache, print the date
    python3 scripts/fetch_guidelines.py --print   # also dump the text to stdout
"""
import html
import pathlib
import re
import sys
import urllib.request

URL = "https://developer.apple.com/app-store/review/guidelines/"
OUT = pathlib.Path(__file__).resolve().parent.parent / "references" / "_cache" / "guidelines.txt"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def to_text(raw: str) -> str:
    match = re.search(r"<main.*?</main>", raw, re.S) or re.search(r"<body.*?</body>", raw, re.S)
    body = match.group(0) if match else raw
    body = re.sub(r"<(script|style|nav|footer|header)\b.*?</\1>", "", body, flags=re.S)
    body = re.sub(r"</(p|div|li|h1|h2|h3|h4|tr)>", "\n", body)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)
    body = re.sub(r"[ \t]+", " ", body)
    return re.sub(r"\n\s*\n+", "\n\n", body).strip()


def main() -> int:
    text = to_text(fetch(URL))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")

    stamp = re.search(r"Last Updated:\s*(.+)", text)
    print(f"Wrote {len(text):,} chars to {OUT}")
    print(f"Apple's stated last update: {stamp.group(1).strip() if stamp else 'not found'}")
    if "--print" in sys.argv:
        print("\n" + text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
