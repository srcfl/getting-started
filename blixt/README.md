# Blixt: getting started

> **Applies to:** the Blixt gateway on EDATEC ED-IPC3630 (IPC3600 series) or ED-IPC2210, dashboard 3.x
> **Last verified:** 2026-10-15, against `blixt-gateway` on `main` (491197b) and EDATEC's manuals
> **For:** the installer commissioning a Blixt on a site

Blixt is an industrial gateway that controls batteries, hybrid inverters, meters and EV chargers on commercial and industrial sites. It reads and controls the devices over Modbus RTU or TCP, keeps the site within its fuse and export limits, and sends measurements to Sourceful. Everything is set up in the Blixt dashboard on the site network.

**Going on site?** Print the one-pager: [English](blixt-one-pager-en.pdf) · [Svenska](blixt-one-pager-sv.pdf). Svenska: [README.sv.md](README.sv.md).

[![The Blixt one-pager](images/one-pager-en.png)](blixt-one-pager-en.pdf)

## The two models

| IPC3630 | IPC2210 |
| --- | --- |
| ![Blixt on the IPC3630, front and side](../assets/devices/blixt-ipc3630.svg) | ![Blixt on the IPC2210, front and side](../assets/devices/blixt-ipc2210.svg) |

Sourceful installs both. They mount upright on a DIN rail, with the antennas on top and every connector on the narrow front.

| | IPC3630 | IPC2210 |
| --- | --- | --- |
| Size (front × height × depth) | 55 × 143 × 100 mm | 34 × 143 × 100 mm |
| Power | 9–36 V DC, green 2-pin plug, **VIN+** on top, **GND** below | Same |
| Ethernet | **1000M** (the site network) and **100M** | **ETH0** (the site network), **ETH1**, **ETH2**, all gigabit |
| RS-485 | **COM2** and **COM4** on the lower 6-pin plug | None |
| Lights | **PWR** red, **ACT** green, **COM1–COM4**, plus lights for inputs and outputs Blixt does not use | **PWR** red, **ACT** green |
| Antennas | WiFi/BT and 4G on the top end, if the unit was ordered with them | Same |

The IPC3630 front, top to bottom: the lights, the power plug, the upper serial plug (COM1 and COM3), the lower serial plug (COM2 and COM4), then the 1000M and 100M Ethernet ports. The plugs to the right of them (inputs, CAN, outputs) are not used by Blixt.

## What Sourceful does before you go

You should receive a prepared unit. Ask Sourceful before you leave if any of this is unclear:

- The unit has the right software and is connected to the right Sourceful environment.
- The unit's identity is registered with Sourceful. Without it, no measurements arrive. Sourceful does this; there is no step for the installer.
- On the IPC3630: the serial ports are enabled for the unit.
- Who terminates the RS-485 bus. The Blixt has no termination from the factory: its 120 Ω jumpers sit on the circuit board inside the case and are open.
- You know which inverters, batteries and meters to connect, and there is a driver for each model.

> **Warning:** If the site takes part in Svenska kraftnät's reserve market: change nothing in the dashboard, do not restart and do not unplug anything without Sourceful's approval for that exact action.

## Bring

- [ ] The Blixt, with its antennas if it has them
- [ ] A 9–36 V DC supply
- [ ] An Ethernet cable to the site network, with DHCP
- [ ] Twisted-pair cable for RS-485 if any device connects by serial (IPC3630 only)
- [ ] Model, IP address, port and unit ID for every inverter, battery and meter
- [ ] The site's fuse size, number of phases and voltage
- [ ] A laptop on the same network as the Blixt

## 1. Mount and connect

1. Snap the Blixt onto the DIN rail, upright, antennas on top. Screw on the antennas: **WiFi/BT** and **4G**.
2. Connect Ethernet to the site network. IPC3630: the **1000M** port. IPC2210: **ETH0**. The Blixt gets its address over DHCP. 4G is the backup link.
3. Connect power to the green plug: **VIN+** on top, **GND** below, 9–36 V DC. Check the polarity before you switch on.

Do not use the **PROGRAMMING** port (Micro-USB, under the DIN bracket). It is only for imaging the unit.

- **PWR red, solid:** the unit has power. **PWR blinking:** the supply is bad. Cut the power and check it.
- **ACT green:** blinks with storage activity.

The unit is online after about a minute. The first time, it downloads its software, about 1.6 GB. That takes 10–20 minutes, longer over 4G. Do not cut the power meanwhile.

## 2. Wire RS-485 (IPC3630 only)

Use the **lower** serial plug. Its left column is COM2, its right column COM4. The labels are printed next to the plug.

| Port | Plug labels, top to bottom | Device in the dashboard |
| --- | --- | --- |
| COM2 | **IGND**, **A2**, **B2** (left column) | `/dev/ttyAMA4` |
| COM4 | **IGND**, **A4**, **B4** (right column) | `/dev/ttyAMA3` |

1. Connect A to A, B to B and IGND to the device's GND. The ports are isolated, so GND must be connected.
2. Terminate only the two ends of the bus with 120 Ω. The Blixt is not terminated from the factory. If it sits at one end of the bus, that end needs 120 Ω: either its jumper inside the case (J22 for COM2, J24 for COM4) or a resistor across A and B. Agree with Sourceful before you go which it is.
3. A device can have only one Modbus master. If another system needs to read the same device, use **Gateway → Modbus proxy** in the dashboard instead of a second master.

The **COM2** or **COM4** light blinks when there is traffic on the line. It is a quick wiring check.

> **Warning:** Do not use the upper plug (COM1 and COM3) for Modbus. They are not verified for it, and on some variants they are RS-232.

The IPC2210 has no serial port. Connect its devices over the network (Modbus TCP).

## 3. Open the dashboard

From a laptop on the same network: `http://blixt-<serial>.local/`.

Use the serial in the address. Plain `blixt.local` goes wrong when there is more than one Blixt on the network. The dashboard does not answer on the 4G address.

> **Warning:** Whoever reaches the dashboard can control the battery. Keep the Blixt on a protected network, and never open it to the internet.

## 4. Set up the site

Do this **before** anything is controlled.

1. Go to **Flow → Site configuration**.
2. Enter the fuse size, the number of phases and the voltage. The default is 63 A, 3 phases, 230 V.
3. Choose the site meter. It must report current and voltage on every phase. If it does not, the batteries are limited and a banner says why.

## 5. Add the devices

For each inverter, battery and meter:

1. Go to **Devices** and choose **Add device**.
2. Pick the driver and the **version** from the list. The list comes from Sourceful's driver registry. If a new version is missing, press **↻ Refresh**.
3. Always pin a version. A device without a pinned version follows the latest one and can change behaviour without anyone noticing.
4. Choose the connection:
   - **TCP:** IP address, port (usually 502) and unit ID.
   - **RTU** (IPC3630): serial port (`/dev/ttyAMA4` for COM2, `/dev/ttyAMA3` for COM4), baud rate, parity and unit ID.

> **Warning:** The RTU form is pre-filled with `/dev/ttyAMA0`. On the IPC3630 that is COM3. Change it to COM2 or COM4.

## 6. Done when

- **Devices:** every device shows `live`. `timeout`, `stale` or `no data` means it is not answering.
- **Flow:** power, state of charge (SoC) and frequency show within a few seconds.
- **Battery test:** in **Manual** mode, run about 10 % of the battery's rated power. Positive power charges, negative discharges. The deviation should stay close to 0 and **FAULT** should be off.

Sourceful connects the Blixt to an aggregator, not the installer. While an aggregator is in control, the local controls are locked.

## Troubleshooting

| What you see | Probably | Do this |
| --- | --- | --- |
| An RTU device shows `timeout` or `no data` | Wrong plug or port (the upper plug, or the pre-filled `/dev/ttyAMA0`), A and B swapped, wrong baud rate or unit ID, no termination | Use COM2 or COM4 on the lower plug. Check A/B, the settings and the termination. |
| The COM light does not blink | No traffic on that line | Check that the device uses the same port in the dashboard as the wire is on. |
| The same garbage at every baud rate | The serial ports are not enabled for the unit | Contact Sourceful. |
| Serial errors after you changed a device's port and restarted control | The old port is still held open | Contact Sourceful for a restart of the control service. |
| PWR blinks | The supply is too weak or wrong | Cut the power and check the supply: 9–36 V DC, VIN+ on top. |
| The dashboard does not open | Wrong address, or several Blixts with the same name | Use `blixt-<serial>.local` from a laptop on the same network. |
| The controls are greyed out | An aggregator is in control | That is intended. Contact Sourceful if you need local control. |
| The battery charges but does not discharge | The inverter's export protection (anti-backflow) is on | Check that setting in the inverter. |
| Power settles just below the setpoint | The fuse limit is capping it | Check **Site configuration**. |
| The unit never shows up at Sourceful | The first update is still running, or the identity is not registered | Wait 20 minutes, then contact Sourceful. |

## Open questions

- IPC2210: serial devices would need a USB-to-RS-485 adapter. That is not documented or tested for Blixt.
- When the Blixt sits at a bus end: does Sourceful fit the jumper before delivery, or does the installer add a resistor at the plug? EDATEC gives no procedure for opening the case.
- Is the serial printed on the unit the same one used in `blixt-<serial>.local`?
- The existing quick start in `blixt-gateway` says Blixt runs on USB-C 5 V. That matches neither model.

## Sources

- EDATEC: [IPC3630 user manual](https://edatec.cn/docs/ipc3630/um/1-hardware/) and [datasheet](https://edatec.cn/docs/ipc3630/ds/) (front panel, power plug, serial plugs and pins, termination jumpers, lights, ports), [IPC2200 user manual](https://edatec.cn/docs/ipc2200/um/1-hardware/) and [datasheet](https://edatec.cn/docs/ipc2200/ds/) (IPC2210 front panel, power, Ethernet)

The `srcfl/blixt-gateway` repository is internal. Paths refer to `main` at 491197b.

- `README.md`: what Blixt is, provisioning and identity registration (done by Sourceful with an admin key), first boot, drivers from the registry
- `docs/specs/ipc-3600-specs.md`: COM ports and their Linux devices, which ports to use for Modbus, lights under balenaOS
- `docs/gateway/DASHBOARD-ACCESS.md`: dashboard address and network protection
- `services/dashboard/README.md`: device states, aggregator lock, driver choice and version pinning
- `docs/specs/site-limits.md`: fuse, phases and the site-meter requirement
- `docs/gateway/Sourceful-Gateway-Battery-and-SvK-Tests.html`: the battery test in Manual mode
- `services/dashboard/web/src/.../DeviceForm.tsx`: the pre-filled `/dev/ttyAMA0` and connection types
- Fleets and units, read-only listing on 2026-10-15
- The one-pager is built from [onepagers/blixt.py](../onepagers/blixt.py)
