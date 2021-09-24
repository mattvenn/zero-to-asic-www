---
title: "NMOS"
date: 2020-11-13T13:12:26+01:00
description: "N-type Metal Oxide Semiconductor"
images: ["nmos.png"]
featured_image: "nmos.png"
---

NMOS refers to building the [standard cells](/terminology/standardcell) we need for building our [IC](/terminology/ic) out of only N-type [MOSFETs](/terminology/mosfet)

Heres how we can build an inverter from only N-type MOSFETS.

| Input       | Output      |
| ----------- | ----------- |
| 0           | 1           |
| 1           | 0           |

If the input is low, the gate is not charged and current doesn't flow through the MOSFET. The resistor pulls up the output to make it high.

If the input is high, the gate is charged and the MOSFET conducts. This pulls the output low.

![nmos](/nmos.png)

The disadvantage with NMOS is that the pullup resistors waste a tiny bit of current. If you have millions of these then you are wasting electricity as heat and your chips get hot and slow down. [CMOS](/terminology/cmos) was invented to solve this shortcoming.
