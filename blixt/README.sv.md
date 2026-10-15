# Blixt: kom igång

> **Gäller:** Blixt-gatewayen på EDATEC ED-IPC3630 (Pi CM5), dashboard 3.x. ED-IPC1100 där det står.
> **Senast verifierad:** 2026-10-15, mot `blixt-gateway` på `main` (491197b)
> **För:** installatören som driftsätter en Blixt på en anläggning

Blixt är en industri-PC som styr batterier, hybridväxelriktare, mätare och laddboxar på kommersiella och industriella anläggningar. Den läser och styr enheterna över Modbus RTU eller TCP, håller anläggningens säkring och exportgräns, och skickar mätvärden till Sourceful. Allt ställs in i Blixts lokala dashboard.

**Ska du ut på plats?** Skriv ut one-pagern: [Svenska](blixt-one-pager-sv.pdf) · [English](blixt-one-pager-en.pdf). English: [README.md](README.md).

[![Blixt-one-pagern](images/one-pager-sv.png)](blixt-one-pager-sv.pdf)

## Det här gör Sourceful innan du åker

Du ska få en enhet som är förberedd. Fråga Sourceful om något av det här är oklart innan du åker:

- Enheten har rätt programvara och är kopplad till rätt miljö hos Sourceful.
- Enhetens identitet är registrerad hos Sourceful. Annars kommer inga mätvärden fram.
- På IPC3630: serieportarna är aktiverade för enheten.
- Du vet vilka växelriktare, batterier och mätare som ska kopplas in, och att det finns en drivrutin för varje modell.

> **Varning:** Är anläggningen med på Svenska kraftnäts stödtjänstmarknad: ändra ingenting i dashboarden, starta inte om och dra inte ur något utan att Sourceful har godkänt just det.

## Ta med

- [ ] Blixt med antenner (4G och WiFi/BT)
- [ ] Strömförsörjning 9–36 V DC (IPC3630)
- [ ] Ethernetkabel till anläggningens nät, med DHCP
- [ ] Partvinnad kabel för RS-485 om någon enhet ska kopplas seriellt
- [ ] Modell, IP-adress, port och unit-id för varje växelriktare, batteri och mätare
- [ ] Säkringsstorlek, antal faser och spänning för anläggningen
- [ ] En dator på samma nät som Blixt

## 1. Montera och anslut

1. Skruva fast antennerna: **4G** och **WiFi/BT**.
2. Anslut Ethernet till anläggningens nät. Blixt hämtar adress via DHCP. 4G är reservförbindelse.
3. Anslut strömmen. IPC3630: 2-polig plint, **stift 1 = GND**, **stift 2 = VIN+**, 9–36 V DC. Kontrollera polariteten innan du slår på.

Använd inte **PROGRAMMING**-porten. Den är bara till för att avbilda enheten.

Enheten är uppkopplad efter ungefär en minut. Första gången hämtar den sin programvara, ungefär 1,6 GB. Det tar 10–20 minuter, längre på 4G. Dra inte ur strömmen under tiden.

## 2. Koppla RS-485 (IPC3630)

> **Varning:** Använd bara **COM2** eller **COM4** för Modbus. COM1 och COM3 tappar korta Modbus-ramar.

| Port | B | A | GND | Enhet i dashboarden | Terminering |
| --- | --- | --- | --- | --- | --- |
| COM2 | stift 1 | stift 3 | stift 5 eller 6 | `/dev/ttyAMA4` | bygel J22 |
| COM4 | stift 2 | stift 4 | stift 5 eller 6 | `/dev/ttyAMA3` | bygel J24 |

1. Koppla A till A, B till B och GND till GND. Portarna är isolerade, så GND ska med.
2. Terminera bara bussens två ändar med 120 Ω. Är Blixt i ena änden: sätt bygeln för porten. Byglarna sitter öppna från fabrik.
3. En enhet kan bara ha en Modbus-master. Behöver något annat system läsa samma enhet: använd **Gateway → Modbus proxy** i dashboarden i stället för en andra master.

## 3. Öppna dashboarden

Från en dator på samma nät: `http://blixt-<serienummer>.local/`.

Använd serienumret i adressen. Bara `blixt.local` blir fel när det finns fler än en Blixt på nätet. Dashboarden svarar inte på 4G-adressen.

> **Varning:** Den som når dashboarden kan styra batteriet. Ha Blixt på ett skyddat nät, och öppna den aldrig mot internet.

## 4. Ställ in anläggningen

Gör det här **innan** något styrs.

1. Gå till **Flow → Site configuration**.
2. Ange säkringsstorlek, antal faser och spänning. Standardvärdet är 63 A, 3 faser, 230 V.
3. Välj anläggningens mätare. Den måste rapportera ström och spänning på varje fas. Gör den inte det begränsas batterierna, och en banderoll visar varför.

## 5. Lägg till enheterna

För varje växelriktare, batteri och mätare:

1. Gå till **Devices** och välj **Add device**.
2. Välj drivrutin och **version** i listan. Listan kommer från Sourcefuls drivrutinsregister. Syns inte en ny version: tryck **↻ Refresh**.
3. Lås alltid en version. En enhet utan låst version följer senaste versionen och kan ändra beteende utan att någon märker det.
4. Välj anslutning:
   - **TCP:** IP-adress, port (oftast 502) och unit-id.
   - **RTU:** serieport (`/dev/ttyAMA4` för COM2, `/dev/ttyAMA3` för COM4), hastighet, paritet och unit-id.

> **Varning:** I RTU-formuläret är `/dev/ttyAMA0` förifyllt. Det är COM3. Byt till COM2 eller COM4.

## 6. Klart när

- **Devices:** varje enhet visar `live`. `timeout`, `stale` eller `no data` betyder att den inte svarar.
- **Flow:** effekt, laddnivå (SoC) och frekvens syns inom några sekunder.
- **Batteritest:** i **Manual**-läge, kör ungefär 10 % av batteriets märkeffekt. Positiv effekt laddar, negativ laddar ur. Avvikelsen ska ligga nära 0 och **FAULT** ska vara släckt.

Kopplingen till en aggregator görs av Sourceful och inte på plats. Medan en aggregator styr är de lokala reglagen låsta.

## Felsökning

| Det du ser | Troligen | Gör så här |
| --- | --- | --- |
| En RTU-enhet visar `timeout` eller `no data` | Fel port (COM1, COM3 eller förifyllda `/dev/ttyAMA0`), A och B förväxlade, fel hastighet eller unit-id, ingen terminering | Använd COM2 eller COM4. Kontrollera A/B, inställningarna och termineringen. |
| Samma skräpdata oavsett hastighet, på IPC3630 | Serieportarna är inte aktiverade för enheten | Kontakta Sourceful. |
| Fel på serieporten efter att du bytt port och startat om styrningen | Den gamla porten hänger kvar | Kontakta Sourceful för en omstart av styrtjänsten. |
| Dashboarden öppnas inte | Fel adress, eller flera Blixt med samma namn | Använd `blixt-<serienummer>.local` från en dator på samma nät. |
| Reglagen är gråa | En aggregator styr | Det är avsiktligt. Kontakta Sourceful om du behöver styra lokalt. |
| Batteriet laddar men laddar inte ur | Växelriktarens skydd mot export (anti-backflow) är på | Kontrollera inställningen i växelriktaren. |
| Effekten stannar strax under börvärdet | Säkringsgränsen begränsar | Kontrollera **Site configuration**. |
| Enheten dyker aldrig upp hos Sourceful | Antenn saknas (IPC1100), första uppdateringen pågår, eller identiteten är inte registrerad | Kontrollera antennen, vänta 20 minuter, kontakta sedan Sourceful. |

## Öppna frågor

- Vilken hårdvara är produkten för nya installationer, IPC3630 eller IPC1100? Den här guiden beskriver IPC3630, för den är bäst dokumenterad.
- IPC1100: strömområde, RS-485-plint och terminering saknar dokumentation.
- Vem registrerar enhetens identitet, och finns det ett steg för installatören?
- Är serienumret på enheten samma som det som används i `blixt-<serienummer>.local`?
- Den befintliga snabbstarten i `blixt-gateway` säger att Blixt drivs med USB-C 5 V. Det stämmer inte med någon av modellerna.

## Källor

Repot `srcfl/blixt-gateway` är internt. Sökvägarna gäller `main` vid 491197b.

- `README.md`: vad Blixt är, provisionering, första uppstart, drivrutiner från registret
- `docs/specs/ipc-3600-specs.md`: ström, portar, COM-portar, terminering, isolering
- `docs/gateway/DASHBOARD-ACCESS.md`: adress till dashboarden och nätskydd
- `services/dashboard/README.md`: Devices-statusar, aggregatorlås, drivrutinsval och versionslåsning
- `docs/specs/site-limits.md`: säkring, faser och krav på anläggningens mätare
- `docs/gateway/Sourceful-Gateway-Battery-and-SvK-Tests.html`: batteritestet i Manual-läge
- `services/dashboard/web/src/.../DeviceForm.tsx`: förifyllda `/dev/ttyAMA0` och anslutningstyper
