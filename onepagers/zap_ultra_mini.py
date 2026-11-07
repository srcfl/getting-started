"""Zap Ultra Mini one-pager: connect a Zap Ultra Mini to a P1 meter, over Ethernet or Wi-Fi.

Sources:
- The hardware vendor's documentation (2026-11-07): the IN side has, from left, P1 IN,
  Ethernet, USB-C, a power light and the 3-pin RS485 terminal; the OUT side has the button,
  the status light, a P1 OUT light and P1 OUT. RS485 pins A+, B-, GND counted from USB-C.
  A version 5.0 meter powers it; older meters, and a device on P1 OUT, need USB-C. No PoE.
- srcfl/srcful-zap-x-firmware v7.0.5 (346754de): zap-ultra-mini.h (ESP32-S3, W5500, WS2812
  status light, button GPIO 0, P1 in 18 / out 21, RS485 on UART2), main.cpp (rainbow at
  boot; Bluetooth starts without saved Wi-Fi, also with Ethernet), main_loop.cpp (blue while
  Bluetooth waits; Bluetooth stops 60 s after Wi-Fi or Ethernet is up; button 2/5/10 s),
  eth_manager.cpp (Ethernet by DHCP, no static IP), fw_controller/API.md (ethConnected).
- The app 2.7.9 (srcful-flutter-app v2.7.9): the onboarding is the Zap P1's; with Ethernet up
  the Wi-Fi screen shows "Ethernet detected" and "Skip WiFi setup" (zap_wifi_setup_screen.dart).
- Sourceful's test rig, 2026-11-07: a Zap Ultra Mini on 7.0.5 reads a P1 meter and an SDM630
  over RS485.
"""
import zap_ethernet
from common import BLUE

# Set to True when CHECKLIST.md is ticked off on real hardware.
FIELD_TESTED = False

LAYOUT = {
    "p1_in": 0.266, "eth": 0.445, "usbc": 0.624, "rs485": (0.775, 9.0, ("A+", "B−", "GND")),
    "p1_out": 0.270, "status": 0.615, "button": 0.716,
}

T = {
    "sv": {
        "title": "Koppla en Zap Ultra Mini",
        "rail": "Installationsguide &middot; Zap Ultra Mini &middot; Mainnet",
        "lede": "För installatören, på plats. Mätare med RJ12 P1-port. Online via Ethernet eller wifi. RS485 för en mätare eller växelriktare.",
        "before": "Innan du åker",
        "p1_t": "P1-porten påslagen", "p1_d": "Hos elnätsbolaget, före besöket.",
        "net_t": "Nätverk", "net_d": "Ethernet med DHCP, eller wifi 2,4&nbsp;GHz.",
        "app_t": "Appen och Bluetooth", "app_d": "Sourceful Energy, inloggad.",
        "pow_t": "Kablar", "pow_d": "RJ12 P1-kabel och nätverkskabel.",
        "meter": "ELMÄTARE", "reading": "12 345,6", "pins": "6 STIFT · CA 9,5 MM",
        "zap_above": "ZAP ULTRA MINI OVANIFRÅN · EJ SKALENLIG",
        "out": "P1 UT", "status": "STATUS", "button": "KNAPP", "in": "P1 IN", "eth": "ETHERNET",
        "usbc": "USB-C", "rs485": "RS485", "router": "Router", "router_sub": "DHCP",
        "lights": "LAMPAN",
        "rows": [
            ("rainbow", "Regnbåge", "~1 s", "Startar"),
            (BLUE, "Blå, fast", "", "Väntar på appen"),
            ("off", "Släckt", "", "Igång, eller ingen ström"),
            (BLUE, "Blå, snabb", "KNAPP", "5–10 s: wifi rensas"),
        ],
        "s1_h": "Hitta porten",
        "s1_p": "Det lilla uttaget, som ett gammalt telefonjack. Märkt <b>P1</b>, <b>Customer</b>, <b>User</b> eller <b>RJ12</b>. Sex stift. Ofta bakom ett lock.",
        "s1_warn": "Åtta stift är fel uttag, även om det står HAN. <b>Tvinga aldrig i kabeln.</b>",
        "s2_h": "Koppla in",
        "s2_p": "P1-kabeln i <b>P1 IN</b> och i mätaren. Nätverkskabeln i <b>ETHERNET</b> och i routern. Alla ska klicka.",
        "s2_q": "USB-C 5 V om P1 UT används eller mätaren inte räcker. Ingen PoE.",
        "s3_h": "Kolla lampan",
        "s3_p1": "Regnbåge en sekund: Zap startar. Sedan blå, fast: den väntar på appen.",
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
        "ok2_q": "Lampan släckt", "ok2": "Bluetooth har stängt. Den visar inte nätet.",
        "ok3_q": "<code>ethConnected</code>", "ok3": "<code>true</code> i <code>zap.local/api/network</code>.",
        "ifnot": "Om inte",
        "f1_q": "Mätaren kunde inte identifieras", "f1": "Porten är inte påslagen, eller kabeln sitter löst. Fråga elnätsbolaget.",
        "f2_q": "Ingen <b>Ethernet upptäckt</b>", "f2": "Ingen adress från routern. Kolla kabel och port, eller använd wifi.",
        "f3_q": "Appen hittar inte Zappen", "f3": "Bluetooth har stängt. Koppla om, försök igen.",
        "wifi_h": "Byta wifi",
        "wifi_p": "Håll knappen 5–10&nbsp;s (snabb blå blink), släpp. Sedan:<br>",
        "wifi_path": ["<b>Mina Zappar</b>", "Zappen", "<b>Konfigurera om WiFi</b>", "välj&nbsp;den", "<b>Konfigurera Nätverk</b>", "nät, lösenord", "<b>Anslut</b>"],
        "card_k": "RS485", "card_m": "Modbus RTU",
        "card1": "Stiften från USB-C: <b>A+, B−, GND</b>. A+ till enhetens A, B− till B, GND till GND.",
        "card2": "I appen: <b>Lägg till energienhet</b>, modellen, <b>Modbus RTU</b>, sedan enhetens seriella inställningar.",
        "card3": "<b>Annan ordning än Zap P1 och Zap HAN.</b> Koppla med strömmen av.",
        "foot1": "firmware 7.0.5 &middot; appen 2.7.9 &middot; 2026-11-07",
        "foot2": "Ritningen ej skalenlig &middot; RJ12: Open Connector Graphics, CC BY 4.0",
    },
    "en": {
        "title": "Connect a Zap Ultra Mini",
        "rail": "Installation guide &middot; Zap Ultra Mini &middot; Mainnet",
        "lede": "For the installer, on site. Meters with an RJ12 P1 port. Online over Ethernet or Wi-Fi. RS485 for a meter or inverter.",
        "before": "Before you go",
        "p1_t": "P1 port enabled", "p1_d": "By the grid operator, beforehand.",
        "net_t": "Network", "net_d": "Ethernet with DHCP, or 2.4&nbsp;GHz Wi-Fi.",
        "app_t": "App and Bluetooth", "app_d": "Sourceful Energy, signed in.",
        "pow_t": "Cables", "pow_d": "RJ12 P1 cable and network cable.",
        "meter": "ELECTRICITY METER", "reading": "12,345.6", "pins": "6 PINS · ABOUT 9.5 MM",
        "zap_above": "ZAP ULTRA MINI FROM ABOVE · NOT TO SCALE",
        "out": "P1 OUT", "status": "STATUS", "button": "BUTTON", "in": "P1 IN", "eth": "ETHERNET",
        "usbc": "USB-C", "rs485": "RS485", "router": "Router", "router_sub": "DHCP",
        "lights": "THE LIGHT",
        "rows": [
            ("rainbow", "Rainbow", "~1 s", "Starting"),
            (BLUE, "Blue, solid", "", "Waiting for the app"),
            ("off", "Off", "", "Running, or no power"),
            (BLUE, "Blue, fast", "BUTTON", "5–10 s: Wi-Fi cleared"),
        ],
        "s1_h": "Find the port",
        "s1_p": "The small socket, like an old phone jack. Labelled <b>P1</b>, <b>Customer</b>, <b>User</b> or <b>RJ12</b>. Six pins. Often behind a cover.",
        "s1_warn": "Eight pins is the wrong socket, even if it says HAN. <b>Never force the cable.</b>",
        "s2_h": "Plug in",
        "s2_p": "The P1 cable into <b>P1 IN</b> and the meter. The network cable into <b>ETHERNET</b> and the router. All should click.",
        "s2_q": "USB-C 5 V if P1 OUT is used or the meter is not enough. No PoE.",
        "s3_h": "Check the light",
        "s3_p1": "Rainbow for a second: starting. Then blue, solid: waiting for the app.",
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
        "ok2_q": "The light is off", "ok2": "Bluetooth has closed. It does not show the network.",
        "ok3_q": "<code>ethConnected</code>", "ok3": "<code>true</code> in <code>zap.local/api/network</code>.",
        "ifnot": "If not",
        "f1_q": "The meter was not detected", "f1": "Port not on, or cable not fully in. Ask the grid operator.",
        "f2_q": "No <b>Ethernet detected</b>", "f2": "No address from the router. Check cable and port, or use Wi-Fi.",
        "f3_q": "The app does not find the Zap", "f3": "Bluetooth has closed. Replug, try again.",
        "wifi_h": "Change Wi-Fi",
        "wifi_p": "Hold the button 5–10&nbsp;s (fast blue blink), let go. Then:<br>",
        "wifi_path": ["<b>My Zaps</b>", "the Zap", "<b>Reconfigure WiFi</b>", "pick&nbsp;it", "<b>Configure network</b>", "network, password", "<b>Connect</b>"],
        "card_k": "RS485", "card_m": "Modbus RTU",
        "card1": "Pins from USB-C: <b>A+, B−, GND</b>. A+ to the device's A, B− to B, GND to GND.",
        "card2": "In the app: <b>Add Energy Device</b>, the model, <b>Modbus RTU</b>, then the device's serial settings.",
        "card3": "<b>Not the order of the Zap P1 or Zap HAN.</b> Wire with the power off.",
        "foot1": "firmware 7.0.5 &middot; app 2.7.9 &middot; 2026-11-07",
        "foot2": "Drawing not to scale &middot; RJ12: Open Connector Graphics, CC BY 4.0",
    },
}


def build(lang):
    return zap_ethernet.build(lang, T[lang], LAYOUT, FIELD_TESTED)


def devices():
    return {"zap-ultra-mini": zap_ethernet.device_drawing(T["en"], LAYOUT)}
