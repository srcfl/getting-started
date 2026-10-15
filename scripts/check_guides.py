#!/usr/bin/env python3
"""Check the guides against CONTRIBUTING.md.

- Every product has README.md (English) and README.sv.md (Swedish), each with its
  header fields (Applies to / Last verified / For, or Gäller / Senast verifierad / För)
  and a sources section (## Sources / ## Källor).
- Every product has a one-pager in both languages and a field-test CHECKLIST.md, and
  the guides say whether that field test is done (Field test / Fälttest).
- Relative links and images point at files that exist.
- The root README links to every guide.
- Nothing internal leaks out: private IPs, internal host names, fleet names, keys.

Run: python3 scripts/check_guides.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES = ["zap", "zap-han", "blixt", "blixt-x"]

FORBIDDEN = [
    (re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"), "private IP address (10.x)"),
    (re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"), "private IP address (192.168.x)"),
    (re.compile(r"\b172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}\b"), "private IP address (172.16–31.x)"),
    (re.compile(r"balena\.srcful\.dev", re.I), "internal host name (openBalena)"),
    (re.compile(r"\bsvk-[a-z0-9]+"), "fleet name (svk-*)"),
    (re.compile(r"\b[0-9a-f]{32}\b"), "device UUID or key"),
    (re.compile(r"(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*\S+", re.I), "key or password"),
    (re.compile(r"ssh\s+\S*root@", re.I), "SSH login"),
]

LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def check_links(path, text):
    for target in LINK.findall(text):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        file_part = target.split("#", 1)[0]
        if not file_part:
            continue
        if not (path.parent / file_part).exists():
            err(path, f"link points at something that does not exist: {target}")


LANG_FIELDS = {
    "README.md": (("**Applies to:**", "**Last verified:**", "**For:**", "**Field test:**"), "## Sources"),
    "README.sv.md": (("**Gäller:**", "**Senast verifierad:**", "**För:**", "**Fälttest:**"), "## Källor"),
}


def check_guide(name):
    for filename, (fields, sources) in LANG_FIELDS.items():
        path = ROOT / name / filename
        if not path.exists():
            err(ROOT / name, f"missing {filename}")
            continue
        text = path.read_text()
        head = text[:1500]
        for field in fields:
            if field not in head:
                err(path, f"missing {field} at the top")
        if not re.search(r"\*\*(Last verified|Senast verifierad):\*\*\s*\d{4}-\d{2}-\d{2}", head):
            err(path, "last-verified date missing (YYYY-MM-DD)")
        if not re.search(rf"^{re.escape(sources)}\s*$", text, re.M):
            err(path, f"missing {sources}")
    if not (ROOT / name / "CHECKLIST.md").exists():
        err(ROOT / name, "missing CHECKLIST.md (the field-test checklist)")
    for lang in ("en", "sv"):
        pdf = ROOT / name / f"{name}-one-pager-{lang}.pdf"
        if not pdf.exists():
            err(ROOT / name, f"missing {pdf.name}")


def main():
    for filename in ("README.md", "README.sv.md"):
        readme = ROOT / filename
        if not readme.exists():
            err(ROOT, f"missing {filename}")
            continue
        index = readme.read_text()
        for name in GUIDES:
            if f"{name}/" not in index:
                err(readme, f"does not link to {name}/")

    for name in GUIDES:
        check_guide(name)

    for path in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text()
        check_links(path, text)
        for pattern, what in FORBIDDEN:
            hit = pattern.search(text)
            if hit:
                err(path, f"{what}: {hit.group(0)!r}")

    if errors:
        print("\n".join(errors))
        sys.exit(f"{len(errors)} problem(s)")
    print(f"ok: {len(GUIDES)} guides, both languages, no problems")


if __name__ == "__main__":
    main()
