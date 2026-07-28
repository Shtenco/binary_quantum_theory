#!/usr/bin/env python3
"""Validate the GitHub Markdown/LaTeX boundary in every repository Markdown file.

The check intentionally has no third-party dependencies.  It catches the source
errors that most often prevent GitHub MathJax rendering: unclosed delimiters,
unbalanced groups, TeX commands outside math, and unescaped table separators in
inline formulae.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX_COMMAND = re.compile(
    r"\\(?:begin|end|frac|sqrt|sum|prod|int|mathcal|mathfrak|mathrm|text|"
    r"operatorname|alpha|beta|gamma|delta|lambda|mu|pi|rho|sigma|theta|"
    r"Delta|Lambda|Phi|Psi|Theta|Omega|cdot|times|approx|leq|geq|infty)\b"
)
ENVIRONMENT = re.compile(r"\\(begin|end)\{([^{}]+)\}")


@dataclass(frozen=True)
class Problem:
    path: Path
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path.relative_to(ROOT)}:{self.line}: {self.message}"


def validate_expression(source: str, path: Path, line: int) -> list[Problem]:
    problems: list[Problem] = []
    depth = 0
    escaped = False
    for char in source:
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                problems.append(Problem(path, line, "unmatched '}' in math"))
                depth = 0
    if depth:
        problems.append(Problem(path, line, f"{depth} unclosed '{{' group(s) in math"))

    stack: list[str] = []
    for kind, name in ENVIRONMENT.findall(source):
        if kind == "begin":
            stack.append(name)
        elif not stack or stack.pop() != name:
            problems.append(Problem(path, line, f"unmatched \\end{{{name}}}"))
    for name in stack:
        problems.append(Problem(path, line, f"unclosed \\begin{{{name}}}"))
    return problems


def validate_markdown(path: Path) -> tuple[int, list[Problem]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    problems: list[Problem] = []
    expressions = 0
    in_fence = False
    display_source: list[str] | None = None
    display_line = 0

    for number, line in enumerate(lines, 1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        outside: list[str] = []
        position = 0
        while position < len(line):
            if display_source is not None:
                closing = line.find("$$", position)
                if closing < 0:
                    display_source.append(line[position:])
                    position = len(line)
                    continue
                display_source.append(line[position:closing])
                source = "\n".join(display_source)
                problems.extend(validate_expression(source, path, display_line))
                expressions += 1
                display_source = None
                position = closing + 2
                continue

            opening = line.find("$", position)
            if opening < 0:
                outside.append(line[position:])
                break
            if opening and line[opening - 1] == "\\":
                outside.append(line[position : opening + 1])
                position = opening + 1
                continue
            outside.append(line[position:opening])
            if line.startswith("$$", opening):
                display_source = []
                display_line = number
                position = opening + 2
                continue

            closing = opening + 1
            while True:
                closing = line.find("$", closing)
                if closing < 0:
                    problems.append(Problem(path, number, "unclosed inline '$' delimiter"))
                    position = len(line)
                    break
                if line[closing - 1] != "\\":
                    source = line[opening + 1 : closing]
                    problems.extend(validate_expression(source, path, number))
                    if line.startswith("|") and "|" in source:
                        problems.append(
                            Problem(path, number, "unescaped '|' inside table math")
                        )
                    expressions += 1
                    position = closing + 1
                    break
                closing += 1

        plain = re.sub(r"`[^`]*`", "", " ".join(outside))
        if TEX_COMMAND.search(plain):
            problems.append(Problem(path, number, "TeX command outside a math delimiter"))

    if in_fence:
        problems.append(Problem(path, len(lines), "unclosed fenced code block"))
    if display_source is not None:
        problems.append(Problem(path, display_line, "unclosed '$$' delimiter"))
    return expressions, problems


def main() -> int:
    paths = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    total = 0
    problems: list[Problem] = []
    for path in paths:
        count, found = validate_markdown(path)
        total += count
        problems.extend(found)
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print(f"FAIL: {len(problems)} problem(s) in {total} math expression(s)", file=sys.stderr)
        return 1
    print(f"PASS: {total} GitHub LaTeX expression(s) in {len(paths)} Markdown file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
