"""Blixt X one-pager: set up a Blixt X (gateway software 2.0.1, the release in the field).

Facts from srcfl/srcful-blixt-x-firmware at d501e798 (2.0.1) and the Sourceful Energy app
2.7.9 (srcfl/srcful-flutter-app 9800165):
- BLE name blixt-<serial> (fallback BLIXT-<wlan MAC>), advertising 3 min after start;
  button (GPIO 7) held 3 s or double-clicked reopens 3 min (bluetooth/ble_service.py,
  gpioButton.py).
- Local API on port 80, mDNS blixt.local, blixt-<suffix>.local on a name clash
  (server/network/network_utils.py). /api/network has internetConnected and mqttConnected.
- 2.0.1 does not report Ethernet in /api/network, so the app never offers Skip WiFi setup.
- Modbus RTU defaults to /dev/ttyS0, the Pi 4 RS-485 UART (server/core/device_factory.py).
- The app onboards it with the Zap flow and labels; every screen says "Zap".
"""
from common import (BLUE, BOLT, CREAM, IC_LIST, IC_PHONE, IC_WIFI, INK, LOGO_LIGHT, MONO,
                    MUTED, SIGNAL, TICK, fill, icon, marker, page)

IC_NET = icon('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>')

T = {
    "sv": {
        "title": "Sätt upp en Blixt X",
        "rail": "Kom igång &middot; Blixt X 2.0.1 &middot; Mainnet",
        "lede": "För ägaren eller installatören. Blixt X kopplar växelriktare, batterier och mätare till Sourceful, och sätts upp i appen som en Zap.",
        "before": "Innan du börjar",
        "net_t": "Nätverk", "net_d": "Ethernet eller wifi med internet.",
        "app_t": "Appen, inloggad", "app_d": "Med profil och anläggning.",
        "dev_t": "Enhetslista", "dev_d": "Modell, IP, port, unit-id.",
        "bt_t": "Bluetooth på", "bt_d": "Stå nära gatewayen.",
        "gw": "BLIXT X", "gw_sub": "RASPBERRY PI 4", "bt_win": "BLUETOOTH · 3 MIN", "bt_name": "blixt-&lt;serie&gt;",
        "phone": "Appen", "net": "ETHERNET ELLER WIFI", "cloud": "Sourceful", "cloud_sub": "MAINNET",
        "tcp": "Växelriktare", "tcp_sub": "MODBUS TCP", "rtu": "Mätare / batteri", "rtu_sub": "RS-485 · RTU",
        "laptop": "Kontroll", "laptop_sub": "blixt.local/api/network",
        "s1_h": "Starta",
        "s1_p": "Ström på. Ethernet: koppla in kabeln. Wifi: ställs in i appen i steg 4.",
        "s1_q": "Blixt X har inga statuslampor att läsa av. Kontrollen görs i steg 5.",
        "s2_h": "Bluetooth-fönstret",
        "s2_p": "Efter start syns den som <b>blixt-&lt;serie&gt;</b> i <b>3 minuter</b>.",
        "s2_q": "Missat fönstret: håll knappen 3&nbsp;s eller dubbelklicka. Eller bryt strömmen och starta om.",
        "s3_h": "Koppla enheterna",
        "s3_p": "TCP-enheter på samma nät, med fast IP. RTU-enheter på gatewayens RS-485-port.",
        "s3_q": "En Modbus-master per enhet. Stäng andra system som läser den.",
        "s4_h": "I appen", "s4_micro": "Samma flöde som Zap",
        "app_steps": [
            ("<b>Lägg till en ny Zap</b>", "Under <b>Kom igång</b>, eller <b>Mer → Mina Zappar</b>. Appen säger Zap."),
            ("Välj <b>blixt-…</b>", "Inom 3 minuter efter start. Flest staplar om du ser flera."),
            ("<b>Registrera &amp; konfigurera nätverk</b>", "Gatewayen hamnar i profilen du har vald."),
            ("Wifi", "Nät, lösenord, <b>Anslut</b>. Dolt nät: <b>Ange manuellt</b>."),
            ("<b>Klar</b>", "Namnge den om du vill."),
            ("Enheter", "<b>Mer → Energienheter</b>, sedan typ, modell, IP, port och enhets-ID."),
        ],
        "s5_h": "Klart när",
        "seen": "Det här syns",
        "ok1_q": "<code>internetConnected: true</code>", "ok1": "Och <code>mqttConnected: true</code> på <b>http://blixt.local/api/network</b> från samma nät.",
        "ok2_q": "<code>/api/devices</code>", "ok2": "Listar enheterna du lade till.",
        "ok3_q": "Appen", "ok3": "Visar data från enheterna.",
        "ifnot": "Om inte",
        "f1_q": "Syns inte i appen", "f1": "Bluetooth-fönstret har stängt. Knappen eller en omstart öppnar det.",
        "f2_q": "<code>blixt.local</code> svarar inte", "f2": "Finns flera på nätet heter den <code>blixt-…local</code>. Eller använd IP-adressen.",
        "f3_q": "<code>mqttConnected: false</code>", "f3": "Ingen internetåtkomst. Kontrollera nätet och brandväggen.",
        "f4_q": "En enhet svarar inte", "f4": "Fel IP, port eller unit-id, Modbus TCP avstängt, eller en annan master.",
        "know_h": "Bra att veta",
        "k1_q": "Appen säger Zap", "k1": "Varje skärm säger Zap. Det är rätt flöde.",
        "k2_q": "Inga statuslampor", "k2": "Läs status på <b>blixt.local/api/network</b> i stället.",
        "k3_q": "Bara Ethernet?", "k3": "Appen ser inte Ethernet på 2.0.1 och visar wifi-steget ändå. Fråga Sourceful.",
        "card_k": "3.0.0", "card_m": "Nästa version",
        "card1": "<b>Den här sidan gäller 2.0.1</b>, versionen som körs i fält i oktober 2026.",
        "card2": "I 3.0.0 läggs enheter till med drivrutiner från Sourcefuls register. Sidan uppdateras när den släpps.",
        "foot1": "srcful-blixt-x-firmware d501e798 &middot; appen 2.7.9 &middot; verifierad 2026-10-15",
        "foot2": "Schematisk bild",
    },
    "en": {
        "title": "Set up a Blixt X",
        "rail": "Getting started &middot; Blixt X 2.0.1 &middot; Mainnet",
        "lede": "For the owner or installer. Blixt X connects inverters, batteries and meters to Sourceful, and is set up in the app like a Zap.",
        "before": "Before you start",
        "net_t": "Network", "net_d": "Ethernet or Wi-Fi with internet.",
        "app_t": "The app, signed in", "app_d": "With a profile and a site.",
        "dev_t": "Device list", "dev_d": "Model, IP, port, unit ID.",
        "bt_t": "Bluetooth on", "bt_d": "Stand close to the gateway.",
        "gw": "BLIXT X", "gw_sub": "RASPBERRY PI 4", "bt_win": "BLUETOOTH · 3 MIN", "bt_name": "blixt-&lt;serial&gt;",
        "phone": "The app", "net": "ETHERNET OR WI-FI", "cloud": "Sourceful", "cloud_sub": "MAINNET",
        "tcp": "Inverter", "tcp_sub": "MODBUS TCP", "rtu": "Meter / battery", "rtu_sub": "RS-485 · RTU",
        "laptop": "Check", "laptop_sub": "blixt.local/api/network",
        "s1_h": "Start",
        "s1_p": "Power on. Ethernet: plug in the cable. Wi-Fi: set in the app in step 4.",
        "s1_q": "Blixt X has no status lights to read. The check is step 5.",
        "s2_h": "The Bluetooth window",
        "s2_p": "After start it shows up as <b>blixt-&lt;serial&gt;</b> for <b>3 minutes</b>.",
        "s2_q": "Missed it: hold the button 3&nbsp;s or double-click. Or cut the power and start again.",
        "s3_h": "Connect the devices",
        "s3_p": "TCP devices on the same network, with a fixed IP. RTU devices on the gateway's RS-485 port.",
        "s3_q": "One Modbus master per device. Stop other systems that read the same device.",
        "s4_h": "In the app", "s4_micro": "Same flow as Zap",
        "app_steps": [
            ("<b>Onboard a new Zap</b>", "Under <b>Get started</b>, or <b>More → My Zaps</b>. The app says Zap."),
            ("Pick <b>blixt-…</b>", "Within 3 minutes of start. Most bars if you see several."),
            ("<b>Claim &amp; Configure network</b>", "The gateway joins the profile you have selected."),
            ("Wi-Fi", "Network, password, <b>Connect</b>. Hidden: <b>Enter manually</b>."),
            ("<b>Done</b>", "Name it if you like."),
            ("Devices", "<b>More → Energy devices</b>, then type, model, IP, port and unit ID."),
        ],
        "s5_h": "Done when",
        "seen": "You see this",
        "ok1_q": "<code>internetConnected: true</code>", "ok1": "And <code>mqttConnected: true</code> at <b>http://blixt.local/api/network</b> from the same network.",
        "ok2_q": "<code>/api/devices</code>", "ok2": "Lists the devices you added.",
        "ok3_q": "The app", "ok3": "Shows data from the devices.",
        "ifnot": "If not",
        "f1_q": "Not in the app", "f1": "The Bluetooth window has closed. The button or a restart opens it again.",
        "f2_q": "<code>blixt.local</code> does not answer", "f2": "With several on the network it is <code>blixt-…local</code>. Or use its IP address.",
        "f3_q": "<code>mqttConnected: false</code>", "f3": "No internet access. Check the network and the firewall.",
        "f4_q": "A device does not answer", "f4": "Wrong IP, port or unit ID, Modbus TCP off, or another master.",
        "know_h": "Good to know",
        "k1_q": "The app says Zap", "k1": "Every screen in the flow says Zap. It is the right flow for Blixt X.",
        "k2_q": "No status lights", "k2": "Read the status at <b>blixt.local/api/network</b> instead.",
        "k3_q": "Ethernet only?", "k3": "On 2.0.1 the app does not see Ethernet and shows the Wi-Fi step anyway. Ask Sourceful.",
        "card_k": "3.0.0", "card_m": "Next version",
        "card1": "<b>This page covers 2.0.1</b>, the version running in the field in October 2026.",
        "card2": "In 3.0.0, devices are added with drivers from Sourceful's registry. This page changes when it ships.",
        "foot1": "srcful-blixt-x-firmware d501e798 &middot; app 2.7.9 &middot; verified 2026-10-15",
        "foot2": "Schematic",
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


def hero(t):
    W, H = 186, 50
    o = [f'<svg class="hero bx" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')
    line = lambda d, w=1.0, c=INK, dash="": o.append(
        f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
        f'stroke-linejoin="round"{f" stroke-dasharray={chr(34)}{dash}{chr(34)}" if dash else ""}/>')
    label = lambda x, y, s, size=2.1, c=MUTED, anchor="start", weight="400": o.append(
        f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="0.3" fill="{c}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
    box = lambda x, y, w, h, title, sub, subc=MUTED: (
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>'),
        o.append(f'<text x="{x + 3}" y="{y + 5.2}" font-size="2.9" font-weight="500" fill="{INK}">{title}</text>'),
        label(x + 3, y + 8.6, sub, 1.8, subc))

    # phone with the Bluetooth window
    o.append(f'<rect x="10" y="12" width="15" height="26" rx="3" fill="#FFFFFF" stroke="{INK}" stroke-width="0.5"/>')
    o.append(f'<rect x="15" y="34.6" width="5" height="0.8" rx="0.4" fill="{INK}"/>')
    label(17.5, 43, t["phone"], 2.1, INK, "middle", "700")
    line("M27 25 H52", 0.6, BLUE, "1.2 1.2")
    label(39.5, 22.6, t["bt_win"], 1.8, BLUE, "middle", "700")
    label(39.5, 29.4, t["bt_name"], 1.8, MUTED, "middle")

    # the gateway
    gx, gy, gw, gh = 54, 13, 34, 24
    o.append(f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" rx="4" fill="{INK}"/>')
    s = 0.2
    o.append(f'<path d="{BOLT}" fill="{CREAM}" transform="translate({gx + 6 - 22.8 * s:.2f},{gy + 8 - 23.3 * s:.2f}) scale({s})"/>')
    label(gx + 10, gy + 9, t["gw"], 3, "#FAFAF7", weight="700")
    label(gx + 10, gy + 12.8, t["gw_sub"], 1.7, "#B9B6AA")

    # network up to Sourceful
    line(f"M{gx + gw} {gy + 6} H122", 1.0)
    label(105, gy + 4, t["net"], 1.8, INK, "middle", "700")
    box(122, 8, 30, 12, t["cloud"], t["cloud_sub"])
    # TCP device on the LAN
    line(f"M{gx + gw} {gy + 13} H100 V31 H122", 0.8)
    box(122, 24, 30, 12, t["tcp"], t["tcp_sub"])
    # RTU device on RS-485
    line(f"M{gx + gw / 2} {gy + gh} V44 H122", 0.8)
    box(122, 38.5, 30, 10.5, t["rtu"], t["rtu_sub"])
    # local check
    o.append(f'<rect x="155" y="24" width="28" height="12" rx="2.5" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="158" y="29.2" font-size="2.9" font-weight="500" fill="{INK}">{t["laptop"]}</text>')
    o.append(f'<text x="158" y="32.8" {MONO} font-size="1.55" fill="{SIGNAL}">{t["laptop_sub"]}</text>')
    line("M152 30 H155", 0.5, MUTED, "0.8 0.8")

    for n, (mx, my) in enumerate(((gx, gy), (39.5, 25), (gx + gw / 2, 44)), 1):
        o.append(marker(n, mx, my))
    o.append(marker(5, 182.5, 24))
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
        <div><span class="chip">{{IC_WIFI}}</span><div><div class="t">{{bt_t}}</div><div class="d">{{bt_d}}</div></div></div>
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
        "IC_WIFI": IC_WIFI, "HERO": hero(t), "APP_TRACK": track, "TICK": TICK,
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)
