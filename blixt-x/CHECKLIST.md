# Blixt X: field-test checklist

Walk through [the guide](README.md) on a real RAK Hotspot V2 running Blixt X 2.0.1, and tick each line that matches. If something differs, write down what you saw, fix the guide, the Swedish guide and both one-pagers in the same pull request, and test that line again.

When every line is ticked: set **Field test** at the top of `README.md` and **Fälttest** in `README.sv.md` to the date and who tested, and set `FIELD_TESTED = True` in `onepagers/blixt_x.py`.

| | |
| --- | --- |
| Tested by | |
| Date | |
| Blixt X version | |
| App version and language | |
| Devices connected (models) | |

## The gateway

- [ ] The long side has USB-C and the round pairing button; the front has the antenna, TF slot and two lights; the back has Ethernet.
- [ ] With the antenna on, Ethernet in and USB-C power: **red** is solid and **green** blinks while it starts.
- [ ] With a weak power supply, red blinks.

## Bluetooth

- [ ] After start it shows up in the app as **blixt-&lt;serial&gt;**.
- [ ] After 3 minutes it no longer shows up.
- [ ] Holding the pairing button 3 s, or double-clicking it, makes it show up again for 3 minutes.

## In the app, on Ethernet

- [ ] **Onboard a new Zap** → pick **blixt-…** → **Claim & Configure network** claims it.
- [ ] **WiFi Setup** opens; there is no **Skip WiFi setup**.
- [ ] Backing out of **WiFi Setup** leaves the gateway claimed and online.
- [ ] `http://blixt.local/api/network` shows `"internetConnected": true` and `"mqttConnected": true`.

## Devices

- [ ] **More → Energy devices → Add Energy Device** → type → model → IP, port, unit ID → **Connect Device** adds a Modbus TCP device.
- [ ] `http://blixt.local/api/devices` lists it, and the app shows its data.

## The one-pager

- [ ] Printed on A4, both languages: every step matches what you saw.
