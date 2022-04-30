---
title: "CMOS"
date: 2020-11-13T13:35:41+01:00
description: "Complementary Metal Oxide Semiconductor"
images: ["inverter-schematic-labelled.png"]
featured_image: "inverter-schematic-labelled.png"
---

CMOS was introduced to [ICs](/terminology/ic) in the late 1960s. Before then, [NMOS](/terminology/nmos) was used for digital logic. NMOS isn't very energy efficient because the pullup resistor is dissipating energy when the N type transitor is on. 

To get better energy efficiency, an extra P type transistor replaces the pullup resistor. Only one transistor is on at a time.

https://en.wikipedia.org/wiki/CMOS:

> Complementary Metal Oxide Semiconductor (CMOS) is a type of [MOSFET](/terminology/mosfet) fabrication [process](/terminology/node) that uses complementary and symmetrical pairs of p-type and n-type MOSFETs to build logic functions. 

Here is a CMOS inverter showing the complementary N and P type MOSFETs.

![cmos inverter](/inverter-schematic-labelled.png)

And here's how it could be laid out using a tool like [Magic](/terminology/magic)

![cmos inverter](/inverter-magic-labelled.png)

This video shows a sped up screen capture of me laying out a [DRC](/terminology/drc) clean inverter with Magic.

{{< youtube IQ_DcWT_cbc >}}

