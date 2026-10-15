"""Blixt one-pager: commission a Blixt (EDATEC ED-IPC3630) on a C&I site.

Facts from srcfl/blixt-gateway main @ 491197b (internal): README.md,
docs/specs/ipc-3600-specs.md, docs/gateway/DASHBOARD-ACCESS.md,
services/dashboard/README.md, docs/specs/site-limits.md, DeviceForm.tsx.
The drawing is a topology, not the physical front panel.
"""
from common import (crop, rail, BOLT, CREAM, IC_FUSE, IC_LAPTOP, IC_LIST, IC_SHIELD, INK, LOGO_LIGHT, MONO,
                    MUTED, SIGNAL, TICK, fill, marker, page)

# Set to True when CHECKLIST.md is ticked off on real hardware.
FIELD_TESTED = False

T = {
    "sv": {
        "title": "Driftsätt en Blixt",
        "rail": "Driftsättning &middot; Blixt &middot; IPC3630 / IPC2210",
        "lede": "För installatören på en kommersiell eller industriell anläggning. Från DIN-skenan till första batteritestet.",
        "before": "Innan du åker",
        "prep_t": "Förberedd av Sourceful", "prep_d": "Programvara, identitet, serieportar, dashboard-adress.",
        "site_t": "Anläggningens data", "site_d": "Säkring, antal faser, spänning.",
        "dev_t": "Enhetslista", "dev_d": "Modell, IP, port, unit-id. Drivrutin finns.",
        "kit_t": "Laptop och kabel", "kit_d": "Laptop, partvinnad kabel, 120 Ω, 9–36 V DC.",
        "leds": "LAMPOR", "leds_sub": "PWR röd · ACT grön", "leds_sub2": "PWR röd · ACT grön",
        "power": "9–36 V DC", "power_sub": "VIN+ överst · GND under",
        "rs485": "RS-485", "rs485_sub": "undre plinten",
        "eth0": "anläggningens nät", "eth2210": "ETH0: anläggningens nät", "no_serial": "bara Modbus TCP",
        "zoom": "UNDRE PLINTEN, IPC3630", "device": "Enhet",
        "zoom_note1": "A till A, B till B, IGND till GND.",
        "zoom_note2": "Inte den övre plinten (COM1, COM3).",
        "zoom_note3": "120 Ω mellan A och B i bussens båda ändar.",
        "s1_h": "Montera och anslut",
        "s1_p": "På DIN-skenan, antennerna uppåt. Ethernet i <b>1000M</b> (IPC3630) eller <b>ETH0</b> (IPC2210). Ström 9–36 V DC i gröna pluggen: <b>VIN+</b> överst, <b>GND</b> under.",
        "s1_q": "<b>PWR</b> röd fast: ström. Blinkar: dålig matning, bryt den. Första start: 10–20 min.",
        "s2_h": "Koppla RS-485",
        "s2_p": "Bara IPC3630: den undre plinten, <b>COM2</b> till vänster eller <b>COM4</b> till höger. COM-lampan blinkar när Modbus-trafik går.",
        "s2_q": "Inte terminerad från fabrik. I en buss-ände: 120 Ω mellan A och B i plinten. IPC2210: bara Modbus TCP.",
        "s3_h": "Öppna dashboarden",
        "s3_p": "Från laptopen: <b>http://blixt-&lt;serie&gt;.local/</b>, namnet får du av Sourceful. Eller IP-adressen från routern. Svarar inte på 4G.",
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
            "<b>RTU:</b> <code>/dev/ttyAMA4</code> (COM2) eller <code>/dev/ttyAMA3</code> (COM4). Förifyllda <code>ttyAMA0</code> är fel: byt.",
        ],
        "s6_h": "Klart när",
        "seen": "Det här syns",
        "ok1_q": "Devices: <code>live</code>", "ok1": "På varje enhet.",
        "ok2_q": "Flow", "ok2": "Effekt, laddnivå och frekvens inom några sekunder.",
        "ok3_q": "Batteritest", "ok3": "<b>Manual</b>, ~10 % av märkeffekten. Plus laddar, minus laddar ur. <b>FAULT</b> släckt.",
        "ifnot": "Om inte",
        "f1_q": "RTU-enhet: <code>timeout</code>", "f1": "Fel plint eller port, A/B förväxlade, fel hastighet eller unit-id, ingen terminering.",
        "f2_q": "PWR-lampan blinkar", "f2": "Matningen räcker inte eller är fel. Bryt strömmen och kontrollera den.",
        "f3_q": "Gråa reglage", "f3": "En aggregator styr. Det är avsiktligt.",
        "card_k": "SvK", "card_m": "Stödtjänster",
        "card1": "<b>Är anläggningen med på Svenska kraftnäts stödtjänstmarknad?</b> Ändra, starta om eller dra ur ingenting utan Sourcefuls godkännande för just det.",
        "card2": "Kopplingen till en <b>aggregator</b> gör Sourceful. Medan den styr är de lokala reglagen låsta.",
        "foot1": "blixt-gateway 491197b &middot; EDATECs manualer &middot; verifierad 2026-10-15",
        "foot2": "Ritad efter EDATEC, med Sourcefuls etikett",
    },
    "en": {
        "title": "Commission a Blixt",
        "rail": "Commissioning &middot; Blixt &middot; IPC3630 / IPC2210",
        "lede": "For the installer on a commercial or industrial site. From the DIN rail to the first battery test.",
        "before": "Before you go",
        "prep_t": "Prepared by Sourceful", "prep_d": "Software, identity, serial ports, dashboard address.",
        "site_t": "Site data", "site_d": "Fuse size, phases, voltage.",
        "dev_t": "Device list", "dev_d": "Model, IP, port, unit ID. A driver exists.",
        "kit_t": "Laptop and cable", "kit_d": "Laptop, twisted pair, 120 Ω, 9–36 V DC.",
        "leds": "LIGHTS", "leds_sub": "PWR red · ACT green", "leds_sub2": "PWR red · ACT green",
        "power": "9–36 V DC", "power_sub": "VIN+ top · GND below",
        "rs485": "RS-485", "rs485_sub": "the lower plug",
        "eth0": "site network", "eth2210": "ETH0: the site network", "no_serial": "Modbus TCP only",
        "zoom": "THE LOWER PLUG, IPC3630", "device": "Device",
        "zoom_note1": "A to A, B to B, IGND to GND.",
        "zoom_note2": "Not the upper plug (COM1, COM3).",
        "zoom_note3": "120 Ω between A and B at both ends of the bus.",
        "s1_h": "Mount and connect",
        "s1_p": "On the DIN rail, antennas up. Ethernet in <b>1000M</b> (IPC3630) or <b>ETH0</b> (IPC2210). Power 9–36 V DC in the green plug: <b>VIN+</b> on top, <b>GND</b> below.",
        "s1_q": "<b>PWR</b> red, solid: power. Blinking: bad supply, cut it. First start: 10–20 min.",
        "s2_h": "Wire RS-485",
        "s2_p": "IPC3630 only: the lower plug, <b>COM2</b> on the left or <b>COM4</b> on the right. The COM light blinks when Modbus traffic flows.",
        "s2_q": "Not terminated from the factory. At a bus end: 120 Ω between A and B at the plug. IPC2210: Modbus TCP only.",
        "s3_h": "Open the dashboard",
        "s3_p": "From the laptop: <b>http://blixt-&lt;serial&gt;.local/</b>; Sourceful gives you the name. Or the IP from the router. No answer over 4G.",
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
            "<b>RTU:</b> <code>/dev/ttyAMA4</code> (COM2) or <code>/dev/ttyAMA3</code> (COM4). The pre-filled <code>ttyAMA0</code> is wrong: change it.",
        ],
        "s6_h": "Done when",
        "seen": "You see this",
        "ok1_q": "Devices: <code>live</code>", "ok1": "On every device.",
        "ok2_q": "Flow", "ok2": "Power, state of charge and frequency within seconds.",
        "ok3_q": "Battery test", "ok3": "<b>Manual</b>, ~10 % of rated power. Plus charges, minus discharges. <b>FAULT</b> off.",
        "ifnot": "If not",
        "f1_q": "RTU device: <code>timeout</code>", "f1": "Wrong plug or port, A/B swapped, wrong baud or unit ID, no termination.",
        "f2_q": "The PWR light blinks", "f2": "The supply is too weak or wrong. Cut the power and check it.",
        "f3_q": "Controls greyed out", "f3": "An aggregator is in control. That is intended.",
        "card_k": "SvK", "card_m": "Reserve market",
        "card1": "<b>Does the site take part in Svenska kraftnät's reserve market?</b> Change nothing, do not restart and do not unplug anything without Sourceful's approval for that exact action.",
        "card2": "Sourceful connects the <b>aggregator</b>. While it is in control, the local controls are locked.",
        "foot1": "blixt-gateway 491197b &middot; EDATEC manuals &middot; verified 2026-10-15",
        "foot2": "Drawn after EDATEC, with Sourceful's label",
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
.hero.blixt{height:64mm;}
h1{font-size:31pt;}
.saj p{flex:1.4;}
.olist{list-style:none;counter-reset:n;}
.olist li{counter-increment:n;display:flex;gap:2mm;padding:1.2mm 0;border-top:0.6pt solid var(--hair-faint);font-size:8.1pt;line-height:1.36;}
.olist li::before{content:counter(n);flex:none;width:4mm;font-family:'JetBrains Mono',monospace;font-size:7pt;color:var(--signal);}
.sec .warn{margin-top:1.6mm;font-size:8pt;}
.steps3 .warn{font-size:8pt;margin:0 0 1.2mm;}
"""


def hero(t, export=False):
    """IPC3630 and IPC2210 as mounted on the DIN rail, white-labelled, plus the RS-485 plug.

    Front-panel layout from EDATEC's drawings (edatec.cn/docs/ipc3630/um/1-hardware/,
    edatec.cn/docs/ipc2200/um/1-hardware/). Real fronts are 55 x 143 mm (IPC3630) and
    34 x 143 mm (IPC2210); drawn at 0.3. The vendor label is replaced by Sourceful's.
    """
    W, H = 186, 64
    k = 0.3
    o = [f'<svg class="hero blixt" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Satoshi">']
    if not export:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="{CREAM}"/>')
    line = lambda d, w=0.25, c=MUTED: o.append(
        f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    label = lambda x, y, s, size=1.8, c=INK, anchor="start", weight="700": o.append(
        f'<text x="{x}" y="{y}" {MONO} font-size="{size}" letter-spacing="0.2" fill="{c}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
    SIDE, RIB, FRONT, PLUG = "#2B2B2A", "#3A3A38", "#ECEAE4", "#1E1F21"
    GOLD, RED, GRN, BLUEP = "#B8892E", "#C8372D", "#15803D", "#2F5DA8"
    top, fh = 11, 143 * k

    def body(x, side_w, front_w):
        for ax in (x + side_w * 0.35, x + side_w * 0.8):            # SMA antennas on the top end
            o.append(f'<rect x="{ax - 0.9:.2f}" y="{top - 2}" width="1.8" height="2" fill="{GOLD}"/>')
            o.append(f'<rect x="{ax - 0.8:.2f}" y="{top - 8.5}" width="1.6" height="6.6" rx="0.8" fill="{INK}"/>')
        o.append(f'<rect x="{x}" y="{top}" width="{side_w}" height="{fh}" rx="0.8" fill="{SIDE}"/>')
        n = int(side_w / 0.9)
        for i in range(1, n):
            o.append(f'<rect x="{x + i * 0.9:.2f}" y="{top + 0.6}" width="0.3" height="{fh - 1.2:.2f}" fill="{RIB}"/>')
        sx = x + side_w * 0.2                                         # Sourceful label band
        o.append(f'<rect x="{sx:.2f}" y="{top + 1.5}" width="{side_w * 0.3:.2f}" height="{fh - 3:.2f}" fill="{SIGNAL}"/>')
        s = 0.07
        o.append(f'<path d="{BOLT}" fill="#FFFFFF" transform="translate({sx + side_w * 0.15 - 22.8 * s:.2f},{top + 4 - 23.3 * s:.2f}) scale({s})"/>')
        o.append(f'<text transform="translate({sx + side_w * 0.15 + 0.7:.2f},{top + fh - 3}) rotate(-90)" '
                 f'{MONO} font-size="1.8" letter-spacing="0.4" fill="#FFFFFF" font-weight="700">BLIXT</text>')
        fx = x + side_w
        o.append(f'<rect x="{fx}" y="{top}" width="{front_w}" height="{fh}" rx="0.6" fill="{FRONT}" stroke="#C9C6BD" stroke-width="0.2"/>')
        return fx

    Y = lambda r: top + r * fh                                        # relative height on the front

    def callout(x0, y0, x1, text, sub=""):
        line(f"M{x0} {y0} H{x1 - 0.8}")
        label(x1, y0 + 0.6, text)
        if sub:
            label(x1, y0 + 2.9, sub, 1.55, MUTED, weight="400")

    # ---------------- IPC3630 ----------------
    fx = body(8, 9, 55 * k)
    fw = 55 * k
    for r in range(4):                                                 # ACT|PWR, USER|4G, COM1|COM3, COM2|COM4
        cy = Y(0.10 + r * 0.025)
        o.append(f'<circle cx="{fx + 2.8}" cy="{cy:.2f}" r="0.45" fill="{GRN if r == 0 else "#9C9A92"}"/>')
        o.append(f'<circle cx="{fx + 4.4}" cy="{cy:.2f}" r="0.45" fill="{RED if r == 0 else "#9C9A92"}"/>')
    for r in range(9):                                                 # DI / CAN / DO LEDs, not used
        cy = Y(0.10 + r * 0.025)
        for cx in (fx + 10.8, fx + 12.4):
            o.append(f'<circle cx="{cx}" cy="{cy:.2f}" r="0.4" fill="#C4C1B8"/>')
    o.append(f'<rect x="{fx + 2}" y="{Y(0.23):.2f}" width="3" height="{0.11 * fh:.2f}" rx="0.3" fill="{GRN}"/>')   # power
    for py in (0.49, 0.575):                                          # serial plugs, upper then lower
        o.append(f'<rect x="{fx + 2}" y="{Y(py):.2f}" width="6" height="{0.075 * fh:.2f}" rx="0.3" fill="{PLUG}"/>')
    o.append(f'<rect x="{fx + 2}" y="{Y(0.575):.2f}" width="6" height="{0.075 * fh:.2f}" rx="0.3" fill="none" stroke="{SIGNAL}" stroke-width="0.45"/>')
    for py in (0.49, 0.68, 0.80):                                      # DI, CAN, DO plugs, not used
        o.append(f'<rect x="{fx + 10}" y="{Y(py):.2f}" width="5.2" height="{0.1 * fh:.2f}" rx="0.3" fill="#B9B6AD"/>')
    for py in (0.68, 0.81):                                            # 1000M, 100M
        o.append(f'<rect x="{fx + 2.4}" y="{Y(py):.2f}" width="5.4" height="{0.095 * fh:.2f}" rx="0.3" fill="#8F8D86"/>')
        o.append(f'<rect x="{fx + 3.3}" y="{Y(py) + 1.2:.2f}" width="3.6" height="2" fill="{PLUG}"/>')
    cx = fx + fw + 2.5
    callout(fx + 5, Y(0.11), cx, t["leds"], t["leds_sub"])
    callout(fx + 5, Y(0.285), cx, t["power"], t["power_sub"])
    callout(fx + 8, Y(0.61), cx, t["rs485"], t["rs485_sub"])
    callout(fx + 7.8, Y(0.725), cx, "1000M", t["eth0"])
    label(8 + (9 + fw) / 2, top + fh + 4.6, "IPC3630", 2.2, INK, "middle")

    # ---------------- IPC2210 ----------------
    x2 = 62
    fx2 = body(x2, 7, 34 * k)
    fw2 = 34 * k
    for r in range(2):                                                 # ACT|PWR, USER|4G
        cy = Y(0.08 + r * 0.03)
        o.append(f'<circle cx="{fx2 + 3.5}" cy="{cy:.2f}" r="0.45" fill="{GRN if r == 0 else "#9C9A92"}"/>')
        o.append(f'<circle cx="{fx2 + 6.5}" cy="{cy:.2f}" r="0.45" fill="{RED if r == 0 else "#9C9A92"}"/>')
    o.append(f'<rect x="{fx2 + 3.6}" y="{Y(0.19):.2f}" width="3" height="{0.11 * fh:.2f}" rx="0.3" fill="{GRN}"/>')
    for py in (0.49, 0.62, 0.75):                                      # ETH0, ETH1, ETH2
        o.append(f'<rect x="{fx2 + 2.4}" y="{Y(py):.2f}" width="5.4" height="{0.105 * fh:.2f}" rx="0.3" fill="#8F8D86"/>')
        o.append(f'<rect x="{fx2 + 3.3}" y="{Y(py) + 1.4:.2f}" width="3.6" height="2" fill="{PLUG}"/>')
    o.append(f'<rect x="{fx2 + 3.4}" y="{Y(0.89):.2f}" width="3.4" height="{0.05 * fh:.2f}" rx="0.3" fill="{BLUEP}"/>')
    cx2 = fx2 + fw2 + 2.5
    callout(fx2 + 7, Y(0.095), cx2, t["leds"], t["leds_sub2"])
    callout(fx2 + 6.6, Y(0.245), cx2, t["power"], t["power_sub"])
    callout(fx2 + 7.8, Y(0.62), cx2, "ETH0–ETH2", t["eth2210"])
    callout(fx2 + 6.8, Y(0.9), cx2, "USB", t["no_serial"])
    label(x2 + (7 + fw2) / 2, top + fh + 4.6, "IPC2210", 2.2, INK, "middle")

    # ---------------- the RS-485 plug, close up ----------------
    zx, zy, zw, zh = 118, 6, 64, 52
    o.append(f'<rect x="{zx}" y="{zy}" width="{zw}" height="{zh}" rx="3" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    label(zx + 3, zy + 4.4, t["zoom"], 1.9, MUTED, weight="400")
    # the device on the left, the plug on the right: COM2 is the left column, so its wires leave left
    o.append(f'<rect x="{zx + 4}" y="{zy + 10}" width="15" height="19" rx="2" fill="#FFFFFF" stroke="{INK}" stroke-width="0.4"/>')
    o.append(f'<text x="{zx + 11.5}" y="{zy + 18.5}" text-anchor="middle" font-size="2.5" font-weight="500" fill="{INK}">{t["device"]}</text>')
    label(zx + 11.5, zy + 22, "MODBUS RTU", 1.4, MUTED, "middle", "400")
    px, py0, cw, rh = zx + 38, zy + 11, 8, 5.6
    o.append(f'<rect x="{px}" y="{py0}" width="{cw * 2 + 3}" height="{rh * 3 + 2}" rx="0.8" fill="{PLUG}"/>')
    names = (("IGND", "A2", "B2"), ("IGND", "A4", "B4"))
    for c in range(2):
        for r in range(3):
            cx0 = px + 1 + c * (cw + 1)
            o.append(f'<rect x="{cx0:.2f}" y="{py0 + 1 + r * rh:.2f}" width="{cw}" height="{rh - 0.8}" rx="0.4" fill="#3A3B3E"/>')
            o.append(f'<circle cx="{cx0 + 1.6:.2f}" cy="{py0 + 1 + r * rh + (rh - 0.8) / 2:.2f}" r="0.9" fill="#8F8D86"/>')
            label(cx0 + 3, py0 + 1 + r * rh + 3.2, names[c][r], 1.6, "#FAFAF7")
    label(px + 1 + cw / 2, py0 - 1.4, "COM2", 2, SIGNAL, "middle")
    label(px + 2 + cw * 1.5, py0 - 1.4, "COM4", 2, SIGNAL, "middle")
    label(px + 1 + cw / 2, py0 + rh * 3 + 5.4, "ttyAMA4", 1.45, MUTED, "middle", "400")
    label(px + 2 + cw * 1.5, py0 + rh * 3 + 5.4, "ttyAMA3", 1.45, MUTED, "middle", "400")
    for r, (name, colr) in enumerate((("GND", INK), ("A", SIGNAL), ("B", "#1D4ED8"))):
        yy = py0 + 1 + r * rh + (rh - 0.8) / 2
        dy = zy + 13.5 + r * 5
        line(f"M{px + 2.6:.2f} {yy:.2f} C{px - 6} {yy:.2f} {zx + 26} {dy:.2f} {zx + 19} {dy:.2f}", 0.7, colr)
        label(zx + 21, dy - 0.9, name, 1.7, colr)
    label(zx + 3, zy + zh - 7.2, t["zoom_note1"], 1.75, INK, weight="400")
    label(zx + 3, zy + zh - 4.2, t["zoom_note2"], 1.75, INK, weight="400")
    label(zx + 3, zy + zh - 1.4, t["zoom_note3"], 1.75, SIGNAL, weight="700")

    if not export:
        o.append(marker(1, 8 + 4.5, top + 3.5))
        o.append(marker(2, zx + zw - 4, zy + 4))
        o.append(marker(3, fx + 1.2, Y(0.725)))
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
      <p>{{s2_p}}</p>
      <p class="quiet">{{s2_q}}</p>
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
    values = {k: v for k, v in t.items() if isinstance(v, str)}
    values["rail"] = rail(lang, t["rail"], FIELD_TESTED)
    values.update({
        "LOGO": LOGO_LIGHT, "IC_SHIELD": IC_SHIELD, "IC_FUSE": IC_FUSE, "IC_LIST": IC_LIST,
        "IC_LAPTOP": IC_LAPTOP, "HERO": hero(t), "TICK": TICK,
        "S4": "".join(f"<li><span>{x}</span></li>" for x in t["s4_list"]),
        "S5": "".join(f"<li><span>{x}</span></li>" for x in t["s5_list"]),
    })
    return page(lang, t["title"], fill(BODY, values), EXTRA_CSS)


# Standalone drawings for assets/devices/, cut out of the hero (English labels).
DEVICES = {"blixt-ipc3630": (4, 0, 56, 64), "blixt-ipc2210": (60.5, 0, 55.5, 64)}


def devices():
    return {name: crop(hero(T["en"], export=True), box) for name, box in DEVICES.items()}
