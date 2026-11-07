"""Shared layout for the Zaps with Ethernet: Zap ETH, Zap Ultra X2 and Zap Ultra Mini.

The three share one case family: the IN side has P1 IN, Ethernet and USB-C (and on the
Ultra boards the RS485 terminal), the OUT side has the button, the status light and P1 OUT.
Port positions are measured from the hardware vendor's side images (2026-11-07) as a
fraction of the case length. The case depth is not documented, so the drawing is not to
scale and says so.

Each product module gives LAYOUT (ports and lights) and T (the text in both languages)
and calls build(lang, t, layout).
"""
from common import (crop, rail, BLUE, CREAM, GREEN, IC_METER, IC_PHONE, IC_PLUG, INK, LOGO_LIGHT,
                    MONO, MUTED, PLASTIC, SIGNAL, TICK, BOLT, fill, icon, jack_g, marker, page)

IC_NET = icon('<rect x="3" y="14" width="18" height="6" rx="1.5"/><path d="M7 14v-3h10v3"/><path d="M12 11V4"/>'
              '<path d="M9 4h6"/><circle cx="7" cy="17" r="0.6"/><circle cx="10" cy="17" r="0.6"/>')

RAINBOW = ("#E5484D", "#F5A524", "#F2D53C", "#30A46C", "#3E63DD", "#8E4EC6")


def light_glyph(kind, x, y, r=1.0):
    if kind == "rainbow":
        return "".join(f'<circle cx="{x + (i - 2.5) * 0.55:.2f}" cy="{y}" r="{r * 0.55:.2f}" fill="{c}"/>'
                       for i, c in enumerate(RAINBOW))
    if kind == "off":
        return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" stroke="#9C9A92" stroke-width="0.3"/>'
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{kind}"/>'


def zap_top(o, t, layout, zx, zy):
    """The Zap from above. Lower long side = IN side, upper long side = OUT side, which is
    mirrored as seen from above (the vendor's OUT-side image is taken facing that side)."""
    zw, zh = 56, 42.7
    zb = zy + zh
    X = lambda f: zx + f * zw
    o.append(f'<text x="{zx + zw / 2}" y="{zy - 3.9}" text-anchor="middle" {MONO} font-size="2.1" '
             f'letter-spacing="0.3" fill="{MUTED}">{t["zap_above"]}</text>')
    # the plugs: the P1 cable in P1 IN, the network cable in ETHERNET
    for f, w in ((layout["p1_in"], 6.6), (layout["eth"], 7.8)):
        o.append(f'<rect x="{X(f) - w / 2 - 0.6:.2f}" y="{zb - 0.6:.2f}" width="{w + 1.2:.2f}" height="6.6" rx="0.9" '
                 f'fill="{PLASTIC}" stroke="{INK}" stroke-width="0.25"/>')
        o.append(f'<rect x="{X(f) - 1.5:.2f}" y="{zb + 6:.2f}" width="3" height="2.2" rx="0.5" fill="#BDB8AA"/>')
    o.append(f'<rect x="{zx}" y="{zy}" width="{zw}" height="{zh}" rx="5.6" fill="{INK}"/>')
    o.append(f'<rect x="{zx + 2.2}" y="{zy + 2.2}" width="{zw - 4.4}" height="{zh - 4.4}" rx="3.8" fill="#1F1F1E"/>')
    s = 0.3
    o.append(f'<path d="{BOLT}" fill="{CREAM}" transform="translate({zx + zw / 2 - 22.8 * s:.2f},'
             f'{zy + zh / 2 - 23.3 * s:.2f}) scale({s})"/>')
    lab = f'{MONO} font-size="1.9" letter-spacing="0.2" fill="#B9B6AA" text-anchor="middle"'
    edge = lambda f, w, y, color, rx=0.4: o.append(
        f'<rect x="{X(f) - w / 2:.2f}" y="{y - 0.8:.2f}" width="{w}" height="1.6" rx="{rx}" fill="{color}"/>')
    tick = lambda x, y1, y2: o.append(f'<line x1="{x:.2f}" y1="{y1:.2f}" x2="{x:.2f}" y2="{y2:.2f}" '
                                      f'stroke="#6E6C66" stroke-width="0.2"/>')

    # upper long side, the OUT side
    edge(layout["p1_out"], 8.4, zy, "#55534F")
    o.append(f'<text x="{X(layout["p1_out"]):.2f}" y="{zy + 4.6:.2f}" {lab}>{t["out"]}</text>')
    o.append(f'<circle cx="{X(layout["status"]):.2f}" cy="{zy + 2.6:.2f}" r="0.85" fill="{BLUE}"/>')
    tick(X(layout["status"]), zy + 3.6, zy + 7.4)
    o.append(f'<text x="{X(layout["status"]):.2f}" y="{zy + 9.6:.2f}" {lab}>{t["status"]}</text>')
    o.append(f'<rect x="{X(layout["button"]) - 3:.2f}" y="{zy - 0.8:.2f}" width="6" height="1.6" rx="0.8" '
             f'fill="{INK}" stroke="#8C8A80" stroke-width="0.25"/>')
    tick(X(layout["button"]), zy + 1, zy + 2.9)
    o.append(f'<text x="{X(layout["button"]):.2f}" y="{zy + 4.6:.2f}" {lab}>{t["button"]}</text>')

    # lower long side, the IN side
    edge(layout["p1_in"], 7.2, zb, "#55534F")
    edge(layout["eth"], 8.4, zb, "#55534F")
    edge(layout["usbc"], 5.6, zb, "#8C8A80", 0.8)
    o.append(f'<text x="{X(layout["p1_in"]):.2f}" y="{zb - 3.2:.2f}" {lab}>{t["in"]}</text>')
    o.append(f'<text x="{X(layout["eth"]):.2f}" y="{zb - 6.2:.2f}" {lab}>{t["eth"]}</text>')
    tick(X(layout["eth"]), zb - 1, zb - 5.3)
    o.append(f'<text x="{X(layout["usbc"]):.2f}" y="{zb - 3.2:.2f}" {lab}>{t["usbc"]}</text>')
    term = layout.get("rs485")
    if term:
        f, w, pins = term
        edge(f, w, zb, "#5E8F66", 0.2)
        pitch = w / len(pins)
        for i, pin in enumerate(pins):
            o.append(f'<text x="{X(f) - w / 2 + pitch * (i + 0.5):.2f}" y="{zb - 2.6:.2f}" {MONO} font-size="1.3" '
                     f'font-weight="700" fill="#8FC79A" text-anchor="middle">{pin}</text>')
        o.append(f'<text x="{X(f):.2f}" y="{zb - 5.2:.2f}" {lab}>{t["rs485"]}</text>')
    return zb


def meter_p1(o, t):
    """The meter with its RJ12 P1 port, and the magnifier over the port (as in zap.py)."""
    o.append(f'<rect x="8" y="7" width="38" height="52" rx="3.2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="12" y="12.6" {MONO} font-size="2.2" letter-spacing="0.35" fill="{MUTED}">{t["meter"]}</text>')
    o.append(f'<rect x="12" y="14.6" width="30" height="9" rx="1.2" fill="#ECE8DA"/>')
    o.append(f'<text x="14.4" y="20.6" {MONO} font-size="3.9" fill="{INK}">{t["reading"]}</text>')
    o.append(f'<text x="35.4" y="20.6" {MONO} font-size="1.9" fill="{MUTED}">kWh</text>')
    jg, _, _ = jack_g(23.15, 34.2, 0.6)
    o.append(jg)
    o.append(f'<rect x="23.5" y="36.6" width="7" height="4.9" rx="0.9" fill="{PLASTIC}" stroke="{INK}" stroke-width="0.25"/>')
    o.append(f'<rect x="25.4" y="37.6" width="3.2" height="1.1" rx="0.4" fill="#BDB8AA"/>')
    o.append(f'<text x="12" y="39.6" {MONO} font-size="2.2" letter-spacing="0.2" fill="{INK}" font-weight="700">P1</text>')
    o.append('<defs><clipPath id="lupp"><circle cx="62" cy="21" r="14"/></clipPath></defs>')
    o.append(f'<line x1="30.6" y1="35.4" x2="50.4" y2="28.6" stroke="{INK}" stroke-width="0.25"/>')
    o.append('<circle cx="62" cy="21" r="14" fill="#FFFFFF"/>')
    big, _, _ = jack_g(62 - 12.85 * 0.85, 21 - 12.4 * 0.85, 1.7, frame=False)
    o.append(f'<g clip-path="url(#lupp)">{big}</g>')
    o.append(f'<circle cx="62" cy="21" r="14" fill="none" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="62" y="40.4" text-anchor="middle" font-size="3.6" font-weight="700" fill="{INK}">RJ12</text>')
    o.append(f'<text x="62" y="44.1" text-anchor="middle" {MONO} font-size="2.1" letter-spacing="0.2" fill="{MUTED}">{t["pins"]}</text>')


def hero(t, layout, export=False):
    W, H = 186, 64.5
    o = [f'<svg class="hero" viewBox="0 0 {W} {H}" style="height:{H}mm" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    if not export:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')
    lab = lambda x, y, s, size=2.1, c=MUTED, anchor="start", weight="400": o.append(
        f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="0.3" fill="{c}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

    meter_p1(o, t)
    zx, zy = 88, 9.5
    zb = zap_top(o, t, layout, zx, zy)
    px = zx + layout["p1_in"] * 56
    ex = zx + layout["eth"] * 56

    # the P1 cable: meter -> P1 IN, from below
    o.append(f'<path d="M27 41.4 V56 C27 59.8 29.4 61.8 33.2 61.8 H{px - 2.9:.2f} C{px - 1:.2f} 61.8 {px:.2f} 61.2 {px:.2f} {zb + 8:.2f}" '
             f'fill="none" stroke="{INK}" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"/>')
    # the network cable: ETHERNET -> the router
    bx, by, bw, bh = 128.5, 55.4, 19, 7.6
    o.append(f'<path d="M{ex:.2f} {zb + 8.2:.2f} V{by + 3.6:.2f} C{ex:.2f} {by + 5.4:.2f} {ex + 1.2:.2f} {by + 5.8:.2f} {ex + 3:.2f} {by + 5.8:.2f} H{bx:.2f}" '
             f'fill="none" stroke="{INK}" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="{bx + bw / 2:.2f}" y="{by + 3.5:.2f}" text-anchor="middle" font-size="2.5" font-weight="500" fill="{INK}">{t["router"]}</text>')
    lab(bx + bw / 2, by + 6.2, t["router_sub"], 1.5, SIGNAL, "middle", "700")

    # the light, explained
    lx = 153.5
    lab(lx + 5, 12.6, t["lights"], 2.2)
    y = 18.4
    for kind, name, extra, mean in t["rows"]:
        o.append(light_glyph(kind, lx + 1.6, y - 0.85, 1.0))
        o.append(f'<text x="{lx + 4.6}" y="{y}" font-size="2.6" font-weight="500" fill="{INK}">{name} '
                 f'<tspan {MONO} font-size="1.7" letter-spacing="0.2" fill="{MUTED}">{extra}</tspan></text>')
        o.append(f'<text x="{lx + 4.6}" y="{y + 3.2}" font-size="2.35" fill="#33363C">{mean}</text>')
        y += 9.2

    for n, (cx, cy) in enumerate(((50.6, 9.4), (68, 61.8), (lx + 1.6, 11.9)), 1):
        if not export:
            o.append(marker(n, cx, cy))
    o.append('</svg>')
    return "".join(o)


EXTRA_CSS = """
h1{font-size:24pt;}
.path{line-height:1.45;}
.sub.later{margin-top:2.4mm;}
.list li{padding:1.25mm 0;}
code{font-family:'JetBrains Mono',monospace;font-size:0.88em;}
"""

BODY = """
  <div class="rail">{{LOGO}}<span class="micro">{{rail}}</span></div>
  <div class="top">
    <div class="title">
      <h1>{{title}}<span>.</span></h1>
      <p class="lede">{{lede}}</p>
    </div>
    <div class="prep">
      <div class="micro"><span class="n">00</span>{{before}}</div>
      <div class="prep-grid">
        <div><span class="chip">{{IC_METER}}</span><div><div class="t">{{p1_t}}</div><div class="d">{{p1_d}}</div></div></div>
        <div><span class="chip">{{IC_NET}}</span><div><div class="t">{{net_t}}</div><div class="d">{{net_d}}</div></div></div>
        <div><span class="chip">{{IC_PHONE}}</span><div><div class="t">{{app_t}}</div><div class="d">{{app_d}}</div></div></div>
        <div><span class="chip">{{IC_PLUG}}</span><div><div class="t">{{pow_t}}</div><div class="d">{{pow_d}}</div></div></div>
      </div>
    </div>
  </div>

  {{HERO}}

  <div class="steps3">
    <section>
      <div class="head"><span class="num">1</span><span class="h">{{s1_h}}</span></div>
      <p>{{s1_p}}</p>
      <p class="warn">{{s1_warn}}</p>
    </section>
    <section>
      <div class="head"><span class="num">2</span><span class="h">{{s2_h}}</span></div>
      <p>{{s2_p}}</p>
      <p class="quiet">{{s2_q}}</p>
    </section>
    <section>
      <div class="head"><span class="num">3</span><span class="h">{{s3_h}}</span></div>
      <p>{{s3_p1}}</p>
      <p>{{s3_p2}}</p>
    </section>
  </div>

  <section class="sec">
    <div class="head"><span class="num">4</span><span class="h">{{s4_h}}</span><span class="micro">{{s4_micro}}</span></div>
    <ol class="track">{{APP_TRACK}}</ol>
  </section>

  <section class="sec">
    <div class="head"><span class="num">5</span><span class="h">{{s5_h}}</span></div>
    <div class="cols3">
      <div>
        <div class="sub">{{seen}}</div>
        <ul class="list">
          <li><span class="q">{{TICK}} {{ok1_q}}</span>{{ok1}}</li>
          <li><span class="q">{{TICK}} {{ok2_q}}</span>{{ok2}}</li>
          <li><span class="q">{{TICK}} {{ok3_q}}</span>{{ok3}}</li>
        </ul>
      </div>
      <div>
        <div class="sub">{{ifnot}}</div>
        <ul class="list">
          <li><span class="q">{{f1_q}}</span>{{f1}}</li>
          <li><span class="q">{{f2_q}}</span>{{f2}}</li>
          <li><span class="q">{{f3_q}}</span>{{f3}}</li>
        </ul>
      </div>
      <div>
        <div class="sub">{{wifi_h}}</div>
        <p class="small">{{wifi_p}}</p>
        <div class="path">{{WIFI_PATH}}</div>
      </div>
    </div>
  </section>

  <div class="bottom">
    <section class="saj">
      <div><div class="k">{{card_k}}</div><div class="micro">{{card_m}}</div></div>
      <p>{{card1}}</p>
      <p>{{card2}}</p>
      <p>{{card3}}</p>
    </section>
    <div class="foot">
      <span class="micro">{{foot1}}</span>
      <span class="micro">{{foot2}}</span>
    </div>
  </div>
"""


def build(lang, t, layout, field_tested):
    track = "".join(
        f'<li><div class="row"><span class="node">{i}</span><span class="line"></span></div>'
        f'<div class="t">{a}</div><div class="d">{b}</div></li>'
        for i, (a, b) in enumerate(t["app_steps"], 1))
    arrow = '&nbsp;<span class="arr">&rarr;</span> '
    values = {k: v for k, v in t.items() if isinstance(v, str)}
    values["rail"] = rail(lang, t["rail"], field_tested)
    values.update({
        "LOGO": LOGO_LIGHT, "IC_METER": IC_METER, "IC_NET": IC_NET, "IC_PHONE": IC_PHONE,
        "IC_PLUG": IC_PLUG, "HERO": hero(t, layout), "APP_TRACK": track, "TICK": TICK,
        "WIFI_PATH": arrow.join(t["wifi_path"]),
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)


def device_drawing(t, layout):
    """The Zap alone, for assets/devices/ (English labels)."""
    return crop(hero(t, layout, export=True), (84, 1, 64, 63.5))
