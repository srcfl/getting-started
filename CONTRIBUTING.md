# How we write the guides

A getting-started guide has to work on site, with a phone in one hand and a cable in the other. Three requirements, in this order:

1. **Correct.** Everything in a guide has a source. What we cannot back up does not go in the steps.
2. **Concrete.** Exact button names, exact lights, exact ports. Never "configure the device".
3. **Easy to read.** Short sentences. One action per step. The most important thing first.

## Two languages, one set of facts

Every product has:

- `README.md`, the guide in English, and `README.sv.md`, the same guide in Swedish
- `<product>-one-pager-en.pdf` and `<product>-one-pager-sv.pdf`, built from `onepagers/<product>.py`

The four must say the same thing. Change a step in one, change it in all four in the same pull request.

In the Swedish version, write the app's labels as the app shows them in Swedish (`lib/l10n/app_sv.arb` in `srcful-flutter-app`), not the English ones.

## Every guide starts the same way

At the top of `README.md`:

```markdown
> **Applies to:** Zap with current firmware (2.3.x), the Sourceful Energy app 2.7.9 on mainnet
> **Last verified:** 2026-10-15, against the sources at the bottom
> **For:** the installer on site
```

At the top of `README.sv.md`, the same with **Gäller**, **Senast verifierad** and **För**.

The guide always ends with `## Sources` (`## Källor` in Swedish), listing the support articles, repositories, commits and files the steps are built on. CI rejects a guide that lacks any of this.

## The steps

- One action per step, in the imperative: "Push the cable into P1 IN", not "The cable should be pushed".
- Text from the app or the device is written exactly as it appears there, in bold: **Onboard a new Zap**, **P1 IN**.
- Say what you see when the step worked: "Green light, solid".
- Warnings go with the step where the mistake happens, not in a list at the end.
- Troubleshooting is written as symptom, cause, fix. The symptom is what you see, not an error code you have to look up.
- No "simply", "just" or "obviously". What is simple to us is not simple on site.

## Correctness

- Write from the source, not from memory. The code at the version the field runs, the app at the version in the stores, the support articles and the product images are sources. An old guide, a chat thread or "that's how it usually works" is not.
- When sources disagree, the app and the firmware win over the support articles, because they are what the person on site sees. List the disagreement under `## Open questions` so the other source gets fixed.
- When something cannot be verified, it goes under `## Open questions`, not into the steps.
- When the app, the firmware or the hardware changes, update the guide in the same go and set a new **Last verified** date.
- Drivers come only from Sourceful's device-support registry. Point there, never to a copy in a repository.

## What does not belong here

This repository is public. CI rejects a change that contains:

- internal IP addresses, host names and fleet names
- device UUIDs, keys, tokens and passwords
- SSH logins

Also keep out customer names, site names and partner names. Internal operations (deploys, pinning, SSH, reserve-market tests) belong in each product's own repository.

## Images

- Product images go in `<product>/images/`. Use Sourceful's own images where they exist, for example from `srcful-marketing-website` or the app.
- Give every image alt text that says what it shows.
- Keep images under about 400 kB.
- A drawing that is not to scale or not the real front panel says so on the page.

## The one-pagers

```sh
pip install weasyprint==70.0
python3 onepagers/build.py --thumbs
```

- One A4 page each. The build fails if a one-pager spills onto a second page, or if the content runs into the block at the bottom.
- Layout and drawing helpers are shared in `onepagers/common.py` and `onepagers/base.css`. The text for both languages sits in the `T` dictionary of each product module.
- `--thumbs` refreshes the preview images in `<product>/images/` (needs `pdftoppm`).
- Every build also writes the device drawings to `assets/devices/`. Draw a device from the vendor's or Sourceful's own images, at the right proportions, with Sourceful's label instead of the vendor's. Where no image exists, ask someone who has the device, or draw a schematic and say so on the page.

## Making a change

1. Make the change on a branch and open a pull request.
2. CI runs `scripts/check_guides.py` and builds every one-pager. Both must pass.
3. Someone who knows the product reads the steps against the sources before the pull request is merged.
