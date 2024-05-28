---
title: "Tiny Tapeout 2 submitted for manufacture"
date: 2023-01-02T09:00:00+01:00
tags: ["ASIC", "course","Tiny Tapeout"]
images: ["tinytapeout02.png"]
featured_image: "tinytapeout02.png"
---

I'm happy to announce that [Tiny Tapeout 2](https://tinytapeout.com/runs/tt02/) was successfully submitted for manufacture in December 2022! 164 designs were included on the tapeout.

**Update!** [Tiny Tapeout 2 chips are back and working!](/post/tt02-silicon-is-alive)

If you're unfamiliar, Tiny Tapeout is an educational project that makes it easier and cheaper than ever to get your digital designs manufactured on a real chip! We had a first trial, [Tiny Tapeout ](https://tinytapeout.com/runs/tt01/) in September 2022 that was destined for MPW7. 

Tiny Tapeout 1 helped establish a baseline architecture for the design, wherein up to 500 submissions could be tiled onto a single chip and connected via a custom scanchain. Using the scanchain, each design had access to 8 inputs and ouputs, and an individual design could be accessed by selecting its address with an external DIP switch. The downside to Tiny Tapeout 1 was that it relied on the lottery system for MPW7, so there was no guarantee it would be fabricated.

For Tiny Tapeout 2, Efabless sponsored the project and we were able to guarantee silicon via the paid ChipIgnite shuttle. The architecture was modified slightly to incorporate 250 submissions with slightly larger area (150 um x 170 um), permitting about 1000 logic gates per design. More info on the specs can be found on the [Tiny Tapeout 2 Repository](https://github.com/TinyTapeout/tinytapeout-mpw7/blob/mpw7-submitted-branch/INFO.md).

Other exciting updates for Tiny Tapeout 2 include:

* [Tutorials and customizable design templates](https://tinytapeout.com/digital_design/) on the Tiny Tapeout website,
* Upgraded GitHub Actions that include [routing stats and a cell usage summary](https://github.com/ekliptik/tt02-chase-the-beat/actions/runs/3544351091),
* Interactive [3D rendering of the GDS](https://gds-viewer.tinytapeout.com/?model=https://ekliptik.github.io/tt02-chase-the-beat/tinytapeout.gds.gltf) files,
* Explore the [designs on the website](https://tinytapeout.com/runs/tt02/)
* Printable [PDF datasheet](https://tinytapeout.com/tt02.pdf).

[Sign up for the mailing list](https://tinytapeout.com/) and check out the intro video below if you'd like to learn more:

{{< youtube eMvZ5xsPXhA >}}
