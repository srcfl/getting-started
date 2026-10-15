# Blixt X: kom igång

> **Gäller:** Blixt X gateway-programvara 2.0.1 (versionen som körs i fält i oktober 2026), Sourceful Energy-appen 2.7.9 på mainnet
> **Senast verifierad:** 2026-10-15, mot `srcful-blixt-x-firmware` vid d501e798 (2.0.1) och `srcful-flutter-app` vid 9800165 (2.7.9)
> **För:** ägaren eller installatören som sätter upp en Blixt X

Blixt X är Sourcefuls gateway-programvara på en gateway byggd på Raspberry Pi 4. Precis som en Zap kopplar den växelriktare, batterier, mätare och laddboxar till Sourceful över internet. Appen sätter upp den med Zap-flödet, och varje skärm i det flödet säger "Zap".

Blixt X är inte samma produkt som [Blixt](../blixt/README.sv.md), industri-gatewayen för kommersiella anläggningar.

**Ska du ut på plats?** Skriv ut one-pagern: [Svenska](blixt-x-one-pager-sv.pdf) · [English](blixt-x-one-pager-en.pdf). English: [README.md](README.md).

[![Blixt X-one-pagern](images/one-pager-sv.png)](blixt-x-one-pager-sv.pdf)

## Innan du börjar

- [ ] **Nätverk:** Ethernet eller wifi, med internet.
- [ ] **Sourceful Energy-appen**, inloggad, med en profil och en anläggning.
- [ ] **Bluetooth på** i telefonen.
- [ ] **En enhetslista:** modell, IP-adress, port och unit-id för varje växelriktare, batteri och mätare.

## 1. Starta

1. Slå på strömmen.
2. Ethernet: koppla in kabeln. Wifi: ställs in i appen i steg 4.

Blixt X har inga statuslampor att läsa av. Kontrollen görs i steg 6.

## 2. Bluetooth-fönstret

Efter start syns gatewayen via Bluetooth som **blixt-&lt;serienummer&gt;** i **3 minuter**. Appen hittar den bara under det fönstret.

Har du missat det:

- Håll knappen i 3 sekunder, eller dubbelklicka. Då öppnas 3 minuter till.
- Eller bryt strömmen och starta gatewayen igen.

## 3. Koppla enheterna

- **Modbus TCP-enheter:** på samma nät som gatewayen, med fast IP-adress eller en DHCP-reservation.
- **Modbus RTU-enheter:** på gatewayens RS-485-port.

En enhet kan bara ha en Modbus-master. Stäng andra system som läser samma enhet.

## 4. I appen

Flödet är Zap-flödet. Där appen säger "Zap" menas Blixt X.

1. Öppna Sourceful Energy och logga in. Saknas profil eller anläggning: tryck **Skapa profil** eller **Skapa ny anläggning** först.
2. Tryck **Lägg till en ny Zap** under **Kom igång**. Eller gå till **Mer → Mina Zappar → Lägg till en ny Zap**.
3. Välj **blixt-…** i listan, inom 3 minuter efter att gatewayen startat. Ser du flera: välj den med flest signalstaplar.
4. Tryck **Registrera & konfigurera nätverk**. Gatewayen hamnar i den profil du har vald.
5. Under **WiFi-inställningar**: välj nät, skriv lösenordet och tryck **Anslut**. Dolt nät: **Ange manuellt**.
6. **WiFi anslutet**: namnge gatewayen om du vill, tryck **Klar**.

> **Bara Ethernet?** På 2.0.1 ser appen inte Ethernet-anslutningen. Den visar därför wifi-steget ändå och erbjuder inte **Hoppa över WiFi-konfiguration**. Fråga Sourceful innan du räknar med enbart Ethernet.

## 5. Lägg till enheterna i appen

1. Gå till **Mer**, öppna anläggningen, sedan **Energienheter → Lägg till energienhet**.
2. Med fler än en gateway: **Välj gateway**.
3. Tryck **Lägg till ny enhet**, välj typ och modell.
4. Fyll i **Värdadress**, **Port** och **Enhets-ID**, tryck **Fortsätt**.
5. Tryck **Anslut enhet**, sedan **Aktivera resurser** och **Klar**.

## 6. Klart när

Från en dator på samma nät:

- `http://blixt.local/api/network` visar `"internetConnected": true` och `"mqttConnected": true`.
- `http://blixt.local/api/devices` listar enheterna du lade till.
- Appen visar data från enheterna.

Använder en annan enhet redan namnet heter gatewayen `blixt-<suffix>.local` i stället. IP-adressen fungerar alltid.

## Felsökning

| Det du ser | Troligen | Gör så här |
| --- | --- | --- |
| Appen hittar inte gatewayen | Bluetooth-fönstret på 3 minuter har stängt | Håll knappen 3 s eller dubbelklicka, eller starta om gatewayen. Stå nära. |
| `blixt.local` svarar inte | Flera gatewayar på nätet, eller datorn sitter på ett annat nät | Leta efter `blixt-…local`, eller använd gatewayens IP-adress från routern. |
| `"mqttConnected": false` | Ingen internetåtkomst | Kontrollera nätet, kabeln eller wifin, och brandväggen. |
| En enhet svarar inte | Fel IP, port eller unit-id, Modbus TCP avstängt i enheten, eller en annan Modbus-master | Kontrollera inställningarna i enheten och i appen. Stäng den andra mastern. |

## Det här ändras i 3.0.0

Blixt X 3.0.0 finns på `main` men är inte ute i fält än. I 3.0.0 läggs enheter till med en drivrutin och version från Sourcefuls drivrutinsregister i stället för en inbyggd profil, serieenheter går via en USB-serieadapter, och gatewayen rapporterar Ethernet till appen. Guiden uppdateras när 3.0.0 släpps.

## Öppna frågor

- Vilken hårdvara och vilket hölje har Blixt X-enheterna i dag? Strömförsörjning, var knappen sitter och vilken plint RS-485-porten använder är inte dokumenterat.
- Kan en installation med bara Ethernet gå igenom onboardingen utan wifi på 2.0.1?
- När kommer 3.0.0 ut i fält? Appen 2.7.9 lägger till enheter med en profil, vilket 3.0.0 avvisar, så appen behöver uppdateras först.
- Namnet: firmware-README:n kallar gatewayen "Blixt", samma namn som den kommersiella Blixt.

## Källor

Repona är interna. Sökvägarna gäller de commits som står överst.

- `srcfl/srcful-blixt-x-firmware` vid d501e798 (2.0.1): `bluetooth/ble_service.py` och `bluetooth/gpioButton.py` (namn, 3-minutersfönster, knapp), `server/network/network_utils.py` (`blixt.local`), `server/core/api_server.py` (`/api/network`), `server/core/device_factory.py` (RS-485 som standard), `server/app/app.py` (version 2.0.1)
- `srcfl/srcful-blixt-x-firmware` på `main` (156134dd): `api.md`, `server/core/serial_ports.py`, `server/api/system.py` (det som ändras i 3.0.0)
- `srcfl/srcful-flutter-app` vid 9800165 (appen 2.7.9): `lib/screens/zap_onboard_screen.dart` (sökningen hittar `blixt-…`), `zap_wifi_setup_screen.dart` och `lib/services/zap_ble_client.dart` (Ethernet), `lib/services/zap_proxy_client.dart` (enheter läggs till med en profil), `lib/l10n/app_sv.arb`
- One-pagern byggs från [onepagers/blixt_x.py](../onepagers/blixt_x.py)
