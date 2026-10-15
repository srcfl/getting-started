# Getting started with Sourceful

Getting-started guides for Sourceful Energy's devices. One guide per product, written for the person on site who has to make it work. Every guide comes with a printable one-pager in English and Swedish.

Svenska: [README.sv.md](README.sv.md)

| Product | What it does | Guide | One-pager |
| --- | --- | --- | --- |
| **Zap** | Reads the electricity meter's P1/HAN port and sends meter data to the Sourceful Energy app | [zap/](zap/README.md) | [EN](zap/zap-one-pager-en.pdf) · [SV](zap/zap-one-pager-sv.pdf) |
| **Blixt** | Industrial gateway that controls batteries, inverters, meters and EV chargers on commercial and industrial sites | [blixt/](blixt/README.md) | [EN](blixt/blixt-one-pager-en.pdf) · [SV](blixt/blixt-one-pager-sv.pdf) |
| **Blixt X** | Sourceful's gateway software on a Raspberry Pi 4–based gateway, set up in the app like a Zap | [blixt-x/](blixt-x/README.md) | [EN](blixt-x/blixt-x-one-pager-en.pdf) · [SV](blixt-x/blixt-x-one-pager-sv.pdf) |

| | | |
| --- | --- | --- |
| [![Zap one-pager](zap/images/one-pager-en.png)](zap/zap-one-pager-en.pdf) | [![Blixt one-pager](blixt/images/one-pager-en.png)](blixt/blixt-one-pager-en.pdf) | [![Blixt X one-pager](blixt-x/images/one-pager-en.png)](blixt-x/blixt-x-one-pager-en.pdf) |

## How we keep the guides good

The guides must be **correct, concrete and easy to read**. Each guide says at the top what it applies to and when it was last checked against its sources, and lists the sources at the bottom. Where sources disagree, the guide says so under **Open questions** instead of guessing. The rules are in [CONTRIBUTING.md](CONTRIBUTING.md), and CI checks them on every change.

Found a step that is wrong? Open an issue or a pull request. A mistake in a guide is a mistake on site.

## Repository layout

```
<product>/README.md                  the guide in English
<product>/README.sv.md               the guide in Swedish
<product>/<product>-one-pager-en.pdf the one-pager in English
<product>/<product>-one-pager-sv.pdf the one-pager in Swedish
<product>/images/                    product images and one-pager previews
onepagers/                           the source of every one-pager
assets/                              fonts and the Sourceful logo
scripts/check_guides.py              the checks CI runs
```

Build the one-pagers:

```sh
pip install weasyprint==70.0
python3 onepagers/build.py --thumbs
```

## More help

- Support articles: [support.sourceful.energy](https://support.sourceful.energy/en)
- The old Energy Gateway guide (2024) is kept under the tag [`egw-2024`](https://github.com/srcfl/getting-started/tree/egw-2024).
