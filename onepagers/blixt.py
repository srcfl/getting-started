"""Blixt one-pager: commission a Blixt (EDATEC ED-IPC3630) on a C&I site.

Facts from srcfl/blixt-gateway main @ 491197b (internal): README.md,
docs/specs/ipc-3600-specs.md, docs/gateway/DASHBOARD-ACCESS.md,
services/dashboard/README.md, docs/specs/site-limits.md, DeviceForm.tsx.
The drawing is a topology, not the physical front panel.
"""
from common import (BOLT, CREAM, IC_FUSE, IC_LAPTOP, IC_LIST, IC_SHIELD, INK, LOGO_LIGHT, MONO,
                    MUTED, SIGNAL, TICK, fill, marker, page)

T = {
    "sv": {
        "title": "Driftsätt en Blixt",
        "rail": "Driftsättning &middot; Blixt &middot; IPC3630",
        "lede": "För installatören på en kommersiell eller industriell anläggning. Från montering till första batteritestet.",
        "before": "Innan du åker",
        "prep_t": "Förberedd av Sourceful", "prep_d": "Programvara, identitet och serieportar klara.",
        "site_t": "Anläggningens data", "site_d": "Säkring, antal faser, spänning.",
        "dev_t": "Enhetslista", "dev_d": "Modell, IP, port, unit-id. Drivrutin finns.",
        "kit_t": "Laptop och kabel", "kit_d": "Laptop på nätet, partvinnad kabel, 9–36 V DC.",
        "blixt": "BLIXT", "model": "IPC3630", "power": "9–36 V DC", "pins_power": "1 GND · 2 VIN+",
        "lan": "ANLÄGGNINGENS NÄT", "dhcp": "DHCP", "tcp_dev": "Växelriktare", "tcp_sub": "MODBUS TCP · 502",
        "laptop": "Laptop", "url": "blixt-&lt;serie&gt;.local",
        "bus": "RS-485 · COM2 ELLER COM4", "bus_sub": "A–A · B–B · GND",
        "dev1": "Batteriväxelriktare", "dev2": "Anläggningsmätare", "rtu": "MODBUS RTU",
        "term": "120 Ω",
        "s1_h": "Montera och anslut",
        "s1_p": "Antenner på <b>4G</b> och <b>WiFi/BT</b>. Ethernet till nätet (DHCP). Ström 9–36 V DC: <b>stift 1 GND</b>, <b>stift 2 VIN+</b>. Kontrollera polariteten.",
        "s1_q": "Första starten hämtar ~1,6 GB, 10–20 min. Bryt inte strömmen. Rör inte <b>PROGRAMMING</b>.",
        "s2_h": "Koppla RS-485",
        "s2_warn": "Bara <b>COM2</b> eller <b>COM4</b>. COM1 och COM3 tappar Modbus-ramar.",
        "s2_rows": [("COM2", "1", "3", "<code>ttyAMA4</code>", "J22"), ("COM4", "2", "4", "<code>ttyAMA3</code>", "J24")],
        "s2_cols": ("Port", "B", "A", "Enhet", "120 Ω"),
        "s2_p": "GND på stift 5 eller 6. Terminera bara bussens ändar. En Modbus-master per enhet.",
        "s3_h": "Öppna dashboarden",
        "s3_p": "Från laptopen: <b>http://blixt-&lt;serie&gt;.local/</b>. Bara <code>blixt.local</code> blir fel med flera Blixt. Svarar inte på 4G.",
        "s3_q": "Den som når dashboarden kan styra batteriet. Skyddat nät, aldrig mot internet.",
        "s4_h": "Ställ in anläggningen", "s4_micro": "Före all styrning",
        "s4_list": [
            "<b>Flow → Site configuration</b>.",
            "Säkring, faser, spänning. Standard: 63 A, 3 faser, 230 V.",
            "Välj anläggningens mätare. Den måste ge ström och spänning per fas.",
        ],
        "s5_h": "Lägg till enheterna",
        "s5_list": [
            "<b>Devices → Add device</b>. Drivrutin och <b>version</b> ur registret. Lås versionen.",
            "<b>TCP:</b> IP, port (oftast 502), unit-id.",
            "<b>RTU:</b> <code>/dev/ttyAMA4</code> (COM2) eller <code>/dev/ttyAMA3</code> (COM4), hastighet, paritet, unit-id. Förifyllda <code>ttyAMA0</code> är COM3: byt.",
        ],
        "s6_h": "Klart när",
        "seen": "Det här syns",
        "ok1_q": "Devices: <code>live</code>", "ok1": "På varje enhet.",
        "ok2_q": "Flow", "ok2": "Effekt, laddnivå och frekvens inom några sekunder.",
        "ok3_q": "Batteritest", "ok3": "<b>Manual</b>, ~10 % av märkeffekten. Plus laddar, minus laddar ur. <b>FAULT</b> släckt.",
        "ifnot": "Om inte",
        "f1_q": "RTU-enhet: <code>timeout</code>", "f1": "Fel port, A/B förväxlade, fel hastighet eller unit-id, ingen terminering.",
        "f2_q": "Skräpdata oavsett hastighet", "f2": "Serieportarna är inte aktiverade. Kontakta Sourceful.",
        "f3_q": "Gråa reglage", "f3": "En aggregator styr. Det är avsiktligt.",
        "card_k": "SvK", "card_m": "Stödtjänster",
        "card1": "<b>Är anläggningen med på Svenska kraftnäts stödtjänstmarknad?</b> Ändra, starta om eller dra ur ingenting utan Sourcefuls godkännande för just det.",
        "card2": "Kopplingen till en <b>aggregator</b> gör Sourceful. Medan den styr är de lokala reglagen låsta.",
        "foot1": "blixt-gateway main 491197b &middot; verifierad 2026-10-15",
        "foot2": "Topologi, inte frontpanelen",
    },
    "en": {
        "title": "Commission a Blixt",
        "rail": "Commissioning &middot; Blixt &middot; IPC3630",
        "lede": "For the installer on a commercial or industrial site. From mounting to the first battery test.",
        "before": "Before you go",
        "prep_t": "Prepared by Sourceful", "prep_d": "Software, identity and serial ports ready.",
        "site_t": "Site data", "site_d": "Fuse size, phases, voltage.",
        "dev_t": "Device list", "dev_d": "Model, IP, port, unit ID. A driver exists.",
        "kit_t": "Laptop and cable", "kit_d": "Laptop on the network, twisted pair, 9–36 V DC.",
        "blixt": "BLIXT", "model": "IPC3630", "power": "9–36 V DC", "pins_power": "1 GND · 2 VIN+",
        "lan": "SITE NETWORK", "dhcp": "DHCP", "tcp_dev": "Inverter", "tcp_sub": "MODBUS TCP · 502",
        "laptop": "Laptop", "url": "blixt-&lt;serial&gt;.local",
        "bus": "RS-485 · COM2 OR COM4", "bus_sub": "A–A · B–B · GND",
        "dev1": "Battery inverter", "dev2": "Site meter", "rtu": "MODBUS RTU",
        "term": "120 Ω",
        "s1_h": "Mount and connect",
        "s1_p": "Antennas on <b>4G</b> and <b>WiFi/BT</b>. Ethernet to the network (DHCP). Power 9–36 V DC: <b>pin 1 GND</b>, <b>pin 2 VIN+</b>. Check the polarity.",
        "s1_q": "The first start downloads ~1.6 GB, 10–20 min. Keep the power on. Leave <b>PROGRAMMING</b> alone.",
        "s2_h": "Wire RS-485",
        "s2_warn": "Only <b>COM2</b> or <b>COM4</b>. COM1 and COM3 drop Modbus frames.",
        "s2_rows": [("COM2", "1", "3", "<code>ttyAMA4</code>", "J22"), ("COM4", "2", "4", "<code>ttyAMA3</code>", "J24")],
        "s2_cols": ("Port", "B", "A", "Device", "120 Ω"),
        "s2_p": "GND on pin 5 or 6. Terminate only the ends of the bus. One Modbus master per device.",
        "s3_h": "Open the dashboard",
        "s3_p": "From the laptop: <b>http://blixt-&lt;serial&gt;.local/</b>. Plain <code>blixt.local</code> goes wrong with several Blixts. No answer over 4G.",
        "s3_q": "Whoever reaches the dashboard can control the battery. Protected network, never the internet.",
        "s4_h": "Set up the site", "s4_micro": "Before any control",
        "s4_list": [
            "<b>Flow → Site configuration</b>.",
            "Fuse, phases, voltage. Default: 63 A, 3 phases, 230 V.",
            "Choose the site meter. It must give current and voltage per phase.",
        ],
        "s5_h": "Add the devices",
        "s5_list": [
            "<b>Devices → Add device</b>. Driver and <b>version</b> from the registry. Pin the version.",
            "<b>TCP:</b> IP, port (usually 502), unit ID.",
            "<b>RTU:</b> <code>/dev/ttyAMA4</code> (COM2) or <code>/dev/ttyAMA3</code> (COM4), baud, parity, unit ID. The pre-filled <code>/dev/ttyAMA0</code> is COM3: change it.",
        ],
        "s6_h": "Done when",
        "seen": "You see this",
        "ok1_q": "Devices: <code>live</code>", "ok1": "On every device.",
        "ok2_q": "Flow", "ok2": "Power, state of charge and frequency within seconds.",
        "ok3_q": "Battery test", "ok3": "<b>Manual</b>, ~10 % of rated power. Plus charges, minus discharges. <b>FAULT</b> off.",
        "ifnot": "If not",
        "f1_q": "RTU device: <code>timeout</code>", "f1": "Wrong port, A/B swapped, wrong baud or unit ID, no termination.",
        "f2_q": "Garbage at every baud rate", "f2": "The serial ports are not enabled. Contact Sourceful.",
        "f3_q": "Controls greyed out", "f3": "An aggregator is in control. That is intended.",
        "card_k": "SvK", "card_m": "Reserve market",
        "card1": "<b>Does the site take part in Svenska kraftnät's reserve market?</b> Change nothing, do not restart and do not unplug anything without Sourceful's approval for that exact action.",
        "card2": "Sourceful connects the <b>aggregator</b>. While it is in control, the local controls are locked.",
        "foot1": "blixt-gateway main 491197b &middot; verified 2026-10-15",
        "foot2": "Topology, not the front panel",
    },
}

EXTRA_CSS = """
.pins{width:100%;border-collapse:collapse;margin:1.4mm 0 1.4mm;font-size:7.8pt;}
.pins th{font-family:'JetBrains Mono',monospace;font-weight:400;font-size:6pt;letter-spacing:0.12em;
  text-transform:uppercase;color:var(--muted);text-align:left;padding:0 1.2mm 0.8mm 0;}
.pins td{padding:0.9mm 1.2mm 0.9mm 0;border-top:0.6pt solid var(--hair-faint);}
.pins td:first-child{font-weight:700;color:var(--ink);}
code{font-family:'JetBrains Mono',monospace;font-size:0.88em;}
.cols2{display:flex;gap:6mm;}
.cols2 > section, .cols2 > div{flex:none;width:90mm;}
.hero.blixt{height:52mm;}
h1{font-size:31pt;}
.saj p{flex:1.4;}
.olist{list-style:none;counter-reset:n;}
.olist li{counter-increment:n;display:flex;gap:2mm;padding:1.2mm 0;border-top:0.6pt solid var(--hair-faint);font-size:8.1pt;line-height:1.36;}
.olist li::before{content:counter(n);flex:none;width:4mm;font-family:'JetBrains Mono',monospace;font-size:7pt;color:var(--signal);}
.sec .warn{margin-top:1.6mm;font-size:8pt;}
.steps3 .warn{font-size:8pt;margin:0 0 1.2mm;}
"""


def hero(t):
    W, H = 186, 52
    o = [f'<svg class="hero blixt" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')
    line = lambda d, w=1.0, c=INK: o.append(
        f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    label = lambda x, y, s, size=2.1, c=MUTED, anchor="start", weight="400": o.append(
        f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="0.3" fill="{c}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
    box = lambda x, y, w, h: o.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')

    # Blixt with antennas and the power terminal
    bx, by, bw, bh = 10, 13, 40, 25
    for ax, name in ((bx + 8, "4G"), (bx + bw - 10, "WiFi/BT")):
        line(f"M{ax} {by} V{by - 7}", 0.8)
        o.append(f'<circle cx="{ax}" cy="{by - 7.6}" r="1.1" fill="{INK}"/>')
        label(ax + 2, by - 5.6, name, 2)
    o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="4.5" fill="{INK}"/>')
    s = 0.2
    o.append(f'<path d="{BOLT}" fill="{CREAM}" transform="translate({bx + 6 - 22.8 * s:.2f},{by + 7 - 23.3 * s:.2f}) scale({s})"/>')
    label(bx + 10, by + 8.1, t["blixt"], 3.2, "#FAFAF7", weight="700")
    label(bx + 10, by + 12, t["model"], 2, "#B9B6AA")
    for py, name in ((by + 7, "ETH0"), (by + 18, "COM2")):
        o.append(f'<rect x="{bx + bw - 1}" y="{py - 1.6}" width="3" height="3.2" rx="0.6" fill="#55534F"/>')
        label(bx + bw - 3, py + 0.8, name, 2, "#B9B6AA", "end")
    line(f"M{bx + 12} {by + bh} V{by + bh + 3.5}", 0.8)
    o.append(f'<rect x="{bx + 9}" y="{by + bh + 3.5}" width="6" height="3" rx="0.5" fill="#5E8F66"/>')
    label(bx + 17, by + bh + 5.9, t["power"], 2.2, INK, weight="700")
    label(bx + 17, by + bh + 9, t["pins_power"], 1.9)

    # Ethernet: site network -> TCP inverter and laptop
    sx, sy = 70, 12
    line(f"M{bx + bw + 2} {by + 7} H{sx}", 1.0)
    box(sx, sy, 30, 14)
    label(sx + 15, sy + 6.2, t["lan"], 2, INK, "middle", "700")
    label(sx + 15, sy + 10, t["dhcp"], 1.9, MUTED, "middle")
    tx = sx + 44
    line(f"M{sx + 30} {sy + 4.5} H{sx + 37} V{sy - 3} H{tx}", 0.8)
    line(f"M{sx + 30} {sy + 9.5} H{sx + 37} V{sy + 17} H{tx}", 0.8)
    box(tx, sy - 9, 36, 12)
    o.append(f'<text x="{tx + 3}" y="{sy - 3.6}" font-size="3" font-weight="500" fill="{INK}">{t["tcp_dev"]}</text>')
    label(tx + 3, sy - 0.2, t["tcp_sub"], 1.8)
    box(tx, sy + 11, 36, 12)
    o.append(f'<text x="{tx + 3}" y="{sy + 16.4}" font-size="3" font-weight="500" fill="{INK}">{t["laptop"]}</text>')
    label(tx + 3, sy + 19.8, t["url"], 1.8, SIGNAL)

    # RS-485 bus from COM2, terminated at both ends
    busy = 41
    cx = bx + bw + 2
    line(f"M{cx} {by + 18} H{cx + 6} V{busy} H178", 1.0)
    label(cx + 10, busy - 2, t["bus"], 2, INK, weight="700")
    label(cx + 10, busy - 5, t["bus_sub"], 1.8)
    for dx, name in ((110, t["dev1"]), (146, t["dev2"])):
        line(f"M{dx} {busy} V{busy + 2.5}", 1.0)
        box(dx - 15, busy + 2.5, 30, 8.6)
        o.append(f'<text x="{dx}" y="{busy + 6.4}" text-anchor="middle" font-size="2.6" font-weight="500" fill="{INK}">{name}</text>')
        label(dx, busy + 9.3, t["rtu"], 1.6, MUTED, "middle")
    for rx in (cx + 14, 178):
        line(f"M{rx} {busy} V{busy + 1.6}", 0.45, SIGNAL)
        o.append(f'<rect x="{rx - 1.2}" y="{busy + 1.6}" width="2.4" height="4.6" rx="0.4" fill="#FFFFFF" stroke="{SIGNAL}" stroke-width="0.45"/>')
        label(rx, busy + 9, t["term"], 1.9, SIGNAL, "middle", "700")

    for n, (mx, my) in enumerate(((bx + 4, by + bh + 5), (cx + 6, busy - 7.5), (tx + 36, sy + 11)), 1):
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
        <div><span class="chip">{{IC_SHIELD}}</span><div><div class="t">{{prep_t}}</div><div class="d">{{prep_d}}</div></div></div>
        <div><span class="chip">{{IC_FUSE}}</span><div><div class="t">{{site_t}}</div><div class="d">{{site_d}}</div></div></div>
        <div><span class="chip">{{IC_LIST}}</span><div><div class="t">{{dev_t}}</div><div class="d">{{dev_d}}</div></div></div>
        <div><span class="chip">{{IC_LAPTOP}}</span><div><div class="t">{{kit_t}}</div><div class="d">{{kit_d}}</div></div></div>
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
      <p class="warn">{{s2_warn}}</p>
      {{PINS}}
      <p class="quiet">{{s2_p}}</p>
    </section>
    <section>
      <div class="head"><span class="num">3</span><span class="h">{{s3_h}}</span></div>
      <p>{{s3_p}}</p>
      <p class="quiet">{{s3_q}}</p>
    </section>
  </div>

  <div class="cols2">
    <section class="sec">
      <div class="head"><span class="num">4</span><span class="h">{{s4_h}}</span><span class="micro">{{s4_micro}}</span></div>
      <ol class="olist">{{S4}}</ol>
    </section>
    <section class="sec">
      <div class="head"><span class="num">5</span><span class="h">{{s5_h}}</span></div>
      <ol class="olist">{{S5}}</ol>
    </section>
  </div>

  <section class="sec">
    <div class="head"><span class="num">6</span><span class="h">{{s6_h}}</span></div>
    <div class="cols2 plain">
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
    cols = "".join(f"<th>{c}</th>" for c in t["s2_cols"])
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in t["s2_rows"])
    values = {k: v for k, v in t.items() if isinstance(v, str)}
    values.update({
        "LOGO": LOGO_LIGHT, "IC_SHIELD": IC_SHIELD, "IC_FUSE": IC_FUSE, "IC_LIST": IC_LIST,
        "IC_LAPTOP": IC_LAPTOP, "HERO": hero(t), "TICK": TICK,
        "PINS": f'<table class="pins"><tr>{cols}</tr>{rows}</table>',
        "S4": "".join(f"<li><span>{x}</span></li>" for x in t["s4_list"]),
        "S5": "".join(f"<li><span>{x}</span></li>" for x in t["s5_list"]),
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)
