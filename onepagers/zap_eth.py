"""Zap ETH one-pager: connect a Zap ETH to a P1 meter, over Ethernet or Wi-Fi.

Sources:
- The hardware vendor's documentation (2026-11-07): the IN side has, from left, P1 IN,
  Ethernet, USB-C and the green power light (from hardware 3.2 the power light sits in P1 IN);
  the OUT side has the button, the blue status light and P1 OUT. The green light is always on
  and never blinks. A version 5.0 meter powers it; older meters need USB-C. No PoE.
- srcfl/srcful-zap-x-firmware v7.0.5 (346754de): zap-eth.h (ESP32-C3, W5500, one status light
  on GPIO 8, button GPIO 9, P1 in on GPIO 0, P1 TX -1 so P1 OUT passes nothing on, no Modbus
  RTU pins), main.cpp (status light on 500 ms at boot; Bluetooth starts without saved Wi-Fi,
  also with Ethernet), main_loop.cpp (on while Bluetooth waits; Bluetooth stops 60 s after
  Wi-Fi or Ethernet is up; button 2/5/10 s), eth_manager.cpp (DHCP).
- The app 2.7.9: as for the Zap Ultra Mini ("Ethernet detected", "Skip WiFi setup").
- Sourceful's test rig, 2026-11-07: a Zap ETH on 7.0.5 reads a P1 meter.
"""
import zap_ethernet
from common import BLUE, GREEN

# Set to True when CHECKLIST.md is ticked off on real hardware.
FIELD_TESTED = False

LAYOUT = {"p1_in": 0.254, "eth": 0.435, "usbc": 0.615, "p1_out": 0.255, "status": 0.606, "button": 0.710}

T = {
    "sv": {
        "title": "Koppla en Zap ETH",
        "rail": "Installationsguide &middot; Zap ETH &middot; Mainnet",
        "lede": "För installatören, på plats. Mätare med RJ12 P1-port. Online via Ethernet eller wifi. Bara P1: ingen RS485.",
        "before": "Innan du åker",
        "p1_t": "P1-porten påslagen", "p1_d": "Hos elnätsbolaget, före besöket.",
        "net_t": "Nätverk", "net_d": "Ethernet med DHCP, eller wifi 2,4&nbsp;GHz.",
        "app_t": "Appen och Bluetooth", "app_d": "Sourceful Energy, inloggad.",
        "pow_t": "Kablar", "pow_d": "RJ12 P1-kabel och nätverkskabel.",
        "meter": "ELMÄTARE", "reading": "12 345,6", "pins": "6 STIFT · CA 9,5 MM",
        "zap_above": "ZAP ETH OVANIFRÅN · EJ SKALENLIG",
        "out": "P1 UT", "status": "STATUS", "button": "KNAPP", "in": "P1 IN", "eth": "ETHERNET",
        "usbc": "USB-C", "router": "Router", "router_sub": "DHCP",
        "lights": "LAMPORNA",
        "rows": [
            (GREEN, "Grön", "", "Ström, alltid tänd"),
            (BLUE, "Blå, kort", "~0,5 s", "Startar"),
            (BLUE, "Blå, fast", "", "Väntar på appen"),
            ("off", "Blå släckt", "", "Igång"),
            (BLUE, "Blå, snabb", "KNAPP", "5–10 s: wifi rensas"),
        ],
        "s1_h": "Hitta porten",
        "s1_p": "Det lilla uttaget, som ett gammalt telefonjack. Märkt <b>P1</b>, <b>Customer</b>, <b>User</b> eller <b>RJ12</b>. Sex stift. Ofta bakom ett lock.",
        "s1_warn": "Åtta stift är fel uttag, även om det står HAN. <b>Tvinga aldrig i kabeln.</b>",
        "s2_h": "Koppla in",
        "s2_p": "P1-kabeln i <b>P1 IN</b> och i mätaren. Nätverkskabeln i <b>ETHERNET</b> och i routern. Alla ska klicka.",
        "s2_q": "USB-C 5 V om mätaren inte räcker (grön släckt). Ingen PoE.",
        "s3_h": "Kolla lamporna",
        "s3_p1": "Grön: ström. Blå kort vid start, sedan fast: Zap väntar på appen.",
        "s3_p2": "Bluetooth stänger en minut efter att nätet är uppe. Missad: koppla ur och i Zappen.",
        "s4_h": "I appen", "s4_micro": "Samma flöde som Zap P1",
        "app_steps": [
            ("Logga in", "Öppna Sourceful Energy. Saknas profil eller anläggning: skapa dem först."),
            ("<b>Lägg till en ny Zap</b>", "Under <b>Kom igång</b>, eller <b>Mer → Mina Zappar</b>."),
            ("Välj Zappen", "Blå ska lysa fast. Stå nära, välj den med flest staplar."),
            ("<b>Registrera &amp; konfigurera nätverk</b>", "Zappen hamnar i profilen du har vald."),
            ("<b>Ethernet upptäckt</b>", "<b>Hoppa över WiFi-konfiguration</b>, <b>Klar</b>. Eller wifi 2,4&nbsp;GHz, <b>Anslut</b>."),
            ("Mätaren", "<b>Elmätare → P1 / HAN-mätare → Identifiera mätare</b>."),
        ],
        "s5_h": "Klart när",
        "seen": "Det här syns",
        "ok1_q": "Appen", "ok1": "Visar mätardata inom två minuter efter <b>Mätaren är tillagd</b>.",
        "ok2_q": "Blå släckt", "ok2": "Bluetooth har stängt. Den visar inte nätet.",
        "ok3_q": "<code>ethConnected</code>", "ok3": "<code>true</code> i <code>zap.local/api/network</code>.",
        "ifnot": "Om inte",
        "f1_q": "Mätaren kunde inte identifieras", "f1": "Porten är inte påslagen, eller kabeln sitter löst. Fråga elnätsbolaget.",
        "f2_q": "Ingen <b>Ethernet upptäckt</b>", "f2": "Ingen adress från routern. Kolla kabel och port, eller använd wifi.",
        "f3_q": "Appen hittar inte Zappen", "f3": "Bluetooth har stängt. Koppla om, försök igen.",
        "wifi_h": "Byta wifi",
        "wifi_p": "Håll knappen 5–10&nbsp;s (snabb blå blink), släpp. Sedan:<br>",
        "wifi_path": ["<b>Mina Zappar</b>", "Zappen", "<b>Konfigurera om WiFi</b>", "välj&nbsp;den", "<b>Konfigurera Nätverk</b>", "nät, lösenord", "<b>Anslut</b>"],
        "card_k": "ETH", "card_m": "Bra att veta",
        "card1": "<b>Ingen RS485.</b> För en Modbus RTU-enhet: Zap P1, Zap HAN eller Zap Ultra Mini.",
        "card2": "<b>P1 UT skickar inget vidare</b> med Zap-firmware 7.0.5. Lämna den tom.",
        "card3": "En växelriktare på nätet (Modbus TCP): <b>Lägg till energienhet</b>, som på Zap P1.",
        "foot1": "firmware 7.0.5 &middot; appen 2.7.9 &middot; 2026-11-07",
        "foot2": "Ritningen ej skalenlig &middot; RJ12: Open Connector Graphics, CC BY 4.0",
    },
    "en": {
        "title": "Connect a Zap ETH",
        "rail": "Installation guide &middot; Zap ETH &middot; Mainnet",
        "lede": "For the installer, on site. Meters with an RJ12 P1 port. Online over Ethernet or Wi-Fi. P1 only: no RS485.",
        "before": "Before you go",
        "p1_t": "P1 port enabled", "p1_d": "By the grid operator, beforehand.",
        "net_t": "Network", "net_d": "Ethernet with DHCP, or 2.4&nbsp;GHz Wi-Fi.",
        "app_t": "App and Bluetooth", "app_d": "Sourceful Energy, signed in.",
        "pow_t": "Cables", "pow_d": "RJ12 P1 cable and network cable.",
        "meter": "ELECTRICITY METER", "reading": "12,345.6", "pins": "6 PINS · ABOUT 9.5 MM",
        "zap_above": "ZAP ETH FROM ABOVE · NOT TO SCALE",
        "out": "P1 OUT", "status": "STATUS", "button": "BUTTON", "in": "P1 IN", "eth": "ETHERNET",
        "usbc": "USB-C", "router": "Router", "router_sub": "DHCP",
        "lights": "THE LIGHTS",
        "rows": [
            (GREEN, "Green", "", "Power, always on"),
            (BLUE, "Blue, short", "~0.5 s", "Starting"),
            (BLUE, "Blue, solid", "", "Waiting for the app"),
            ("off", "Blue off", "", "Running"),
            (BLUE, "Blue, fast", "BUTTON", "5–10 s: Wi-Fi cleared"),
        ],
        "s1_h": "Find the port",
        "s1_p": "The small socket, like an old phone jack. Labelled <b>P1</b>, <b>Customer</b>, <b>User</b> or <b>RJ12</b>. Six pins. Often behind a cover.",
        "s1_warn": "Eight pins is the wrong socket, even if it says HAN. <b>Never force the cable.</b>",
        "s2_h": "Plug in",
        "s2_p": "The P1 cable into <b>P1 IN</b> and the meter. The network cable into <b>ETHERNET</b> and the router. All should click.",
        "s2_q": "USB-C 5 V if the meter is not enough (green off). No PoE.",
        "s3_h": "Check the lights",
        "s3_p1": "Green: power. Blue short at start, then solid: waiting for the app.",
        "s3_p2": "Bluetooth closes a minute after the network is up. Missed it: replug the Zap.",
        "s4_h": "In the app", "s4_micro": "Same flow as Zap P1",
        "app_steps": [
            ("Sign in", "Open Sourceful Energy. No profile or site yet: create them first."),
            ("<b>Onboard a new Zap</b>", "Under <b>Get started</b>, or <b>More → My Zaps</b>."),
            ("Pick the Zap", "Blue must be solid. Stand close, pick the one with most bars."),
            ("<b>Claim &amp; Configure network</b>", "The Zap joins the profile you have selected."),
            ("<b>Ethernet detected</b>", "<b>Skip WiFi setup</b>, <b>Done</b>. Or Wi-Fi 2.4&nbsp;GHz, <b>Connect</b>."),
            ("The meter", "<b>Energy Meters → P1 / HAN meter → Detect meter</b>."),
        ],
        "s5_h": "Done when",
        "seen": "You see this",
        "ok1_q": "The app", "ok1": "Shows meter data within two minutes of <b>Meter added</b>.",
        "ok2_q": "Blue off", "ok2": "Bluetooth has closed. It does not show the network.",
        "ok3_q": "<code>ethConnected</code>", "ok3": "<code>true</code> in <code>zap.local/api/network</code>.",
        "ifnot": "If not",
        "f1_q": "The meter was not detected", "f1": "Port not on, or cable not fully in. Ask the grid operator.",
        "f2_q": "No <b>Ethernet detected</b>", "f2": "No address from the router. Check cable and port, or use Wi-Fi.",
        "f3_q": "The app does not find the Zap", "f3": "Bluetooth has closed. Replug, try again.",
        "wifi_h": "Change Wi-Fi",
        "wifi_p": "Hold the button 5–10&nbsp;s (fast blue blink), let go. Then:<br>",
        "wifi_path": ["<b>My Zaps</b>", "the Zap", "<b>Reconfigure WiFi</b>", "pick&nbsp;it", "<b>Configure network</b>", "network, password", "<b>Connect</b>"],
        "card_k": "ETH", "card_m": "Good to know",
        "card1": "<b>No RS485.</b> For a Modbus RTU device: Zap P1, Zap HAN or Zap Ultra Mini.",
        "card2": "<b>P1 OUT passes nothing on</b> with Zap firmware 7.0.5. Leave it empty.",
        "card3": "An inverter on the network (Modbus TCP): <b>Add Energy Device</b>, as on the Zap P1.",
        "foot1": "firmware 7.0.5 &middot; app 2.7.9 &middot; 2026-11-07",
        "foot2": "Drawing not to scale &middot; RJ12: Open Connector Graphics, CC BY 4.0",
    },
}


def build(lang):
    return zap_ethernet.build(lang, T[lang], LAYOUT, FIELD_TESTED)


def devices():
    return {"zap-eth": zap_ethernet.device_drawing(T["en"], LAYOUT)}
