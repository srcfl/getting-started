# Zap ETH: field-test checklist

Walk through [the guide](README.md) on a real Zap ETH and tick each line that matches. If something differs, write down what you saw, fix the guide, the Swedish guide and both one-pagers in the same pull request, and test that line again.

When every line is ticked: set **Field test** at the top of `README.md` and **Fälttest** in `README.sv.md` to the date and who tested, and set `FIELD_TESTED = True` in `onepagers/zap_eth.py`.

| | |
| --- | --- |
| Tested by | |
| Date | |
| Zap firmware | |
| Hardware version (on the label, if any) | |
| App version and language | |
| Meter (brand and model) | |
| Network (Ethernet, Wi-Fi or both) | |

## Ports and power

- [ ] IN side, from the left: P1 IN, Ethernet, USB-C, and the green power light (next to USB-C, or inside P1 IN). OUT side, from the left: button, blue status light, P1 OUT.
- [ ] The P1 cable clicks into **P1 IN** and the meter; the network cable into **Ethernet**.
- [ ] The meter powers the Zap without USB-C: green is solid (note the meter and its P1 version).

## The lights and the button

- [ ] At power-on: blue for about half a second, then blue, solid.
- [ ] With the network cable in, blue goes off about a minute after the Zap gets an address, if the app has not connected.
- [ ] Unplugging and plugging in again gives blue, solid again (no Wi-Fi saved).
- [ ] Holding the button 2–5 s: slow blink; letting go restarts.
- [ ] Holding 5–10 s: fast blink; letting go clears Wi-Fi and gives blue, solid after the restart.

## In the app, over Ethernet

- [ ] **Onboard a new Zap → Claim & Configure network** works (SV: **Lägg till en ny Zap → Registrera & konfigurera nätverk**).
- [ ] **WiFi Setup** shows **Ethernet detected**; **Skip WiFi setup** gives **Connected via Ethernet** and **Done**.
- [ ] `http://zap.local/api/network` shows `"ethConnected": true`, `"internetConnected": true`, `"mqttConnected": true`.

## In the app, over Wi-Fi (another unit, or after a factory reset)

- [ ] Without the network cable, **WiFi Setup → Connect → Done** works as on the Zap P1.

## The meter

- [ ] **Energy Meters → P1 / HAN meter → Detect meter** shows **Meter added**.
- [ ] Meter data shows in the app within two minutes.
- [ ] A device on **P1 OUT** gets no data (expected with firmware 7.0.5).

## The one-pager

- [ ] Printed on A4, both languages: every step matches what you saw.
