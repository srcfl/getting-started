# Blixt: field-test checklist

Walk through [the guide](README.md) on a real IPC3630 and a real IPC2210, and tick each line that matches. If something differs, write down what you saw, fix the guide, the Swedish guide and both one-pagers in the same pull request, and test that line again.

> **Warning:** Test on a unit that is not on Svenska kraftnät's reserve market. Changing, restarting or unplugging a unit that is needs Sourceful's approval for that exact action.

When every line is ticked: set **Field test** at the top of `README.md` and **Fälttest** in `README.sv.md` to the date and who tested, and set `FIELD_TESTED = True` in `onepagers/blixt.py`.

| | |
| --- | --- |
| Tested by | |
| Date | |
| Units (model and serial) | |
| Dashboard version | |
| Devices connected (models) | |

## Mount and power (both models)

- [ ] The unit snaps onto the DIN rail upright, antennas on top.
- [ ] The green power plug: **VIN+** on top, **GND** below. 9–36 V DC starts it.
- [ ] **PWR** is red and solid with a good supply; **ACT** green blinks.
- [ ] The **PROGRAMMING** port is under the DIN bracket.
- [ ] Online after about a minute; the first update takes 10–20 minutes.

## Network

- [ ] IPC3630: the site network works on **1000M**.
- [ ] IPC2210: the site network works on **ETH0**.
- [ ] Sourceful's dashboard address opens from a laptop on the site network; the IP from the router works too.
- [ ] The dashboard does not answer on the 4G address.

## RS-485 (IPC3630)

- [ ] The lower plug's labels read **IGND**, **A2**, **B2** on the left and **IGND**, **A4**, **B4** on the right.
- [ ] A device on COM2 works as `/dev/ttyAMA4`; on COM4 as `/dev/ttyAMA3`.
- [ ] The **COM2** or **COM4** light blinks with Modbus traffic.
- [ ] With the Blixt at a bus end, 120 Ω between A and B at the plug is enough; the case stays closed.
- [ ] The RTU form is pre-filled with `/dev/ttyAMA0`.

## Site and devices

- [ ] **Flow → Site configuration** defaults to 63 A, 3 phases, 230 V.
- [ ] A site meter without current and voltage per phase limits the batteries and shows a banner.
- [ ] **Devices → Add device** lists drivers and versions from the registry; **↻ Refresh** fetches a new one.
- [ ] A TCP device (IP, port 502, unit ID) shows `live`.
- [ ] **Gateway → Modbus proxy** exists.

## Done when

- [ ] **Flow** shows power, state of charge and frequency within seconds.
- [ ] **Manual** at about 10 % of rated power: plus charges, minus discharges, deviation near 0, **FAULT** off.
- [ ] With an aggregator in control, the controls are greyed out.

## The one-pager

- [ ] Printed on A4, both languages: every step matches what you saw.
