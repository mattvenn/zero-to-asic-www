---
title: "CMOS"
date: 2020-11-13T13:35:41+01:00
description: "CMOS (Complementary Metal Oxide Semiconductor) uses paired NMOS and PMOS transistors to build energy-efficient logic gates. It is the dominant transistor technology used in modern chip fabrication."
images: ["inverter-schematic-labelled.png"]
featured_image: "inverter-schematic-labelled.png"
faq:
  - q: What is CMOS?
    a: CMOS (Complementary Metal Oxide Semiconductor) is a transistor fabrication technology that uses complementary pairs of PMOS and NMOS transistors to implement logic functions. PMOS transistors pull outputs high and NMOS transistors pull outputs low. CMOS has been the dominant technology for digital ICs since the 1980s.
  - q: Why is CMOS more energy efficient than NMOS logic?
    a: In CMOS, when inputs are stable only one transistor in each pull-up/pull-down pair is conducting at a time, so there is no static current path from supply to ground. NMOS logic uses a resistor for pull-up, which continuously dissipates power. This makes CMOS far more energy efficient, especially at scale.
  - q: What is crowbar current in CMOS?
    a: Crowbar current is a brief pulse of current that flows directly from the supply through the PMOS transistor to ground through the NMOS transistor during input switching, when both transistors are momentarily on at the same time. CMOS cells are designed to minimise this overlap to reduce switching power consumption.
---

CMOS was introduced to [ICs](/terminology/ic) in the late 1960s. P type MOSFETs are used to pull output signals up, and N type MOSFETs are used to pull output signals down - P and N are the complementary types.

Before CMOS, [NMOS](/terminology/nmos) was used for digital logic. NMOS isn't very energy efficient because the pullup is performed by a resistor which is dissipates energy when the N type transistor is pulling down. It also is hard to balance the pullup and pulldown speeds which makes design difficult. 

By using transistors for both pullup and pulldown we get better energy efficiency. When the inputs are stable, only one transistor is on at a time so there is no static current consumption, but during input switching a small amount of current may flow directly through the P then through the N transistor: this is called crowbar current. Normally the transistors are designed to avoid or minimise this unncessary power consumption.

https://en.wikipedia.org/wiki/CMOS:

> Complementary Metal Oxide Semiconductor (CMOS) is a type of [MOSFET](/terminology/mosfet) fabrication [process](/terminology/node) that uses complementary pairs of p-type and n-type MOSFETs to build logic functions. 

Here is a CMOS inverter showing the complementary N and P type MOSFETs.

![cmos inverter](/inverter-schematic-labelled.png)

And here's how it could be laid out using a tool like [Magic](/terminology/magic)

![cmos inverter](/inverter-magic-labelled.png)

This video shows a sped up screen capture of me laying out a [DRC](/terminology/drc) clean inverter with Magic.

{{< youtube IQ_DcWT_cbc >}}

