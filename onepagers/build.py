#!/usr/bin/env python3
"""Build every one-pager in English and Swedish.

    pip install weasyprint==70.0
    python3 onepagers/build.py            # all products, both languages
    python3 onepagers/build.py zap        # one product
    python3 onepagers/build.py --html     # HTML only, no WeasyPrint
    python3 onepagers/build.py --thumbs   # also the preview images (needs pdftoppm)

Each PDF lands in <product>/<product>-one-pager-<lang>.pdf, and each device drawing in
assets/devices/<name>.svg. The build fails if a one-pager is not exactly one A4 page.
"""
import importlib
import shutil
import subprocess
import sys

from common import ROOT, render

PRODUCTS = {"zap": "zap", "zap-han": "zap_han", "blixt": "blixt", "blixt-x": "blixt_x"}
LANGS = ("en", "sv")


def main(argv):
    pdf = "--html" not in argv
    wanted = [a for a in argv if not a.startswith("--")] or list(PRODUCTS)
    for product in wanted:
        module = importlib.import_module(PRODUCTS[product])
        for lang in LANGS:
            out = ROOT / product / f"{product}-one-pager-{lang}.pdf"
            render(f"{product}-{lang}", module.build(lang), out, pdf=pdf)
            if pdf and "--thumbs" in argv:
                thumb(out, ROOT / product / "images" / f"one-pager-{lang}")
        out_dir = ROOT / "assets" / "devices"
        out_dir.mkdir(parents=True, exist_ok=True)
        for name, svg in module.devices().items():
            (out_dir / f"{name}.svg").write_text(svg)
            print(f"wrote assets/devices/{name}.svg")


def thumb(pdf, stem):
    if not shutil.which("pdftoppm"):
        sys.exit("--thumbs needs pdftoppm (poppler)")
    stem.parent.mkdir(exist_ok=True)
    subprocess.run(["pdftoppm", "-r", "70", "-png", "-singlefile", str(pdf), str(stem)], check=True)
    print(f"wrote {stem.relative_to(ROOT)}.png")


if __name__ == "__main__":
    main(sys.argv[1:])
