#!/usr/bin/env python3
"""Validate local Markdown links in README.md.

External URLs, anchors, mailto links and sandbox-like non-repository links are
ignored. Every relative repository path referenced by README must exist.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

def clean_target(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    target = unquote(target)
    return target or None

def main() -> int:
    text = README.read_text(encoding="utf-8")
    missing = []
    checked = []
    for raw in LINK_RE.findall(text):
        target = clean_target(raw)
        if target is None:
            continue
        p = (ROOT / target).resolve()
        try:
            p.relative_to(ROOT.resolve())
        except ValueError:
            missing.append((target, "escapes repository root"))
            continue
        checked.append(target)
        if not p.exists():
            missing.append((target, "missing"))
    if missing:
        print("README LINK AUDIT: FAIL")
        for target, why in missing:
            print(f" - {target}: {why}")
        return 1
    print(
        f"README LINK AUDIT: PASS "
        f"({len(checked)} local links checked; {len(set(checked))} unique)"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
