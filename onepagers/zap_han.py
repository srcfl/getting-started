"""Zap HAN one-pager: connect a Zap HAN to a meter's RJ45 HAN port.

Sources:
- David (2026-10-15): the Zap HAN has the same box and sockets as the Zap P1, but no separate
  blue status light; the light in its RJ12 socket is an RGB light that does that job
  (rainbow at boot). It ships with an RJ12-to-RJ45 cable and always needs USB-C power
  (5 V, at least 1 A), because the HAN port does not power the Zap the way a P1 port does.
  Tested with Kamstrup.
- Aidon RJ45 HAN interface v1.6 A: pin 1 M-Bus data/power (12-24 V, 30 mA max, about 700 mW),
  pins 2 and 8 GND, 6-7 do not connect; the HAN port and its power are off until the grid
  company turns them on.
- srcfl/srcful-zap-x-firmware main: zap-han.h (HAN input 2400 8N1, one WS2812 RGB LED),
  main.cpp (rainbow at boot; Bluetooth only without saved Wi-Fi), main_loop.cpp (blue while
  waiting for the app, off when Bluetooth closes, button 2/5/10 s), fw_controller/API.md
  (detected_type han_uart), decoders (no decryption).
- The app 2.7.9: same onboarding as the Zap P1; meter added as "P1 / HAN meter".
"""
from zap import zap_top
from common import (crop, BLUE, BOLT, CREAM, GREEN, IC_METER, IC_PHONE, IC_PLUG, IC_WIFI, INK,
                    LOGO_LIGHT, MONO, MUTED, PLASTIC, SIGNAL, TICK, fill, jack_g, marker, page,
                    pattern, pattern_svg)

T = {
    "sv": {
        "title": "Koppla en Zap HAN",
        "rail": "Installationsguide &middot; Zap HAN &middot; Mainnet",
        "lede": "För installatören, på plats. För mätare med RJ45 HAN-uttag. Har mätaren RJ12 P1: använd <b>Zap P1</b>.",
        "before": "Innan du åker",
        "p1_t": "HAN-porten påslagen", "p1_d": "Hos elnätsbolaget, före besöket.",
        "wifi_t": "Wifi, bara 2,4&nbsp;GHz", "wifi_d": "Nätnamn och lösenord.",
        "app_t": "Appen och Bluetooth", "app_d": "Sourceful Energy, inloggad.",
        "pow_t": "Kabel och ström", "pow_d": "RJ12–RJ45-kabeln. USB-C, 5 V, minst 1 A.",
        "meter": "ELMÄTARE", "reading": "12 345,6", "jack": "RJ45", "pins": "8 STIFT · HAN",
        "zap_above": "ZAP HAN OVANIFRÅN", "out": "P1 UT", "rs485": "RS485", "button": "KNAPP", "status": "", "in": "IN · RJ12", "usbc": "USB-C",
        "charger": "Laddare", "charger_sub": "5 V · KRAV",
        "cable": "RJ45 → RJ12", "lights": "LAMPAN",
        "rows": [
            ("rainbow", "Regnbåge", "~1 s", "Startar"),
            (BLUE, "Blå, fast", "", "Väntar på appen"),
            ("off", "Släckt", "", "Igång, eller ingen ström"),
            (BLUE, "Blå, snabb", "KNAPP", "5–10 s: wifi rensas"),
        ],
        "s1_h": "Hitta porten",
        "s1_p": "Det bredare uttaget med åtta stift (RJ45), märkt <b>HAN</b>. Ofta bakom ett lock.",
        "s1_warn": "Aldrig en <b>Zap P1</b> eller adapter i RJ45 HAN. Bara Zap HAN och dess kabel.",
        "s2_h": "Koppla in",
        "s2_p": "RJ45-änden i mätaren, RJ12-änden i Zappens <b>IN</b>, långsidan med USB-C. Båda ska klicka. Sätt i USB-C: HAN-porten ger ingen ström till Zap.",
        "s2_q": "Zap HAN startar bara med USB-C-ström.",
        "s3_h": "Kolla lampan",
        "s3_p1": "Lampan sitter i RJ12-uttaget. Regnbåge en sekund: Zap startar. Sedan blå, fast: den väntar på appen.",
        "s3_p2": "Ingen blå: håll knappen 5–10&nbsp;s tills den blinkar snabbt, släpp.",
        "s4_h": "I appen", "s4_micro": "Samma flöde som Zap P1",
        "app_steps": [
            ("Logga in", "Öppna Sourceful Energy. Saknas profil eller anläggning: skapa dem först."),
            ("<b>Lägg till en ny Zap</b>", "Under <b>Kom igång</b>, eller <b>Mer → Mina Zappar</b>."),
            ("Välj Zappen", "Blå ska lysa fast. Stå nära, välj den med flest staplar."),
            ("<b>Registrera &amp; konfigurera nätverk</b>", "Zappen hamnar i profilen du har vald."),
            ("Wifi, 2,4&nbsp;GHz", "Nät, lösenord, <b>Anslut</b>, sedan <b>Klar</b>. Dolt nät: <b>Ange manuellt</b>."),
            ("Mätaren", "<b>Elmätare → P1 / HAN-mätare → Identifiera mätare</b>."),
        ],
        "s5_h": "Klart när",
        "seen": "Det här syns",
        "ok1_q": "Appen", "ok1": "Visar mätardata inom två minuter efter <b>Mätaren är tillagd</b>.",
        "ok2_q": "Lampan släckt", "ok2": "En minut efter att wifi är uppe. Bluetooth har stängt.",
        "ok3_q": "<code>han_uart</code>", "ok3": "Syns på mätaren i <code>zap.local/api/devices</code>.",
        "ifnot": "Om inte",
        "f1_q": "Mätaren kunde inte identifieras", "f1": "HAN-porten är inte påslagen, eller kabeln sitter fel. Be elnätsbolaget slå på den.",
        "f2_q": "Krypterad mätare", "f2": "Stöds inte än. Kontakta Sourceful.",
        "f3_q": "Allt släckt, syns inte i appen", "f3": "Ingen ström. Kontrollera USB-C-laddaren.",
        "wifi_h": "Byta wifi",
        "wifi_p": "Håll knappen 5–10&nbsp;s (snabb blå blink), släpp. Sedan:<br>",
        "wifi_path": ["<b>Mina Zappar</b>", "Zappen", "<b>Konfigurera om WiFi</b>", "välj&nbsp;den", "<b>Konfigurera Nätverk</b>", "nät, lösenord", "<b>Anslut</b>"],
        "card_k": "HAN", "card_m": "Mätare som stöds",
        "card1": "<b>Okrypterad HAN</b> (DLMS/COSEM över M-Bus). Krypterade mätare fungerar inte än.",
        "card2": "Testad med <b>Kamstrup</b>. Andra märken: fråga Sourceful innan du installerar.",
        "card3": "Elnätsbolaget måste slå på HAN-porten. Den är ofta av från start.",
        "foot1": "firmware main &middot; appen 2.7.9 &middot; Aidon HAN v1.6 &middot; 2026-10-15",
        "foot2": "RJ45: Open Connector Graphics, CC BY 4.0",
    },
    "en": {
        "title": "Connect a Zap HAN",
        "rail": "Installation guide &middot; Zap HAN &middot; Mainnet",
        "lede": "For the installer, on site. For meters with an RJ45 HAN port. Meter with RJ12 P1: use <b>Zap P1</b>.",
        "before": "Before you go",
        "p1_t": "HAN port enabled", "p1_d": "By the grid operator, beforehand.",
        "wifi_t": "Wi-Fi, 2.4&nbsp;GHz only", "wifi_d": "Network name and password.",
        "app_t": "App and Bluetooth", "app_d": "Sourceful Energy, signed in.",
        "pow_t": "Cable and power", "pow_d": "The RJ12–RJ45 cable. USB-C, 5 V, at least 1 A.",
        "meter": "ELECTRICITY METER", "reading": "12,345.6", "jack": "RJ45", "pins": "8 PINS · HAN",
        "zap_above": "ZAP HAN FROM ABOVE", "out": "P1 OUT", "rs485": "RS485", "button": "BUTTON", "status": "", "in": "IN · RJ12", "usbc": "USB-C",
        "charger": "Charger", "charger_sub": "5 V · REQUIRED",
        "cable": "RJ45 → RJ12", "lights": "THE LIGHT",
        "rows": [
            ("rainbow", "Rainbow", "~1 s", "Starting"),
            (BLUE, "Blue, solid", "", "Waiting for the app"),
            ("off", "Off", "", "Running, or no power"),
            (BLUE, "Blue, fast", "BUTTON", "5–10 s: Wi-Fi cleared"),
        ],
        "s1_h": "Find the port",
        "s1_p": "The wider socket with eight pins (RJ45), labelled <b>HAN</b>. Often behind a cover.",
        "s1_warn": "Never a <b>Zap P1</b> or an adapter in RJ45 HAN. Only the Zap HAN and its cable.",
        "s2_h": "Plug in",
        "s2_p": "The RJ45 end into the meter, the RJ12 end into the Zap's <b>IN</b>, the long side with USB-C. Both should click. Plug in USB-C: the HAN port does not power the Zap.",
        "s2_q": "The Zap HAN only starts on USB-C power.",
        "s3_h": "Check the light",
        "s3_p1": "The light sits in the RJ12 socket. Rainbow for a second: starting. Then blue, solid: waiting for the app.",
        "s3_p2": "No blue: hold the button 5–10&nbsp;s until it blinks fast, let go.",
        "s4_h": "In the app", "s4_micro": "Same flow as Zap P1",
        "app_steps": [
            ("Sign in", "Open Sourceful Energy. No profile or site yet: create them first."),
            ("<b>Onboard a new Zap</b>", "Under <b>Get started</b>, or <b>More → My Zaps</b>."),
            ("Pick the Zap", "Blue must be solid. Stand close, pick the one with most bars."),
            ("<b>Claim &amp; Configure network</b>", "The Zap joins the profile you have selected."),
            ("Wi-Fi, 2.4&nbsp;GHz", "Network, password, <b>Connect</b>, then <b>Done</b>. Hidden: <b>Enter manually</b>."),
            ("The meter", "<b>Energy Meters → P1 / HAN meter → Detect meter</b>."),
        ],
        "s5_h": "Done when",
        "seen": "You see this",
        "ok1_q": "The app", "ok1": "Shows meter data within two minutes of <b>Meter added</b>.",
        "ok2_q": "The light is off", "ok2": "A minute after Wi-Fi is up. Bluetooth has closed.",
        "ok3_q": "<code>han_uart</code>", "ok3": "On the meter in <code>zap.local/api/devices</code>.",
        "ifnot": "If not",
        "f1_q": "The meter was not detected", "f1": "The HAN port is not on, or the cable is wrong. Ask the grid operator to turn it on.",
        "f2_q": "Encrypted meter", "f2": "Not supported yet. Contact Sourceful.",
        "f3_q": "All dark, not in the app", "f3": "No power. Check the USB-C charger.",
        "wifi_h": "Change Wi-Fi",
        "wifi_p": "Hold the button 5–10&nbsp;s (fast blue blink), let go. Then:<br>",
        "wifi_path": ["<b>My Zaps</b>", "the Zap", "<b>Reconfigure WiFi</b>", "pick&nbsp;it", "<b>Configure network</b>", "network, password", "<b>Connect</b>"],
        "card_k": "HAN", "card_m": "Supported meters",
        "card1": "<b>Unencrypted HAN</b> (DLMS/COSEM over M-Bus). Encrypted meters do not work yet.",
        "card2": "Tested with <b>Kamstrup</b>. Other brands: ask Sourceful before you install.",
        "card3": "The grid operator must turn the HAN port on. It is often off at first.",
        "foot1": "firmware main &middot; app 2.7.9 &middot; Aidon HAN v1.6 &middot; 2026-10-15",
        "foot2": "RJ45: Open Connector Graphics, CC BY 4.0",
    },
}

EXTRA_CSS = """
h1{font-size:30pt;}
.path{line-height:1.45;}
.list li{padding:1.25mm 0;}
code{font-family:'JetBrains Mono',monospace;font-size:0.88em;}
"""

RAINBOW = ("#E5484D", "#F5A524", "#F2D53C", "#30A46C", "#3E63DD", "#8E4EC6")


def light_glyph(kind, x, y, r=1.0):
    if kind == "rainbow":
        out = []
        for i, c in enumerate(RAINBOW):
            out.append(f'<circle cx="{x + (i - 2.5) * 0.55:.2f}" cy="{y}" r="{r * 0.55:.2f}" fill="{c}"/>')
        return "".join(out)
    if kind == "off":
        return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" stroke="#9C9A92" stroke-width="0.3"/>'
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{kind}"/>'


def hero(t, export=False):
    W, H = 186, 64.5
    o = [f'<svg class="hero" viewBox="0 0 {W} {H}" style="height:{H}mm" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    if not export:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')
    lab = lambda x, y, s, size=2.1, c=MUTED, anchor="start", weight="400": o.append(
        f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="0.3" fill="{c}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

    # meter with the RJ45 HAN port and the plug in it
    o.append(f'<rect x="8" y="7" width="38" height="52" rx="3.2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    lab(12, 12.6, t["meter"], 2.2)
    o.append(f'<rect x="12" y="14.6" width="30" height="9" rx="1.2" fill="#ECE8DA"/>')
    lab(14.4, 20.6, t["reading"], 3.9, INK)
    lab(36.6, 20.6, "kWh", 1.9)
    jg, jw, jh = jack_g(22.4, 33.6, 0.6, open_w=11.68, pins=8)
    o.append(jg)
    o.append(f'<rect x="22.9" y="36.4" width="8.6" height="5.2" rx="0.9" fill="{PLASTIC}" stroke="{INK}" stroke-width="0.25"/>')
    lab(12, 39.6, "HAN", 2.4, INK, weight="700")

    # magnifier over the RJ45 port
    o.append('<defs><clipPath id="lupp"><circle cx="62" cy="21" r="14"/></clipPath></defs>')
    o.append(f'<line x1="31.6" y1="35.2" x2="50.4" y2="28.6" stroke="{INK}" stroke-width="0.25"/>')
    o.append('<circle cx="62" cy="21" r="14" fill="#FFFFFF"/>')
    big, bw, bh = jack_g(62 - 14.88 * 0.8, 21 - 12.4 * 0.8, 1.6, open_w=11.68, pins=8, frame=False)
    o.append(f'<g clip-path="url(#lupp)">{big}</g>')
    o.append(f'<circle cx="62" cy="21" r="14" fill="none" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="62" y="40.4" text-anchor="middle" font-size="3.6" font-weight="700" fill="{INK}">{t["jack"]}</text>')
    lab(62, 44.1, t["pins"], 2.1, MUTED, "middle")

    # the Zap HAN: the same box as the Zap P1, RGB light in the RJ12 IN socket
    zap_top(o, t, 88, 9.5, han=True)
    zb = 9.5 + 42.7
    ux = 88 + 0.466 * 56                                             # USB-C, with the charger
    o.append(f'<path d="M{ux:.2f} {zb + 0.8:.2f} V{zb + 3.4:.2f}" fill="none" stroke="{INK}" stroke-width="0.9" stroke-linecap="round"/>')
    o.append(f'<rect x="{ux - 4:.2f}" y="{zb + 3.4:.2f}" width="21" height="8.6" rx="2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="{ux + 6.5:.2f}" y="{zb + 7.2:.2f}" text-anchor="middle" font-size="2.5" font-weight="500" fill="{INK}">{t["charger"]}</text>')
    lab(ux + 6.5, zb + 10.4, t["charger_sub"], 1.5, SIGNAL, "middle", "700")

    # the cable: RJ45 in the meter -> RJ12 in the Zap HAN's IN socket, from below
    o.append(f'<path d="M27.2 41.6 V56 C27.2 59.8 29.6 61.8 33.4 61.8 H99 C100.9 61.8 101.9 61.2 101.9 60.2" '
             f'fill="none" stroke="{INK}" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"/>')
    lab(47, 59.6, t["cable"], 2, INK, "middle", "700")

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
        <div><span class="chip">{{IC_WIFI}}</span><div><div class="t">{{wifi_t}}</div><div class="d">{{wifi_d}}</div></div></div>
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


def build(lang):
    t = T[lang]
    track = "".join(
        f'<li><div class="row"><span class="node">{i}</span><span class="line"></span></div>'
        f'<div class="t">{a}</div><div class="d">{b}</div></li>'
        for i, (a, b) in enumerate(t["app_steps"], 1))
    arrow = '&nbsp;<span class="arr">&rarr;</span> '
    values = {k: v for k, v in t.items() if isinstance(v, str)}
    values.update({
        "LOGO": LOGO_LIGHT, "IC_METER": IC_METER, "IC_WIFI": IC_WIFI, "IC_PHONE": IC_PHONE,
        "IC_PLUG": IC_PLUG, "HERO": hero(t), "APP_TRACK": track, "TICK": TICK,
        "WIFI_PATH": arrow.join(t["wifi_path"]),
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)


# Standalone drawings for assets/devices/, cut out of the hero (English labels).
DEVICES = {"zap-han": (84, 1, 64, 63.5)}


def devices():
    return {name: crop(hero(T["en"], export=True), box) for name, box in DEVICES.items()}
