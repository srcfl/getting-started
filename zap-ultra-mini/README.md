# Zap Ultra Mini: getting started

> **Applies to:** Zap Ultra Mini (for meters with an RJ12 P1 port), firmware 7.0.5 or later, the Sourceful Energy app 2.7.9 on mainnet  
> **Last verified:** 2026-11-07, against the sources at the bottom  
> **For:** the installer on site  
> **Field test:** not done yet. Checklist: [CHECKLIST.md](CHECKLIST.md)

The Zap Ultra Mini reads the electricity meter's P1 port (RJ12), like the [Zap P1](../zap/README.md), and sends the data to the Sourceful Energy app over **Ethernet or Wi-Fi**. Its RS485 terminal takes a meter or inverter over Modbus RTU.

Does the meter only have an RJ45 HAN port? Then you need the [Zap HAN](../zap-han/README.md).

**Going on site?** Print the one-pager: [English](zap-ultra-mini-one-pager-en.pdf) · [Svenska](zap-ultra-mini-one-pager-sv.pdf). Svenska: [README.sv.md](README.sv.md).

[![The Zap Ultra Mini one-pager](images/one-pager-en.png)](zap-ultra-mini-one-pager-en.pdf)

## The Zap Ultra Mini

![The Zap Ultra Mini from above, not to scale: P1 IN, Ethernet, USB-C and the RS485 terminal on one long side; P1 OUT, the status light and the button on the other](../assets/devices/zap-ultra-mini.svg)

The drawing shows the order of the ports, not the real proportions.

| IN side, from the left | OUT side, from the left |
| --- | --- |
| **P1 IN** (RJ12): the cable to the meter | The **button** |
| **Ethernet** (RJ45) | The **status light** |
| **USB-C**: power, when needed | A light for **P1 OUT** |
| A power light | **P1 OUT** (RJ12) |
| The **RS485** terminal: **A+, B−, GND**, counted from USB-C | |

## Before you go

- [ ] **The P1 port is enabled by the grid operator.** Usually on their website, otherwise by phone.
- [ ] **A network:** an Ethernet cable to a router or switch port that hands out addresses (DHCP), or the name and password of a 2.4 GHz Wi-Fi network.
- [ ] **The Sourceful Energy app**, signed in, with a profile and a site. **Bluetooth on** on the phone.
- [ ] **An RJ12 P1 cable** and, for Ethernet, a network cable.
- [ ] **A USB-C charger** (5 V) if something will be plugged into P1 OUT, or if the meter is older than P1 version 5.0.

## 1. Find the port on the meter

The small socket, like an old telephone jack: RJ12, six pins. It is labelled **P1**, **Customer**, **User** or **RJ12**, and often sits behind a small cover.

> **Warning:** A wider socket with eight pins (RJ45) is the wrong one, even if it says HAN. Never use an adapter and never force the cable. A meter with only an RJ45 HAN port needs the [Zap HAN](../zap-han/README.md).

## 2. Plug in

1. Push the P1 cable into the Zap's **P1 IN**, on the long side with Ethernet and USB-C, and the other end into the meter's P1 port. Both should click.
2. For Ethernet: a network cable from **Ethernet** to the router or switch. The Zap gets its address by DHCP; there is no setting for a fixed address.

A meter with P1 version 5.0 powers the Zap through the cable. Plug in USB-C (5 V) as well when:

- something is plugged into **P1 OUT**. This one is required.
- the meter is older and does not give enough power: the light stays dark.

The Zap cannot take power from the network cable (no PoE).

## 3. Check the light

- **Rainbow** for about a second: the Zap is starting.
- **Blue, solid:** the Zap is waiting for the app over Bluetooth. Go to step 4.

As long as no Wi-Fi is saved, Bluetooth opens at every start. Once the Zap is online, over Ethernet or Wi-Fi, Bluetooth closes after **one minute**. Have the app ready before you plug in the network cable. Missed it? Unplug the Zap (P1 cable and USB-C) and plug it in again.

> **Warning:** Holding the button longer than 10 seconds and letting go is a factory reset: it deletes the Wi-Fi and every device added to the Zap.

## 4. In the app

1. Open Sourceful Energy and sign in. No profile or site yet: create them first.
2. Tap **Onboard a new Zap** under **Get started**. Or go to **More → My Zaps → Add a new Zap**.
3. Stand close to the Zap and pick the one with the most bars.
4. Tap **Claim & Configure network**. The Zap joins the profile you have selected.
5. **WiFi Setup** opens. With the network cable in, **Ethernet detected** appears within about ten seconds: tap **Skip WiFi setup**. The app closes Bluetooth and shows **Connected via Ethernet**. Name the Zap if you like and tap **Done**.
6. Without Ethernet: pick the 2.4 GHz network, enter the password, tap **Connect**, then **Done**, as on the [Zap P1](../zap/README.md#4-in-the-app).

You can also set up Wi-Fi with the cable in, as a backup. With both up, the Zap sends its data over Wi-Fi.

## 5. Add the meter

The Zap does not read the meter until the meter is added in the app.

1. Go to **More**, open the site, then **Energy devices → Add Energy Device**.
2. Tap **Onboard New Device**, then **Energy Meters** and **P1 / HAN meter**.
3. Tap **Detect meter**. **Meter added** appears. Tap **Done**.

Meter data can take up to two minutes to appear.

## 6. Done when

- **The app** shows meter data.
- **The status light** is off: Bluetooth has closed. The light does not show whether the network works.

On a laptop on the same network, `http://zap.local/api/network` shows `"ethConnected": true` for Ethernet, and `"internetConnected": true` and `"mqttConnected": true` once the Zap reaches Sourceful. `http://zap.local/api/devices` lists the meter; its `sn` starts with `p1m-`.

## RS485

The terminal on the IN side takes one or more Modbus RTU devices, each with its own unit ID, if the app lists **Modbus RTU** for the model.

1. Wire with the power off. The pins, counted from USB-C: **A+, B−, GND**. **A+** to the device's A, **B−** to its B, **GND** to its GND.
2. In the app: **More**, the site, **Energy devices → Add Energy Device → Onboard New Device**, the type and the model. Under **Configure Connection**, pick **Modbus RTU** and enter **Baud Rate**, **Unit ID**, **Parity**, **Data Bits** and **Stop Bits** as set on the device.

> **Warning:** The order differs from the other Zaps: the [Zap P1](../zap/README.md#over-rs485) has GND, A+, B− and the [Zap HAN](../zap-han/README.md#an-rs485-device) B−, GND, A+.

An inverter on the network (Modbus TCP) is added as on the Zap P1: [Add an inverter](../zap/README.md#add-an-inverter).

## Change Wi-Fi

1. Hold the button 5–10 seconds until blue blinks fast, then let go. The Zap forgets the Wi-Fi and restarts with Bluetooth open.
2. In the app: **More → My Zaps**, tap the Zap, then **Reconfigure WiFi**.
3. Tap the Zap in the list, then **Configure network**, pick the network, enter the password and tap **Connect**.

## The light and the button

| Light | How it looks | Means |
| --- | --- | --- |
| Status | Rainbow, about 1 s | Starting |
| Status | Blue, solid | Waiting for the app (Bluetooth open) |
| Status | Off | Running, or no power. It does not show the network: check the app |
| At P1 OUT | On while data comes in | Data from the meter |

| Hold the button | While you hold | When you let go |
| --- | --- | --- |
| 2–5 s | Blinks slowly | The Zap restarts |
| 5–10 s | Blinks fast | Wi-Fi is cleared, the Zap restarts and waits for the app |
| More than 10 s | Solid | Factory reset: Wi-Fi, connection settings and every added device are deleted |

## Troubleshooting

| What you see | Probably | Do this |
| --- | --- | --- |
| The app does not find the Zap | Bluetooth closed a minute after the Zap went online | Unplug the Zap and plug it in, then scan again within a minute. |
| **Ethernet detected** does not appear | No address from the router (DHCP), or the cable is not in | Check the cable and the router port. Or set up Wi-Fi instead. |
| **The meter was not detected** | The P1 port is not enabled, or the cable is not fully in | Push the cable in at both ends. Ask the grid operator to enable the port. |
| Nothing lights at all | No power from the meter | Plug in USB-C (5 V). |
| An RS485 device gives no data | Wired by another Zap's pin order, or wrong serial settings | Wire A+, B−, GND counted from USB-C. Check baud rate, parity and unit ID against the device. |

## Sources

- The hardware vendor's documentation for this board, read 2026-11-07: the ports on both sides and their order, the RS485 terminal (A+, B−, GND from USB-C), power from a P1 version 5.0 meter or USB-C, USB-C needed when P1 OUT is used, no PoE
- `srcfl/srcful-zap-x-firmware` at `v7.0.5` (346754de): `components/board/include/boards/zap-ultra-mini.h` (RGB status light, button, P1 in and out, Modbus RTU on the terminal), `fw_controller/main/main.cpp` (rainbow at start; Bluetooth opens without saved Wi-Fi, also with Ethernet), `fw_controller/main/main_loop.cpp` (blue while Bluetooth waits; Bluetooth closes 60 s after Wi-Fi or Ethernet is up; button 2/5/10 s), `components/p1_data_reader/p1_meter.cpp` (the P1 OUT light, data copied to P1 OUT), `components/wifi/eth_manager.cpp` (DHCP, no fixed address), `fw_controller/API.md` (`ethConnected`, Wi-Fi preferred when both are up)
- `srcfl/srcful-flutter-app` at `v2.7.9`: `lib/screens/zap_wifi_setup_screen.dart` (**Ethernet detected**, **Skip WiFi setup**, **Connected via Ethernet**), `lib/l10n/app_en_US.arb`; adding the meter and devices as for the [Zap P1](../zap/README.md#sources)
- The device-support registry's `connection-types` on mainnet: the **Modbus RTU** fields
- Sourceful's test rig, 2026-11-07: a Zap Ultra Mini on firmware 7.0.5 reads a P1 meter and an SDM630 meter over RS485
- The one-pager is built from [onepagers/zap_ultra_mini.py](../onepagers/zap_ultra_mini.py) and [onepagers/zap_ethernet.py](../onepagers/zap_ethernet.py); the RJ12 jack follows Open Connector Graphics (Wikke Andeweg, CC BY 4.0)
