# Zap HAN: field-test checklist

Walk through [the guide](README.md) on a real Zap HAN and tick each line that matches. If something differs, write down what you saw, fix the guide, the Swedish guide and both one-pagers in the same pull request, and test that line again.

When every line is ticked: set **Field test** at the top of `README.md` and **Fälttest** in `README.sv.md` to the date and who tested, and set `FIELD_TESTED = True` in `onepagers/zap_han.py`.

| | |
| --- | --- |
| Tested by | |
| Date | |
| Zap HAN firmware | |
| App version and language | |
| Meter (brand and model) | |

## Port, cable and power

- [ ] The cable that comes with it has RJ12 on one end and RJ45 on the other.
- [ ] RJ45 clicks into the meter's HAN port; RJ12 clicks into the Zap's **IN** socket, on the long side with USB-C.
- [ ] Without USB-C the Zap HAN does not start (no light).
- [ ] With a 5 V, 1 A USB-C charger it starts.

## The light and the button

- [ ] The light sits in the RJ12 socket; there is no separate blue light.
- [ ] At power-on: rainbow for about a second.
- [ ] With no saved Wi-Fi: blue, solid.
- [ ] Holding the button 2–5 s: slow blue blink; letting go restarts.
- [ ] Holding 5–10 s: fast blue blink; letting go clears Wi-Fi, and blue goes solid.
- [ ] Holding more than 10 s: solid; letting go factory-resets (test on a spare unit).

## In the app

- [ ] The onboarding is the same as the Zap P1: **Onboard a new Zap → Claim & Configure network → WiFi Setup → Connect → Done** (SV: **Lägg till en ny Zap → Registrera & konfigurera nätverk → WiFi-inställningar → Anslut → Klar**).
- [ ] The light goes off about a minute after Wi-Fi is up.

## The meter

- [ ] **Energy Meters → P1 / HAN meter → Detect meter** shows **Meter added**.
- [ ] Meter data shows in the app within two minutes.
- [ ] `http://zap.local/api/devices` lists the meter with `"detected_type": "han_uart"`.
- [ ] On a meter whose HAN port is off: **The meter was not detected** shows.

## Change Wi-Fi

- [ ] Hold 5–10 s, let go → **Reconfigure WiFi** → tap the Zap → **Configure network** → network and password → **Connect** works.

## The one-pager

- [ ] Printed on A4, both languages: every step matches what you saw.
