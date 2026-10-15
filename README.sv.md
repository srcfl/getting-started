# Kom igång med Sourceful

Kom igång-guider för Sourceful Energys enheter. En guide per produkt, skriven för den som står på plats och ska få enheten att fungera. Varje guide har en one-pager att skriva ut, på svenska och engelska.

English: [README.md](README.md)

| Produkt | Vad den gör | Guide | One-pager |
| --- | --- | --- | --- |
| **Zap P1** | Läser mätarens RJ12 P1-port och skickar mätardata till Sourceful Energy-appen | [zap/](zap/README.sv.md) | [SV](zap/zap-one-pager-sv.pdf) · [EN](zap/zap-one-pager-en.pdf) |
| **Zap HAN** | Läser mätarens RJ45 HAN-port (M-Bus), drivs med USB-C | [zap-han/](zap-han/README.sv.md) | [SV](zap-han/zap-han-one-pager-sv.pdf) · [EN](zap-han/zap-han-one-pager-en.pdf) |
| **Blixt** | Industri-gateway som styr batterier, växelriktare, mätare och laddboxar på kommersiella och industriella anläggningar | [blixt/](blixt/README.sv.md) | [SV](blixt/blixt-one-pager-sv.pdf) · [EN](blixt/blixt-one-pager-en.pdf) |
| **Blixt X** | Sourcefuls gateway-programvara på RAK Hotspot V2 (de gamla dual-minrarna), som sätts upp i appen som en Zap | [blixt-x/](blixt-x/README.sv.md) | [SV](blixt-x/blixt-x-one-pager-sv.pdf) · [EN](blixt-x/blixt-x-one-pager-en.pdf) |

| | | | |
| --- | --- | --- | --- |
| [![Zap P1-one-pagern](zap/images/one-pager-sv.png)](zap/zap-one-pager-sv.pdf) | [![Zap HAN-one-pagern](zap-han/images/one-pager-sv.png)](zap-han/zap-han-one-pager-sv.pdf) | [![Blixt-one-pagern](blixt/images/one-pager-sv.png)](blixt/blixt-one-pager-sv.pdf) | [![Blixt X-one-pagern](blixt-x/images/one-pager-sv.png)](blixt-x/blixt-x-one-pager-sv.pdf) |

Enheterna ritade som SVG finns i [assets/devices/](assets/devices/).

Skärmdumpar från appen, skärm för skärm, för att lägga till en Zap och en växelriktare: [mobile/onboarding/](mobile/onboarding/README.md).

## Så håller vi guiderna bra

Guiderna ska vara **korrekta, konkreta och lätta att läsa**. Varje guide säger överst vad den gäller och när den senast kontrollerades mot sina källor, och listar källorna längst ner. Där källorna säger emot varandra står det under **Öppna frågor** i stället för att vi gissar. Reglerna finns i [CONTRIBUTING.md](CONTRIBUTING.md), och CI kontrollerar dem vid varje ändring.

Ingen av guiderna är genomgången på riktig hårdvara än. Varje produkt har en `CHECKLIST.md` för det, och guiderna och one-pagers säger "ej fälttestad" tills det är gjort.

Hittar du ett steg som är fel? Öppna en issue eller en pull request. Ett fel i en guide är ett fel på plats.

## Mer hjälp

- Supportartiklar: [support.sourceful.energy](https://support.sourceful.energy/sv)
- Den gamla Energy Gateway-guiden (2024) finns kvar under taggen [`egw-2024`](https://github.com/srcfl/getting-started/tree/egw-2024).
