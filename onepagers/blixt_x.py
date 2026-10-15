"""Blixt X one-pager: set up a Blixt X (gateway software 2.0.1, the release in the field).

Hardware: the RAK Hotspot V2 (Sourceful ENERGY edition, the former dual miners), drawn from
RAK's datasheet (docs.rakwireless.com/product-categories/wisgate/rak-hotspot-v2/datasheet):
92 x 68.3 x 57.2 mm, black aluminium with heat-sink fins. Long side: USB-C power (5 V / 2.4 A)
and the pairing button. Front: LoRa RP-SMA antenna, TF card slot, red (power) and green
(activity) LEDs. Back: Gigabit Ethernet. No RS-485 or P1 port.

Software facts from srcfl/srcful-blixt-x-firmware at d501e798 (2.0.1) and the app 2.7.9:
- BLE name blixt-<serial>, advertising 3 min after start; the button (GPIO 7, RAK's
  pairing button) held 3 s or double-clicked reopens 3 min.
- Local API on port 80 at blixt.local (blixt-<suffix>.local on a clash);
  /api/network has internetConnected and mqttConnected.
- 2.0.1 does not report Ethernet, so the app never offers Skip WiFi setup.
- The app onboards it with the Zap flow; every screen says "Zap".
"""
from common import (crop, BLUE, BOLT, CREAM, IC_LIST, IC_PHONE, IC_WIFI, INK, LOGO_LIGHT, MONO,
                    MUTED, SIGNAL, TICK, fill, icon, marker, page)

IC_PLUG = icon('<path d="M9 3v5M15 3v5"/><path d="M6 8h12v3a6 6 0 0 1-12 0z"/><path d="M12 17v4"/>')
IC_NET = icon('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>')

T = {
    "sv": {
        "title": "Sätt upp en Blixt X",
        "rail": "Kom igång &middot; Blixt X 2.0.1 &middot; RAK Hotspot V2",
        "lede": "För ägaren eller installatören. Blixt X är vår programvara på RAK-gatewayen, de gamla dual-minrarna. Den sätts upp i appen som en Zap.",
        "before": "Innan du börjar",
        "net_t": "Ethernet", "net_d": "Med internet. Wifi är valfritt.",
        "app_t": "Appen, inloggad", "app_d": "Med profil och anläggning.",
        "dev_t": "Enhetslista", "dev_d": "Modell, IP, port, unit-id.",
        "bt_t": "Strömadaptern", "bt_d": "USB-C, 5 V, 2,4 A.",
        "phone": "Appen", "v_side": "SIDAN", "v_front": "FRAMSIDAN", "v_back": "BAKSIDAN",
        "usbc": "USB-C 5 V", "pair": "PAIRING-KNAPP", "leds": "LAMPOR", "leds_sub": "röd ström · grön aktivitet",
        "eth": "ETHERNET", "cloud": "Sourceful", "cloud_sub": "MAINNET",
        "tcp": "Växelriktare", "tcp_sub": "MODBUS TCP",
        "s1_h": "Starta",
        "s1_p": "Antennen på. Ethernet i baksidan. Ström i USB-C på sidan. Wifi är valfritt och inte rekommenderat.",
        "s1_q": "Röd lampa fast: ström. Grön blinkar när systemet arbetar.",
        "s2_h": "Bluetooth-fönstret",
        "s2_p": "Efter start syns den som <b>blixt-&lt;serie&gt;</b> i <b>3 minuter</b>.",
        "s2_q": "Missat fönstret: håll <b>pairing-knappen</b> 3&nbsp;s eller dubbelklicka, eller starta om.",
        "s3_h": "Koppla enheterna",
        "s3_p": "Modbus TCP på samma nät, med fast IP. RAK-gatewayen har ingen RS-485- eller P1-port.",
        "s3_q": "En Modbus-master per enhet. Stäng andra system som läser den.",
        "s4_h": "I appen", "s4_micro": "Samma flöde som Zap",
        "app_steps": [
            ("<b>Lägg till en ny Zap</b>", "Under <b>Kom igång</b>, eller <b>Mer → Mina Zappar</b>. Appen säger Zap."),
            ("Välj <b>blixt-…</b>", "Inom 3 minuter efter start. Flest staplar om du ser flera."),
            ("<b>Registrera &amp; konfigurera nätverk</b>", "Gatewayen hamnar i profilen du har vald."),
            ("Wifi-steget", "Med Ethernet: tryck tillbaka. Den är redan registrerad."),
            ("Utan kabel", "Nät, lösenord, <b>Anslut</b>, sedan <b>Klar</b>."),
            ("Enheter", "<b>Mer → Energienheter</b>, sedan typ, modell, IP, port och enhets-ID."),
        ],
        "s5_h": "Klart när",
        "seen": "Det här syns",
        "ok1_q": "<code>internetConnected: true</code>", "ok1": "Och <code>mqttConnected: true</code> på <b>http://blixt.local/api/network</b> från samma nät.",
        "ok2_q": "<code>/api/devices</code>", "ok2": "Listar enheterna du lade till.",
        "ok3_q": "Appen", "ok3": "Visar data från enheterna.",
        "ifnot": "Om inte",
        "f1_q": "Syns inte i appen", "f1": "Bluetooth-fönstret har stängt. Tryck pairing-knappen, eller starta om.",
        "f2_q": "Röd lampa blinkar", "f2": "Strömförsörjningen räcker inte. Använd en adapter på 5 V, 2,4 A.",
        "f3_q": "<code>mqttConnected: false</code>", "f3": "Ingen internetåtkomst. Kontrollera nätet och brandväggen.",
        "f4_q": "En enhet svarar inte", "f4": "Fel IP, port eller unit-id, Modbus TCP avstängt, eller en annan master.",
        "know_h": "Bra att veta",
        "k1_q": "Appen säger Zap", "k1": "Varje skärm säger Zap. Det är rätt flöde.",
        "k3_q": "Wifi-steget på Ethernet", "k3": "2.0.1 rapporterar inte Ethernet, så appen visar steget ändå. Backa ur det.",
        "card_k": "3.0.0", "card_m": "Nästa version",
        "card1": "<b>Den här sidan gäller 2.0.1</b>, versionen som körs i fält i oktober 2026.",
        "card2": "I 3.0.0 läggs enheter till med drivrutiner från Sourcefuls register. Sidan uppdateras när den släpps.",
        "foot1": "blixt-x 2.0.1 d501e798 &middot; appen 2.7.9 &middot; RAK datablad &middot; verifierad 2026-10-15",
        "foot2": "Skala 0,4 &middot; portarna enligt RAK",
    },
    "en": {
        "title": "Set up a Blixt X",
        "rail": "Getting started &middot; Blixt X 2.0.1 &middot; RAK Hotspot V2",
        "lede": "For the owner or installer. Blixt X is our software on the RAK gateway, the former dual miners. It is set up in the app like a Zap.",
        "before": "Before you start",
        "net_t": "Ethernet", "net_d": "With internet. Wi-Fi is optional.",
        "app_t": "The app, signed in", "app_d": "With a profile and a site.",
        "dev_t": "Device list", "dev_d": "Model, IP, port, unit ID.",
        "bt_t": "The power adapter", "bt_d": "USB-C, 5 V, 2.4 A.",
        "phone": "The app", "v_side": "SIDE", "v_front": "FRONT", "v_back": "BACK",
        "usbc": "USB-C 5 V", "pair": "PAIRING BUTTON", "leds": "LIGHTS", "leds_sub": "red power · green activity",
        "eth": "ETHERNET", "cloud": "Sourceful", "cloud_sub": "MAINNET",
        "tcp": "Inverter", "tcp_sub": "MODBUS TCP",
        "s1_h": "Start",
        "s1_p": "Antenna on. Ethernet in the back. Power in the USB-C on the side. Wi-Fi is optional and not recommended.",
        "s1_q": "Red light solid: power. Green blinks while the system works.",
        "s2_h": "The Bluetooth window",
        "s2_p": "After start it shows up as <b>blixt-&lt;serial&gt;</b> for <b>3 minutes</b>.",
        "s2_q": "Missed it: hold the <b>pairing button</b> 3&nbsp;s or double-click, or restart it.",
        "s3_h": "Connect the devices",
        "s3_p": "Modbus TCP on the same network, with a fixed IP. The RAK gateway has no RS-485 or P1 port.",
        "s3_q": "One Modbus master per device. Stop other systems that read it.",
        "s4_h": "In the app", "s4_micro": "Same flow as Zap",
        "app_steps": [
            ("<b>Onboard a new Zap</b>", "Under <b>Get started</b>, or <b>More → My Zaps</b>. The app says Zap."),
            ("Pick <b>blixt-…</b>", "Within 3 minutes of start. Most bars if you see several."),
            ("<b>Claim &amp; Configure network</b>", "The gateway joins the profile you have selected."),
            ("The Wi-Fi step", "On Ethernet: tap back. It is already registered."),
            ("No cable", "Network, password, <b>Connect</b>, then <b>Done</b>."),
            ("Devices", "<b>More → Energy devices</b>, then type, model, IP, port and unit ID."),
        ],
        "s5_h": "Done when",
        "seen": "You see this",
        "ok1_q": "<code>internetConnected: true</code>", "ok1": "And <code>mqttConnected: true</code> at <b>http://blixt.local/api/network</b> from the same network.",
        "ok2_q": "<code>/api/devices</code>", "ok2": "Lists the devices you added.",
        "ok3_q": "The app", "ok3": "Shows data from the devices.",
        "ifnot": "If not",
        "f1_q": "Not in the app", "f1": "The Bluetooth window closed. Press the pairing button, or restart.",
        "f2_q": "Red light blinks", "f2": "The power supply is too weak. Use a 5 V, 2.4 A adapter.",
        "f3_q": "<code>mqttConnected: false</code>", "f3": "No internet access. Check the network and the firewall.",
        "f4_q": "A device does not answer", "f4": "Wrong IP, port or unit ID, Modbus TCP off, or another master.",
        "know_h": "Good to know",
        "k1_q": "The app says Zap", "k1": "Every screen says Zap. It is the right flow.",
        "k3_q": "The Wi-Fi step on Ethernet", "k3": "2.0.1 does not report Ethernet, so the app shows the step anyway. Back out of it.",
        "card_k": "3.0.0", "card_m": "Next version",
        "card1": "<b>This page covers 2.0.1</b>, the version running in the field in October 2026.",
        "card2": "In 3.0.0, devices are added with drivers from Sourceful's registry. This page changes when it ships.",
        "foot1": "blixt-x 2.0.1 d501e798 &middot; app 2.7.9 &middot; RAK datasheet &middot; verified 2026-10-15",
        "foot2": "Scale 0.4 &middot; ports as in RAK's datasheet",
    },
}

EXTRA_CSS = """
h1{font-size:29pt;}
code{font-family:'JetBrains Mono',monospace;font-size:0.88em;}
.know{padding-top:2.4mm;}
.hero.bx{height:50mm;}
.cols2{display:flex;gap:6mm;}
.cols2 > div{flex:none;width:90mm;}
"""


def hero(t, export=False):
    W, H = 186, 50
    o = [f'<svg class="hero bx" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    if not export:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')
    line = lambda d, w=1.0, c=INK, dash="": o.append(
        f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
        f'stroke-linejoin="round"{f" stroke-dasharray={chr(34)}{dash}{chr(34)}" if dash else ""}/>')
    label = lambda x, y, s, size=1.9, c=MUTED, anchor="middle", weight="400": o.append(
        f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="0.25" fill="{c}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
    BODY, PANEL, FIN = "#2B2B2A", "#1C1D1F", "#3A3A38"
    GOLD, RED, GRN = "#B8892E", "#C8372D", "#15803D"
    k = 0.4                     # drawing scale, mm per real mm: 92 x 68.3 x 57.2
    L, D, Hh = 92 * k, 68.3 * k, 57.2 * k
    y0 = 13

    def fins(x, w):
        o.append(f'<rect x="{x}" y="{y0}" width="{w}" height="2.2" fill="{BODY}"/>')
        n = int(w // 2.6)
        for i in range(n):
            o.append(f'<rect x="{x + 0.8 + i * 2.6:.2f}" y="{y0 - 1.4}" width="1.3" height="1.6" fill="{BODY}"/>')

    # phone and the Bluetooth link
    o.append(f'<rect x="6" y="{y0}" width="12" height="21" rx="2.6" fill="#FFFFFF" stroke="{INK}" stroke-width="0.5"/>')
    o.append(f'<rect x="10" y="{y0 + 18}" width="4" height="0.7" rx="0.35" fill="{INK}"/>')
    label(12, y0 + 26, t["phone"], 2, INK, weight="700")

    # side: USB-C and the pairing button, antenna on the left end
    sx = 30
    label(sx + L / 2, y0 - 4, t["v_side"], 1.9, MUTED)
    o.append(f'<rect x="{sx - 2.6}" y="{y0 + 4}" width="2.8" height="2.2" rx="0.3" fill="{GOLD}"/>')
    fins(sx, L)
    o.append(f'<rect x="{sx}" y="{y0 + 1.6}" width="{L}" height="{Hh - 1.6}" rx="1.2" fill="{BODY}"/>')
    o.append(f'<rect x="{sx + 1.6}" y="{y0 + 3.4}" width="{L * 0.72:.2f}" height="{Hh - 6:.2f}" rx="0.6" fill="{PANEL}"/>')
    bx, by = sx + 10.5, y0 + 10.5
    o.append(f'<circle cx="{bx}" cy="{by}" r="1.7" fill="#2F3134" stroke="#55575B" stroke-width="0.3"/>')
    ux, uy = sx + 4.2, y0 + 15.6
    o.append(f'<rect x="{ux - 1.8}" y="{uy - 0.6}" width="3.6" height="1.3" rx="0.65" fill="none" stroke="#8C8A80" stroke-width="0.3"/>')
    line(f"M{ux} {uy + 1} V{y0 + Hh + 3}", 0.25, MUTED)
    label(ux, y0 + Hh + 5.2, t["usbc"], 1.8, INK, weight="700")
    line(f"M{bx} {by + 2} V{y0 + Hh + 7}", 0.25, MUTED)
    label(bx + 1, y0 + Hh + 9.2, t["pair"], 1.8, INK, weight="700")
    if not export:
        line(f"M18 {y0 + 9} H{bx - 2.4}", 0.6, BLUE, "1.2 1.2")
        label(22.5, y0 + 6.8, "BLE", 1.8, BLUE, weight="700")

    # front: antenna, TF slot, LEDs
    fx = sx + L + 9
    label(fx + D / 2, y0 - 4, t["v_front"], 1.9, MUTED)
    fins(fx, D)
    o.append(f'<rect x="{fx}" y="{y0 + 1.6}" width="{D}" height="{Hh - 1.6}" rx="1.2" fill="{BODY}"/>')
    o.append(f'<circle cx="{fx + 5}" cy="{y0 + 6}" r="1.7" fill="{GOLD}"/><circle cx="{fx + 5}" cy="{y0 + 6}" r="0.6" fill="#7A5A1E"/>')
    for cx, cy in ((fx + D - 5, y0 + 6), (fx + 5, y0 + 12.4), (fx + D - 5, y0 + 12.4)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="1.9" fill="{FIN}"/>')
    o.append(f'<rect x="{fx + D / 2 - 3.4}" y="{y0 + 15.6}" width="6.8" height="1.8" rx="0.4" fill="{PANEL}" stroke="#55575B" stroke-width="0.25"/>')
    lx, ly = fx + D - 6.2, y0 + 16.2
    o.append(f'<circle cx="{lx}" cy="{ly}" r="0.55" fill="{RED}"/><circle cx="{lx + 1.6}" cy="{ly}" r="0.55" fill="{GRN}"/>')
    line(f"M{lx + 0.8} {ly + 1} V{y0 + Hh + 3}", 0.25, MUTED)
    label(lx + 0.8, y0 + Hh + 5.2, t["leds"], 1.8, INK, weight="700")
    label(lx + 0.8, y0 + Hh + 7.6, t["leds_sub"], 1.6)

    # back: Ethernet
    ex = fx + D + 9
    label(ex + D / 2, y0 - 4, t["v_back"], 1.9, MUTED)
    fins(ex, D)
    o.append(f'<rect x="{ex}" y="{y0 + 1.6}" width="{D}" height="{Hh - 1.6}" rx="1.2" fill="{BODY}"/>')
    for i in range(2):
        o.append(f'<rect x="{ex + 3 + i * 6.4}" y="{y0 + 10.5}" width="5" height="5" rx="0.5" fill="{PANEL}" stroke="#44464A" stroke-width="0.2"/>')
    jx, jy = ex + D - 9.5, y0 + 10.2
    o.append(f'<rect x="{jx}" y="{jy}" width="6.4" height="5.4" rx="0.3" fill="#9A9890"/>')
    o.append(f'<path d="M{jx + 1} {jy + 1} H{jx + 5.4} V{jy + 4} H{jx + 4.2} V{jy + 4.8} H{jx + 2.2} V{jy + 4} H{jx + 1} Z" fill="{PANEL}"/>')
    line(f"M{jx + 3.2} {jy + 5.6} V{y0 + Hh + 3}", 0.25, MUTED)
    label(jx + 3.2, y0 + Hh + 5.2, t["eth"], 1.8, INK, weight="700")

    # network: Ethernet or Wi-Fi to Sourceful and the inverter
    nx = ex + D + 5
    line(f"M{jx + 6.4} {jy + 2.7} H{nx + 3}", 0.9)
    box = lambda y, a, b: (
        o.append(f'<rect x="{nx + 3}" y="{y}" width="{W - nx - 7}" height="11" rx="2.2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>'),
        o.append(f'<text x="{nx + 5.5}" y="{y + 4.8}" font-size="2.7" font-weight="500" fill="{INK}">{a}</text>'),
        label(nx + 5.5, y + 8.2, b, 1.6, MUTED, "start"))
    line(f"M{nx + 1} {jy + 2.7} V{y0 + 1} H{nx + 3}", 0.9)
    line(f"M{nx + 1} {jy + 2.7} V{y0 + 22} H{nx + 3}", 0.9)
    box(y0 - 4.5, t["cloud"], t["cloud_sub"])
    box(y0 + 16.5, t["tcp"], t["tcp_sub"])

    for n, (mx, my) in enumerate(((sx + L - 1.5, y0 + Hh - 1.5), (bx + 3.2, by - 3), (nx + 1, jy + 2.7)), 1):
        if not export:
            o.append(marker(n, mx, my))
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
        <div><span class="chip">{{IC_NET}}</span><div><div class="t">{{net_t}}</div><div class="d">{{net_d}}</div></div></div>
        <div><span class="chip">{{IC_PHONE}}</span><div><div class="t">{{app_t}}</div><div class="d">{{app_d}}</div></div></div>
        <div><span class="chip">{{IC_LIST}}</span><div><div class="t">{{dev_t}}</div><div class="d">{{dev_d}}</div></div></div>
        <div><span class="chip">{{IC_PLUG}}</span><div><div class="t">{{bt_t}}</div><div class="d">{{bt_d}}</div></div></div>
      </div>
    </div>
  </div>

  {{HERO}}

  <div class="steps3">
    <section>
      <div class="head"><span class="num">1</span><span class="h">{{s1_h}}</span></div>
      <p>{{s1_p}}</p>
      <p class="quiet">{{s1_q}}</p>
    </section>
    <section>
      <div class="head"><span class="num">2</span><span class="h">{{s2_h}}</span></div>
      <p>{{s2_p}}</p>
      <p class="quiet">{{s2_q}}</p>
    </section>
    <section>
      <div class="head"><span class="num">3</span><span class="h">{{s3_h}}</span></div>
      <p>{{s3_p}}</p>
      <p class="quiet">{{s3_q}}</p>
    </section>
  </div>

  <section class="sec">
    <div class="head"><span class="num">4</span><span class="h">{{s4_h}}</span><span class="micro">{{s4_micro}}</span></div>
    <ol class="track">{{APP_TRACK}}</ol>
  </section>

  <section class="sec">
    <div class="head"><span class="num">5</span><span class="h">{{s5_h}}</span></div>
    <div class="cols2">
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
          <li><span class="q">{{f4_q}}</span>{{f4}}</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="sec know">
    <div class="cols2">
      <div><div class="sub">{{know_h}}</div><p class="small"><b>{{k1_q}}.</b> {{k1}}</p></div>
      <div><div class="sub">&nbsp;</div><p class="small"><b>{{k3_q}}</b> {{k3}}</p></div>
    </div>
  </section>

  <div class="bottom">
    <section class="saj">
      <div><div class="k">{{card_k}}</div><div class="micro">{{card_m}}</div></div>
      <p>{{card1}}</p>
      <p>{{card2}}</p>
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
    values = {k: v for k, v in t.items() if isinstance(v, str)}
    values.update({
        "LOGO": LOGO_LIGHT, "IC_NET": IC_NET, "IC_PHONE": IC_PHONE, "IC_LIST": IC_LIST,
        "IC_PLUG": IC_PLUG, "HERO": hero(t), "APP_TRACK": track, "TICK": TICK,
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)


# Standalone drawings for assets/devices/, cut out of the hero (English labels).
DEVICES = {"blixt-x-rak-hotspot-v2": (26.5, 3, 114.5, 47)}


def devices():
    return {name: crop(hero(T["en"], export=True), box) for name, box in DEVICES.items()}
