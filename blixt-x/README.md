# Blixt X: getting started

> **Applies to:** Blixt X gateway software 2.0.1 (the release running in the field, October 2026), the Sourceful Energy app 2.7.9 on mainnet
> **Last verified:** 2026-10-15, against `srcful-blixt-x-firmware` at d501e798 (2.0.1) and `srcful-flutter-app` at 9800165 (2.7.9)
> **For:** the owner or installer setting up a Blixt X

Blixt X is Sourceful's gateway software on a Raspberry Pi 4–based gateway. Like a Zap, it connects inverters, batteries, meters and EV chargers to Sourceful over the internet. The app sets it up with the Zap flow, and every screen in that flow says "Zap".

Blixt X is not the same product as [Blixt](../blixt/README.md), the industrial gateway for commercial sites.

**Going on site?** Print the one-pager: [English](blixt-x-one-pager-en.pdf) · [Svenska](blixt-x-one-pager-sv.pdf). Svenska: [README.sv.md](README.sv.md).

[![The Blixt X one-pager](images/one-pager-en.png)](blixt-x-one-pager-en.pdf)

## Before you start

- [ ] **Network:** Ethernet or Wi-Fi, with internet access.
- [ ] **The Sourceful Energy app**, signed in, with a profile and a site.
- [ ] **Bluetooth on** on the phone.
- [ ] **A device list:** model, IP address, port and unit ID for every inverter, battery and meter.

## 1. Start

1. Power the gateway on.
2. On Ethernet: plug in the cable. On Wi-Fi: you set it in the app in step 4.

Blixt X has no status lights to read. You check it in step 6.

## 2. The Bluetooth window

After it starts, the gateway shows up over Bluetooth as **blixt-&lt;serial&gt;** for **3 minutes**. The app only finds it during that window.

Missed it:

- Hold the button for 3 seconds, or double-click it. That opens 3 more minutes.
- Or cut the power and start the gateway again.

## 3. Connect the devices

- **Modbus TCP devices:** on the same network as the gateway, with a fixed IP address or a DHCP reservation.
- **Modbus RTU devices:** on the gateway's RS-485 port.

A device can have only one Modbus master. Stop other systems that read the same device.

## 4. In the app

The flow is the Zap flow. Where the app says "Zap", it means the Blixt X.

1. Open Sourceful Energy and sign in. No profile or site yet: tap **Create new profile** or **Create new site** first.
2. Tap **Onboard a new Zap** under **Get started**. Or go to **More → My Zaps → Add a new Zap**.
3. Pick **blixt-…** in the list, within 3 minutes of the gateway starting. If you see several, pick the one with the most signal bars.
4. Tap **Claim & Configure network**. The gateway joins the profile you have selected.
5. Under **WiFi Setup**, pick the network, enter the password and tap **Connect**. Hidden network: **Enter manually**.
6. **WiFi Connected**: name the gateway if you like, then tap **Done**.

> **Ethernet only?** On 2.0.1 the app does not see the Ethernet connection, so it shows the Wi-Fi step anyway and does not offer **Skip WiFi setup**. Ask Sourceful before you rely on Ethernet alone.

## 5. Add the devices in the app

1. Go to **More**, open the site, then **Energy devices → Add Energy Device**.
2. With more than one gateway: **Select Gateway**.
3. Tap **Onboard New Device**, then the type and the model.
4. Enter **Host Address**, **Port** and **Unit ID**, then **Continue**.
5. Tap **Connect Device**, then **Enable Resources** and **Done**.

## 6. Done when

From a laptop on the same network:

- `http://blixt.local/api/network` shows `"internetConnected": true` and `"mqttConnected": true`.
- `http://blixt.local/api/devices` lists the devices you added.
- The app shows data from the devices.

If another device already uses the name, the gateway calls itself `blixt-<suffix>.local` instead. You can always use its IP address.

## Troubleshooting

| What you see | Probably | Do this |
| --- | --- | --- |
| The app does not find the gateway | The 3-minute Bluetooth window has closed | Hold the button 3 s or double-click it, or restart the gateway. Stand close. |
| `blixt.local` does not answer | Several gateways on the network, or the laptop is on another network | Look for `blixt-…local`, or use the gateway's IP address from the router. |
| `"mqttConnected": false` | No internet access | Check the network, the cable or Wi-Fi, and the firewall. |
| A device does not answer | Wrong IP, port or unit ID, Modbus TCP off in the device, or another Modbus master | Check the settings in the device and in the app. Stop the other master. |

## What changes in 3.0.0

Blixt X 3.0.0 is on `main` but not in the field yet. In 3.0.0, devices are added with a driver and version from Sourceful's driver registry instead of a built-in profile, serial devices go through a USB serial adapter, and the gateway reports Ethernet to the app. This guide is updated when 3.0.0 ships.

## Open questions

- Which hardware and enclosure are Blixt X units today? Power supply, where the button is, and which terminal the RS-485 port uses are not documented.
- On 2.0.1, can an Ethernet-only installation finish onboarding without Wi-Fi?
- When does 3.0.0 reach the field? The app 2.7.9 adds devices with a profile, which 3.0.0 refuses, so the app needs an update first.
- The name: the firmware README calls the gateway "Blixt", the same name as the commercial Blixt.

## Sources

The repositories are internal. Paths refer to the commits named at the top.

- `srcfl/srcful-blixt-x-firmware` at d501e798 (2.0.1): `bluetooth/ble_service.py` and `bluetooth/gpioButton.py` (name, 3-minute window, button), `server/network/network_utils.py` (`blixt.local`), `server/core/api_server.py` (`/api/network`), `server/core/device_factory.py` (RS-485 default), `server/app/app.py` (version 2.0.1)
- `srcfl/srcful-blixt-x-firmware` on `main` (156134dd): `api.md`, `server/core/serial_ports.py`, `server/api/system.py` (what changes in 3.0.0)
- `srcfl/srcful-flutter-app` at 9800165 (app 2.7.9): `lib/screens/zap_onboard_screen.dart` (the scan finds `blixt-…`), `zap_wifi_setup_screen.dart` and `lib/services/zap_ble_client.dart` (Ethernet detection), `lib/services/zap_proxy_client.dart` (devices added with a profile)
- The one-pager is built from [onepagers/blixt_x.py](../onepagers/blixt_x.py)
