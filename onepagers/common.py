"""Shared building blocks for the one-pagers: brand, icons, drawings, rendering."""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
BRAND = ROOT / "assets" / "brand"
CSS = (HERE / "base.css").read_text()

INK, PAPER, CREAM, SIGNAL = "#0A0A0A", "#FAFAF7", "#F5F2E1", "#E85D1F"
GREEN, BLUE = "#15803D", "#1D4ED8"
MUTED, PLASTIC = "#61656F", "#D9D5CA"
MONO = 'font-family="JetBrains Mono"'


def _svg(name):
    s = (BRAND / name).read_text()
    return s[s.index("<svg"):]


LOGO_LIGHT = _svg("big-light.svg")  # dark logo, for light grounds

# The bolt from the squircle mark (small-light.svg), without the squircle
_mark = (BRAND / "small-light.svg").read_text()
_d = _mark[_mark.index('d="') + 3:]
_d = _d[:_d.index('"')]
BOLT = _d[_d.index("M27.2275"):]


# WeasyPrint does not pass currentColor into inline SVG, so the colour is set here
def icon(paths, color=INK, sw="1.6"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'class="ic">{paths}</svg>')


IC_METER = icon('<rect x="4" y="3.5" width="16" height="17" rx="2.5"/><rect x="7" y="6.5" width="10" height="4.5" rx="1"/><circle cx="9" cy="16" r="1"/><circle cx="15" cy="16" r="1"/>')
IC_WIFI = icon(f'<path d="M2.5 9.5a16 16 0 0 1 19 0"/><path d="M5.5 13a11 11 0 0 1 13 0"/><path d="M8.5 16.5a6 6 0 0 1 7 0"/><circle cx="12" cy="20" r="0.6" fill="{INK}"/>')
IC_PHONE = icon('<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>')
IC_CABLE = icon('<rect x="3.5" y="8.5" width="9.5" height="7" rx="1.5"/><path d="M6 8.5V6.8M8.25 8.5V6.8M10.5 8.5V6.8"/><path d="M13 12h3.2a4 4 0 0 1 4 4v4.5"/>')
IC_POWER = icon('<path d="M12 3v8"/><path d="M6.3 7.3a8 8 0 1 0 11.4 0"/>')
IC_LAPTOP = icon('<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2.5 19h19"/>')
IC_LIST = icon('<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/>')
IC_FUSE = icon('<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M12 3v4M12 17v4M9.5 12h5"/>')
IC_SHIELD = icon('<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/>')

TICK = ('<svg class="tick" viewBox="0 0 3.4 3"><path d="M0.4 1.6 l1 1 l2 -2.3" fill="none" '
        f'stroke="{SIGNAL}" stroke-width="0.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def jack_g(x, y, s, open_w=9.65, pins=6, frame=True):
    """RJ12 jack seen from the front.

    Geometry after Open Connector Graphics (Wikke Andeweg, CC BY 4.0), in mm:
    two-step latch slot, 1.02 mm contact pitch, 9.65 mm opening.
    """
    side, top, bottom = 1.6, 1.0, 1.8
    hm, step_h, s1, s2 = 6.86, 1.37, 6.85, 4.11
    hw, hh = open_w + 2 * side, top + 2 * step_h + hm + bottom
    cx = hw / 2
    y0, y1 = top, top + step_h
    y2 = y1 + step_h
    y3 = y2 + hm
    cav = (f"M{cx - s2/2:.3f},{y0} H{cx + s2/2:.3f} V{y1} H{cx + s1/2:.3f} V{y2} "
           f"H{cx + open_w/2:.3f} V{y3} H{cx - open_w/2:.3f} V{y2} H{cx - s1/2:.3f} "
           f"V{y1} H{cx - s2/2:.3f} Z")
    pitch, pw, ph = 1.02, 0.42, 3.3
    span = (pins - 1) * pitch
    p = []
    for i in range(pins):
        px = cx - span / 2 + i * pitch - pw / 2
        p.append(f'<rect x="{px:.3f}" y="{y3 - ph:.3f}" width="{pw}" height="{ph}" fill="{CREAM}"/>')
        p.append(f'<rect x="{px:.3f}" y="{y3 - ph - 0.5:.3f}" width="{pw}" height="0.3" fill="#8C8A80"/>')
    back = (f'<rect x="{cx - open_w/2 + 0.7:.3f}" y="{y3 - 0.5:.3f}" '
            f'width="{open_w - 1.4:.3f}" height="0.5" fill="#2A2A28"/>')
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="0" y="0" width="{hw:.3f}" height="{hh:.3f}" rx="0.9" fill="#FFFFFF" '
            f'stroke="{"#B9B4A6" if frame else "none"}" stroke-width="{0.16 / s:.3f}"/>'
            f'<path d="{cav}" fill="{INK}"/>{back}{"".join(p)}</g>'), hw * s, hh * s


def pattern(kind, color, w=10.0, h=2.2):
    """An LED blink pattern drawn as pills on a track."""
    r = h / 2
    track = f'<rect x="0" y="0" width="{w}" height="{h}" rx="{r}" fill="#E7E3D8"/>'
    pill = lambda x, pw: f'<rect x="{x:.2f}" y="0" width="{pw:.2f}" height="{h}" rx="{r}" fill="{color}"/>'
    marks = {
        "solid": lambda: pill(0, w),
        "fast": lambda: "".join(pill(x, h) for x in (0, 2.6, 5.2, 7.8)),
        "ten": lambda: "".join(pill(x, h) for x in (0, w / 2 - r, w - h)),
        "double": lambda: "".join(pill(x, h) for x in (2.4, 4.9)),
        "once": lambda: pill(0, h),
        "slow": lambda: "".join(pill(x, 2.8) for x in (0, 3.6, 7.2)),
        "off": lambda: "",
    }[kind]()
    return track + marks


def pattern_svg(kind, color, w=10.0, h=2.2, mm=1.25):
    return (f'<svg class="pat" viewBox="0 0 {w} {h}" style="width:{w * mm:.2f}mm;height:{h * mm:.2f}mm" '
            f'xmlns="http://www.w3.org/2000/svg">{pattern(kind, color, w, h)}</svg>')


def marker(n, cx, cy, r=2.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SIGNAL}"/>'
            f'<text x="{cx}" y="{cy + 0.95}" text-anchor="middle" {MONO} font-size="2.7" '
            f'font-weight="700" fill="#FFFFFF">{n}</text>')


def fill(template, values):
    """Replace {{KEY}} placeholders; fail if any is left."""
    out = template
    for key, val in values.items():
        out = out.replace("{{" + key + "}}", val)
    if "{{" in out:
        i = out.index("{{")
        sys.exit(f"unfilled placeholder: {out[i:i + 40]}")
    return out


def page(lang, title, body, extra_css=""):
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
            f'<title>{title}</title><style>{CSS}{extra_css}</style></head>'
            f'<body><div class="page">{body}</div></body></html>')


def render(name, html, pdf_path, pdf=True):
    """Write the HTML next to base.css (so font URLs resolve) and, optionally, the PDF."""
    out_html = HERE / f"_{name}.html"
    out_html.write_text(html)
    if not pdf:
        return
    from weasyprint import HTML
    doc = HTML(filename=str(out_html)).render()
    if len(doc.pages) != 1:
        sys.exit(f"{name}: {len(doc.pages)} pages, must be exactly 1")
    gap = _gap_above_bottom(doc.pages[0])
    if gap < MIN_GAP_MM:
        sys.exit(f"{name}: content runs into the bottom block (gap {gap:.1f} mm, need {MIN_GAP_MM} mm)")
    doc.write_pdf(str(pdf_path))
    print(f"wrote {pdf_path.relative_to(ROOT)} (1 page, {gap:.1f} mm above the bottom block)")


MIN_GAP_MM = 3.0
PX_PER_MM = 96 / 25.4


def _classes(box):
    el = getattr(box, "element", None)
    return (el.get("class") or "").split() if el is not None else []


def _gap_above_bottom(page):
    """Distance in mm between the lowest content box and the top of .bottom.

    The bottom block (SAJ card and footer) is absolutely positioned, so content that
    grows too long slides under it instead of adding a page. This catches that.
    """
    bottom_top, content_end = None, 0.0

    def walk(box, inside_bottom=False):
        nonlocal bottom_top, content_end
        is_bottom = "bottom" in _classes(box)
        if is_bottom:
            bottom_top = box.position_y
        inside = inside_bottom or is_bottom
        if not inside and getattr(box, "element_tag", None) not in (None, "html", "body") \
                and "page" not in _classes(box) and hasattr(box, "margin_height"):
            content_end = max(content_end, box.position_y + box.margin_height() - box.margin_bottom)
        for child in getattr(box, "children", []):
            walk(child, inside)

    walk(page._page_box)
    if bottom_top is None:
        return float("inf")
    return (bottom_top - content_end) / PX_PER_MM
