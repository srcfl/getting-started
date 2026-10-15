"""Zap one-pager: connect a Zap to the meter and the app (mainnet).

Hardware layout follows the product images in zap/images/ (from srcful-marketing-website
and srcful-flutter-app) and the reference manual on support.sourceful.energy:
  IN side (one long side):  P1 IN (cable lives here), USB-C, green power LED in P1 IN
  OUT side (other long side): P1 OUT, RS485 terminal, button, blue status LED,
                              green data LED in P1 OUT
Button timings come from srcful-zap-x-firmware fw_controller/main/main_loop.cpp:
  >2 s slow blink -> restart, >5 s fast blink -> clear Wi-Fi, >10 s solid -> factory reset.
"""
from common import (crop, rail, BLUE, BOLT, CREAM, GREEN, IC_CABLE, IC_METER, IC_PHONE, IC_WIFI, INK,
                    LOGO_LIGHT, MONO, MUTED, PLASTIC, TICK, fill, jack_g, marker, page,
                    pattern, pattern_svg)

# Set to True when CHECKLIST.md is ticked off on real hardware.
FIELD_TESTED = False

T = {
    "sv": {
        "title": "Koppla en Zap",
        "rail": "Installationsguide &middot; Zap P1 &middot; Mainnet",
        "lede": "För installatören, på plats, med Sourceful Energy-appen. Har mätaren bara ett RJ45 HAN-uttag: använd <b>Zap HAN</b>.",
        "before": "Innan du åker",
        "p1_t": "P1/HAN påslagen", "p1_d": "Hos elnätsbolaget, före besöket.",
        "wifi_t": "Wifi, bara 2,4&nbsp;GHz", "wifi_d": "Nätnamn och lösenord.",
        "app_t": "Appen och Bluetooth", "app_d": "Sourceful Energy, inloggad.",
        "cable_t": "RJ12-kabeln", "cable_d": "Följer med Zap.",
        "meter": "ELMÄTARE", "reading": "12 345,6", "pins": "6 STIFT · CA 9,5 MM",
        "zap_above": "ZAP OVANIFRÅN", "out": "P1 UT", "rs485": "RS485", "button": "KNAPP",
        "status": "STATUS", "in": "P1 IN", "usbc": "USB-C",
        "lights": "LAMPORNA",
        "rows": [
            (GREEN, "Grön", "I IN", "solid", "Ström"),
            (BLUE, "Blå", "STATUS", "solid", "Väntar på appen"),
            (BLUE, "Blå", "STATUS", "fast", "Wifi rensat, Bluetooth"),
            (GREEN, "Grön", "I UT", "ten", "Mätardata, ~10 s"),
            (BLUE, "Blå", "STATUS", "off", "Släckt: igång"),
        ],
        "s1_h": "Hitta porten",
        "s1_p": "Det lilla uttaget, som ett gammalt telefonjack. Märkt <b>P1</b>, <b>Customer</b>, <b>User</b> eller <b>RJ12</b>, ibland <b>HAN</b>. Sex stift. Ofta bakom ett lock.",
        "s1_warn": "Åtta stift är fel uttag, även om det står HAN. <b>Tvinga aldrig i kabeln.</b>",
        "s2_h": "Koppla in",
        "s2_p": "Kabeln sitter redan i Zappens <b>P1 IN</b>, på långsidan med USB-C. Sätt andra änden i mätaren tills den klickar. Zap tar ström från mätaren.",
        "s2_q": "USB-C bara om mätaren inte matar, wifin är svag, eller P1 UT används.",
        "s3_h": "Kolla lamporna",
        "s3_p1": "Grön i IN, fast: ström. Blå, fast: Zap väntar på appen.",
        "s3_p2": "Ingen grön: kolla kabeln eller mata med USB-C. Ingen blå: håll knappen 5–10&nbsp;s tills den blinkar snabbt, släpp.",
        "s4_h": "I appen", "s4_micro": "Sourceful Energy &middot; mainnet",
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
        "ok_data_q": "Grön i UT", "ok_data": "Blinkar ungefär var 10:e s när mätaren är tillagd.",
        "ok_wifi_q": "Blå släckt", "ok_wifi": "En minut efter att wifi är uppe. Bluetooth har stängt.",
        "ok_app": "Appen visar mätardata inom 2 min",
        "ifnot": "Om inte",
        "nd_q": "Ingen data-blink",
        "nd": "Är mätaren tillagd (4.6)? Då är porten oftast inte påslagen, eller så sitter kabeln fel.",
        "nw_q": "Appen: Kan inte nå Zap", "nw": "Wifi nås inte. Bättre täckning, eller gör om wifi.",
        "hang_q": "Verkar hängd", "hang": "Håll knappen 2–5&nbsp;s, släpp. Zap startar om.",
        "wifi_h": "Byta wifi",
        "wifi_p": "Håll knappen 5–10&nbsp;s (snabb blå blink), släpp. Sedan:<br>",
        "wifi_path": ["<b>Mina Zappar</b>", "Zappen", "<b>Konfigurera om WiFi</b>", "välj&nbsp;den", "<b>Konfigurera Nätverk</b>", "nät, lösenord", "<b>Anslut</b>"],
        "inv_h": "Sen &middot; växelriktare",
        "inv": "Modell som stöds, fast IP, samma nät. <b>Mer → Energienheter → Lägg till energienhet</b>: typ, modell, IP, port, enhets-ID.",
        "saj_k": "Inte i appen",
        "saj1": "<b>SAJ finns inte i mainnet-appen.</b> Lägg inte till den som en annan växelriktare.",
        "saj2": "Zap ska ha <b>internet</b>, och sitta på <b>samma LAN</b> som SAJ eller vara seriellt kopplad till den.",
        "saj3": "Integrationen gör <b>Sourceful</b>, inte installatören. Ungefär en halv dag när det är på plats.",
        "foot1": "support.sourceful.energy &middot; underlag 2026-06-02",
        "foot2": "RJ12-uttaget efter Open Connector Graphics, Wikke Andeweg, CC BY 4.0",
    },
    "en": {
        "title": "Connect a Zap",
        "rail": "Installation guide &middot; Zap P1 &middot; Mainnet",
        "lede": "For the installer, on site, with the Sourceful Energy app. Meter with only an RJ45 HAN port: use <b>Zap HAN</b>.",
        "before": "Before you go",
        "p1_t": "P1/HAN port enabled", "p1_d": "By the grid operator, beforehand.",
        "wifi_t": "Wi-Fi, 2.4&nbsp;GHz only", "wifi_d": "Network name and password.",
        "app_t": "App and Bluetooth", "app_d": "Sourceful Energy, signed in.",
        "cable_t": "The RJ12 cable", "cable_d": "Comes with the Zap.",
        "meter": "ELECTRICITY METER", "reading": "12,345.6", "pins": "6 PINS · ABOUT 9.5 MM",
        "zap_above": "ZAP FROM ABOVE", "out": "P1 OUT", "rs485": "RS485", "button": "BUTTON",
        "status": "STATUS", "in": "P1 IN", "usbc": "USB-C",
        "lights": "THE LIGHTS",
        "rows": [
            (GREEN, "Green", "IN", "solid", "Power"),
            (BLUE, "Blue", "STATUS", "solid", "Waiting for the app"),
            (BLUE, "Blue", "STATUS", "fast", "Wi-Fi cleared, Bluetooth"),
            (GREEN, "Green", "OUT", "ten", "Meter data, ~10 s"),
            (BLUE, "Blue", "STATUS", "off", "Off: running"),
        ],
        "s1_h": "Find the port",
        "s1_p": "The small socket, like an old phone jack. Labelled <b>P1</b>, <b>Customer</b>, <b>User</b> or <b>RJ12</b>, sometimes <b>HAN</b>. Six pins. Often behind a cover.",
        "s1_warn": "Eight pins is the wrong socket, even if it says HAN. <b>Never force the cable.</b>",
        "s2_h": "Plug in",
        "s2_p": "The cable is already in the Zap's <b>P1 IN</b>, on the long side with USB-C. Push the other end into the meter until it clicks. The meter powers the Zap.",
        "s2_q": "USB-C only if the meter gives no power, the Wi-Fi is weak, or P1 OUT is in use.",
        "s3_h": "Check the lights",
        "s3_p1": "Green in IN, solid: power. Blue, solid: the Zap is waiting for the app.",
        "s3_p2": "No green: check the cable or use USB-C. No blue: hold the button 5–10&nbsp;s until it blinks fast, let go.",
        "s4_h": "In the app", "s4_micro": "Sourceful Energy &middot; mainnet",
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
        "ok_data_q": "Green in OUT", "ok_data": "Blinks about every 10 s once the meter is added.",
        "ok_wifi_q": "Blue off", "ok_wifi": "A minute after Wi-Fi is up. Bluetooth has closed.",
        "ok_app": "Meter data in the app within 2 min",
        "ifnot": "If not",
        "nd_q": "No data blink",
        "nd": "Is the meter added (4.6)? Then the port is usually not enabled, or the cable is wrong.",
        "nw_q": "App: Unable to reach Zap", "nw": "No Wi-Fi. Better coverage, or redo the Wi-Fi.",
        "hang_q": "Seems stuck", "hang": "Hold the button 2–5&nbsp;s, let go. The Zap restarts.",
        "wifi_h": "Change Wi-Fi",
        "wifi_p": "Hold the button 5–10&nbsp;s (fast blue blink), let go. Then:<br>",
        "wifi_path": ["<b>My Zaps</b>", "the Zap", "<b>Reconfigure WiFi</b>", "pick&nbsp;it", "<b>Configure network</b>", "network, password", "<b>Connect</b>"],
        "inv_h": "Then &middot; inverter",
        "inv": "Supported model, fixed IP, same network. <b>More → Energy devices → Add Energy Device</b>: type, model, IP, port, unit ID.",
        "saj_k": "Not in the app",
        "saj1": "<b>SAJ is not in the mainnet app.</b> Do not add it as another inverter.",
        "saj2": "The Zap needs <b>internet</b>, and must be on the <b>same LAN</b> as the SAJ or connected to it by serial.",
        "saj3": "<b>Sourceful</b> does the integration, not the installer. About half a day once that is in place.",
        "foot1": "support.sourceful.energy &middot; sources 2026-06-02",
        "foot2": "RJ12 jack after Open Connector Graphics, Wikke Andeweg, CC BY 4.0",
    },
}


def zap_top(o, t, zx, zy, han=False):
    """The Zap from above, at about 1:1 (RJ12 is ~24 % of the 56 mm long side).

    Lower long side = IN side; upper long side = OUT side, mirrored as seen from above.
    The Zap HAN (han=True) has the same box and sockets but no separate blue status
    light: the light in its RJ12 IN socket is an RGB light that does that job (David,
    2026-10-15).
    """
    zw, zh = 56, 42.7
    zb = zy + zh
    X = lambda f: zx + f * zw
    o.append(f'<text x="{zx + zw / 2}" y="{zy - 3.9}" text-anchor="middle" {MONO} font-size="2.2" '
             f'letter-spacing="0.35" fill="{MUTED}">{t["zap_above"]}</text>')
    o.append(f'<rect x="{X(0.249) - 4.8:.2f}" y="{zb - 0.6:.2f}" width="9.6" height="6.6" rx="0.9" '
             f'fill="{PLASTIC}" stroke="{INK}" stroke-width="0.25"/>')
    o.append(f'<rect x="{X(0.249) - 1.5:.2f}" y="{zb + 6:.2f}" width="3" height="2.2" rx="0.5" fill="#BDB8AA"/>')
    o.append(f'<rect x="{zx}" y="{zy}" width="{zw}" height="{zh}" rx="5.6" fill="{INK}"/>')
    o.append(f'<rect x="{zx + 2.2}" y="{zy + 2.2}" width="{zw - 4.4}" height="{zh - 4.4}" rx="3.8" fill="#1F1F1E"/>')
    s = 0.3
    o.append(f'<path d="{BOLT}" fill="{CREAM}" transform="translate({zx + zw / 2 - 22.8 * s:.2f},'
             f'{zy + zh / 2 - 23.3 * s:.2f}) scale({s})"/>')
    lab = f'{MONO} font-size="2" letter-spacing="0.25" fill="#B9B6AA" text-anchor="middle"'
    tick = lambda x, y1, y2: o.append(f'<line x1="{x:.2f}" y1="{y1:.2f}" x2="{x:.2f}" y2="{y2:.2f}" '
                                      f'stroke="#6E6C66" stroke-width="0.2"/>')
    edge = lambda f, w, y, color, rx=0.4: o.append(
        f'<rect x="{X(f) - w / 2:.2f}" y="{y - 0.8:.2f}" width="{w}" height="1.6" rx="{rx}" fill="{color}"/>')
    # upper long side, the OUT side
    edge(0.286, 13.4, zy, "#55534F")
    edge(0.540, 13.4, zy, "#5E8F66", 0.2)
    o.append(f'<rect x="{X(0.761) - 3:.2f}" y="{zy - 0.8:.2f}" width="6" height="1.6" rx="0.8" '
             f'fill="{INK}" stroke="#8C8A80" stroke-width="0.25"/>')
    tick(X(0.540), zy + 1, zy + 4.2)
    tick(X(0.761), zy + 1, zy + 4.2)
    o.append(f'<text x="{X(0.286):.2f}" y="{zy + 6.4:.2f}" {lab}>{t["out"]}</text>')
    o.append(f'<text x="{X(0.540):.2f}" y="{zy + 6.4:.2f}" {lab}>{t["rs485"]}</text>')
    o.append(f'<text x="{X(0.761):.2f}" y="{zy + 6.4:.2f}" {lab}>{t["button"]}</text>')
    if not han:
        o.append(f'<circle cx="{X(0.286):.2f}" cy="{zy + 2.6:.2f}" r="0.85" fill="{GREEN}"/>')
        o.append(f'<circle cx="{X(0.849):.2f}" cy="{zy + 2.6:.2f}" r="0.85" fill="{BLUE}"/>')
        tick(X(0.849), zy + 3.6, zy + 7.4)
        o.append(f'<text x="{X(0.849):.2f}" y="{zy + 9.6:.2f}" {lab}>{t["status"]}</text>')
    # lower long side, the IN side
    edge(0.249, 13.4, zb, "#55534F")
    edge(0.466, 9.4, zb, "#8C8A80", 0.8)
    if han:   # the RGB light in the RJ12 socket
        for i, c in enumerate(("#E5484D", "#F2D53C", "#30A46C", "#3E63DD")):
            o.append(f'<circle cx="{X(0.249) - 1.6 + i * 1.07:.2f}" cy="{zb - 2.6:.2f}" r="0.5" fill="{c}"/>')
    else:
        o.append(f'<circle cx="{X(0.249):.2f}" cy="{zb - 2.6:.2f}" r="0.85" fill="{GREEN}"/>')
    tick(X(0.466), zb - 1, zb - 4.2)
    o.append(f'<text x="{X(0.249):.2f}" y="{zb - 4.8:.2f}" {lab}>{t["in"]}</text>')
    o.append(f'<text x="{X(0.466):.2f}" y="{zb - 4.8:.2f}" {lab}>{t["usbc"]}</text>')


def hero(t, export=False):
    W, H = 186, 64.5
    o = [f'<svg class="hero" viewBox="0 0 {W} {H}" style="height:{H}mm" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    if not export:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')

    # meter
    o.append(f'<rect x="8" y="7" width="38" height="52" rx="3.2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="12" y="12.6" {MONO} font-size="2.2" letter-spacing="0.35" fill="{MUTED}">{t["meter"]}</text>')
    o.append(f'<rect x="12" y="14.6" width="30" height="9" rx="1.2" fill="#ECE8DA"/>')
    o.append(f'<text x="14.4" y="20.6" {MONO} font-size="3.9" fill="{INK}">{t["reading"]}</text>')
    o.append(f'<text x="35.4" y="20.6" {MONO} font-size="1.9" fill="{MUTED}">kWh</text>')
    o.append(f'<circle cx="13.4" cy="28" r="0.9" fill="{INK}"/>')
    o.append(f'<text x="15.6" y="28.6" {MONO} font-size="1.7" fill="{MUTED}">1000 imp/kWh</text>')
    jg, _, _ = jack_g(23.15, 34.2, 0.6)
    o.append(jg)
    o.append(f'<rect x="23.5" y="36.6" width="7" height="4.9" rx="0.9" fill="{PLASTIC}" stroke="{INK}" stroke-width="0.25"/>')
    o.append(f'<rect x="25.4" y="37.6" width="3.2" height="1.1" rx="0.4" fill="#BDB8AA"/>')
    o.append(f'<text x="12" y="39.6" {MONO} font-size="2.2" letter-spacing="0.2" fill="{INK}" font-weight="700">P1/HAN</text>')

    # cable: meter -> P1 IN, into the Zap's lower long side from below
    o.append(f'<path d="M27 41.4 V56 C27 59.8 29.4 61.8 33.2 61.8 H99 C100.9 61.8 101.9 61.2 101.9 60.2" '
             f'fill="none" stroke="{INK}" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"/>')

    # magnifier over the port
    o.append('<defs><clipPath id="lupp"><circle cx="62" cy="21" r="14"/></clipPath></defs>')
    o.append(f'<line x1="30.6" y1="35.4" x2="50.4" y2="28.6" stroke="{INK}" stroke-width="0.25"/>')
    o.append('<circle cx="62" cy="21" r="14" fill="#FFFFFF"/>')
    big, _, _ = jack_g(62 - 12.85 * 0.85, 21 - 12.4 * 0.85, 1.7, frame=False)
    o.append(f'<g clip-path="url(#lupp)">{big}</g>')
    o.append(f'<circle cx="62" cy="21" r="14" fill="none" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="62" y="40.4" text-anchor="middle" font-size="3.6" font-weight="700" fill="{INK}">RJ12</text>')
    o.append(f'<text x="62" y="44.1" text-anchor="middle" {MONO} font-size="2.1" letter-spacing="0.2" fill="{MUTED}">{t["pins"]}</text>')

    zap_top(o, t, 88, 9.5)

    # the lights
    lx = 153.5
    o.append(f'<text x="{lx + 5}" y="12.6" {MONO} font-size="2.2" letter-spacing="0.35" fill="{MUTED}">{t["lights"]}</text>')
    y = 17.4
    for color, name, where, kind, mean in t["rows"]:
        o.append(f'<circle cx="{lx + 1}" cy="{y - 0.85}" r="1" fill="{color}"/>')
        o.append(f'<text x="{lx + 3.2}" y="{y}" font-size="2.7" font-weight="500" fill="{INK}">{name} '
                 f'<tspan {MONO} font-size="1.8" letter-spacing="0.2" fill="{MUTED}">{where}</tspan></text>')
        o.append(f'<g transform="translate({lx + 19.5},{y - 2})">{pattern(kind, color)}</g>')
        o.append(f'<text x="{lx + 3.2}" y="{y + 3.3}" font-size="2.45" fill="#33363C">{mean}</text>')
        y += 8.4

    for n, (cx, cy) in enumerate(((50.6, 9.4), (62, 61.8), (lx + 1.6, 11.9)), 1):
        if not export:
            o.append(marker(n, cx, cy))
    o.append('</svg>')
    return "".join(o)


EXTRA_CSS = """
.path{line-height:1.45;}
.sub.later{margin-top:2.4mm;}
.list li{padding:1.25mm 0;}
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
        <div><span class="chip">{{IC_WIFI}}</span><div><div class="t">{{wifi_t}}</div><div class="d">{{wifi_d}}</div></div></div>
        <div><span class="chip">{{IC_PHONE}}</span><div><div class="t">{{app_t}}</div><div class="d">{{app_d}}</div></div></div>
        <div><span class="chip">{{IC_CABLE}}</span><div><div class="t">{{cable_t}}</div><div class="d">{{cable_d}}</div></div></div>
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
          <li><span class="q">{{PAT_DATA}} {{ok_data_q}}</span>{{ok_data}}</li>
          <li><span class="q">{{PAT_WIFI}} {{ok_wifi_q}}</span>{{ok_wifi}}</li>
          <li><span class="q">{{TICK}} {{ok_app}}</span></li>
        </ul>
      </div>
      <div>
        <div class="sub">{{ifnot}}</div>
        <ul class="list">
          <li><span class="q">{{nd_q}}</span>{{nd}}</li>
          <li><span class="q">{{PAT_NONE}} {{nw_q}}</span>{{nw}}</li>
          <li><span class="q">{{PAT_RESTART}} {{hang_q}}</span>{{hang}}</li>
        </ul>
      </div>
      <div>
        <div class="sub">{{wifi_h}}</div>
        <p class="small">{{wifi_p}}</p>
        <div class="path">{{WIFI_PATH}}</div>
        <div class="sub later">{{inv_h}}</div>
        <p class="small">{{inv}}</p>
      </div>
    </div>
  </section>

  <div class="bottom">
    <section class="saj">
      <div><div class="k">SAJ</div><div class="micro">{{saj_k}}</div></div>
      <p>{{saj1}}</p>
      <p>{{saj2}}</p>
      <p>{{saj3}}</p>
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
    values["rail"] = rail(lang, t["rail"], FIELD_TESTED)
    values.update({
        "LOGO": LOGO_LIGHT, "IC_METER": IC_METER, "IC_WIFI": IC_WIFI, "IC_PHONE": IC_PHONE,
        "IC_CABLE": IC_CABLE, "HERO": hero(t), "APP_TRACK": track, "TICK": TICK,
        "WIFI_PATH": arrow.join(t["wifi_path"]),
        "PAT_DATA": pattern_svg("ten", GREEN), "PAT_WIFI": pattern_svg("off", BLUE),
        "PAT_NONE": "", "PAT_RESTART": pattern_svg("slow", BLUE),
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)


# Standalone drawings for assets/devices/, cut out of the hero (English labels).
DEVICES = {"zap-p1": (84, 1, 64, 62)}


def devices():
    return {name: crop(hero(T["en"], export=True), box) for name, box in DEVICES.items()}
