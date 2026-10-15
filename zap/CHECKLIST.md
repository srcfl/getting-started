# Zap P1: field-test checklist

Walk through [the guide](README.md) on a real Zap P1 and tick each line that matches. If something differs, write down what you saw, fix the guide, the Swedish guide and both one-pagers in the same pull request, and test that line again.

When every line is ticked: set **Field test** at the top of `README.md` and **Fälttest** in `README.sv.md` to the date and who tested, and set `FIELD_TESTED = True` in `onepagers/zap.py`.

| | |
| --- | --- |
| Tested by | |
| Date | |
| Zap firmware | |
| App version and language | |
| Meter (brand and model) | |

## Port and power

- [ ] The RJ12 cable is already in **P1 IN**, on the long side with USB-C.
- [ ] The cable clicks into the meter's P1 port.
- [ ] Without USB-C, on an enabled meter: the green light in **P1 IN** is solid.

## Lights and button

- [ ] At power-on, blue blinks once.
- [ ] With no saved Wi-Fi, blue is solid.
- [ ] Holding the button 2–5 s: blue blinks slowly. Letting go restarts the Zap.
- [ ] Holding 5–10 s: blue blinks fast. Letting go clears Wi-Fi, and blue goes solid.
- [ ] Holding more than 10 s: blue is solid. Letting go factory-resets (test on a spare unit).

## In the app

- [ ] **Get started → Onboard a new Zap** (SV: **Kom igång → Lägg till en ny Zap**) opens the Bluetooth scan.
- [ ] **More → My Zaps → Add a new Zap** opens the same scan.
- [ ] The Zap shows up with signal bars; the list is not sorted.
- [ ] **Claim & Configure network** (SV: **Registrera & konfigurera nätverk**) claims it.
- [ ] **WiFi Setup** lists networks; **Enter manually** exists; **Connect** connects within 30 s.
- [ ] **WiFi Connected** → name → **Done**.
- [ ] Blue goes off about a minute after Wi-Fi is up.

## The meter

- [ ] Before the meter is added: no green data blink and no meter data in the app.
- [ ] **Connect your meter, inverter or charger → Onboard New Device → Energy Meters → P1 / HAN meter → Detect meter** (SV: **Elmätare → P1 / HAN-mätare → Identifiera mätare**) shows **Meter added**, then **Done**.
- [ ] The green light in **P1 OUT** blinks about every 10 s.
- [ ] Meter data shows in the app within two minutes.

## From a laptop

- [ ] `http://zap.local/api/network`: `"internetConnected": true`, `"mqttConnected": true`, an `rssi` value.
- [ ] `http://zap.local/api/devices` lists the meter with an `sn` starting `p1m-`; `/api/devices/<sn>/data/json` shows live values.
- [ ] The router lists the Zap as `zap-<serial>`.

## Change Wi-Fi

- [ ] Hold 5–10 s, let go. The app shows **Unable to reach Zap** and **Reconfigure WiFi**.
- [ ] **Reconfigure WiFi** → tap the Zap → **Configure network** → network and password → **Connect** works.

## Inverter

- [ ] **More** → site → **Energy devices → Add Energy Device → Inverters** → model → **Host Address**, **Port**, **Unit ID** → **Continue** → **Connect Device** → **Enable Resources** → **Done**.
- [ ] The inverter's data shows in the app.

## The one-pager

- [ ] Printed on A4, both languages: every step matches what you saw.
