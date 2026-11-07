# Zap Ultra X2: field-test checklist

Walk through [the guide](README.md) on a real Zap Ultra X2 and tick each line that matches. If something differs, write down what you saw, fix the guide, the Swedish guide and both one-pagers in the same pull request, and test that line again.

When every line is ticked: set **Field test** at the top of `README.md` and **Fälttest** in `README.sv.md` to the date and who tested, and set `FIELD_TESTED = True` in `onepagers/zap_ultra_x2.py`.

| | |
| --- | --- |
| Tested by | |
| Date | |
| Zap firmware | |
| App version and language | |
| Meter (brand and model) | |
| Network (Ethernet, Wi-Fi or both) | |

## Ports and power

- [ ] IN side, from the left: P1 IN, Ethernet, USB-C, the 5-pin module terminal. OUT side, from the left: button, status light, P1 OUT.
- [ ] Which modules are fitted, left and right slot (note them).
- [ ] The P1 cable clicks into **P1 IN** and the meter; the network cable into **Ethernet**.
- [ ] The meter powers the Zap without USB-C (note the meter and its P1 version).
- [ ] With something on **P1 OUT**, USB-C is needed.

## The light and the button

- [ ] At power-on: rainbow for about a second, then blue, solid.
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

## RS485 (with an RS485 module in the left slot)

- [ ] The terminal's pins, counted from USB-C, are **B−, A+** (left slot), **GND**, **B−, A+** (right slot).
- [ ] With **A+** to the device's A, **B−** to its B and **GND** to its GND, **Modbus RTU** in the app adds the device and its data shows in the app.

## The one-pager

- [ ] Printed on A4, both languages: every step matches what you saw.
