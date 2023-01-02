---
title: "Tiny Tapeout"
date: 2023-01-02T09:00:00+01:00
tags: ["ASIC", "course","Tiny tapeout"]
images: ["tinytapeout02.png"]
featured_image: "tinytapeout02.png"
---

I'm excited to announce that TinyTapeout02 was successfully submitted in December 2022! In all 164 designs were included on the tapeout.

If you're unfamiliar, TinyTapeout is an educational project that makes it easier and cheaper than ever to get your digital designs manufactured on a real chip! We had a first trial, [TinyTapeout01](https://tinytapeout.com/runs/tt01/) in September 2022 that was destined for MPW7. 

TinyTapeout01 helped establish a baseline architecture for the design, wherein up to 500 submissions could be tiled onto a single chip and connected via a custom scanchain. Using the scanchain, each design had access to 8 inputs and ouputs, and an individual design could be accessed by selecting its address with an external DIP switch. The downside to TinyTapeout01 was that it relied on the lottery system for MPW7, so there was no guarantee it would be fabricated.

For TinyTapeout02, we were fortunate to have guaranteed silicon via ChipIgnite. The architecture was modified slightly to incorporate 250 submissions with slightly larger area (150 um x 170 um), permitting about 1000 logic gates per design. More info on the specs can be found on the [TinyTapeout02 Repo](https://github.com/TinyTapeout/tinytapeout-mpw7/blob/mpw7-submitted-branch/INFO.md).

Other exciting updates for TinyTapeout02 include:

1. [Tutorials and customizable design templates](https://tinytapeout.com/digital_design/) on the TinyTapeout website,
2. Upgraded GitHub Actions that include routing stats and a cell usage summary,
3. Interactive 3D rendering of the [GDS](/terminology/gds2/) files, and
4. [PDF datasheet](https://tinytapeout.com/tt02.pdf) of all the designs.

[Sign up for the mailing list](https://tinytapeout.com/) and check out the intro video below if you'd like to learn more:

{{< youtube eMvZ5xsPXhA >}}
