---
title: "NMOS"
date: 2020-11-13T13:12:26+01:00
description: "N-type Metal Oxide Semiconductor"
images: ["nmos.png"]
featured_image: "nmos.png"
---

NMOS logic refers to building the [standard cells](/terminology/standardcell) we need for our [IC](/terminology/ic) out of only N-type [MOSFETs](/terminology/mosfet). This is a form of resistor-transistor logic, where the pulldown path uses an N type transistor, and the pullup path uses a resistor.

Here is how we can build an inverter from only N-type MOSFETS.

| Input       | Output      |
| ----------- | ----------- |
| 0           | 1           |
| 1           | 0           |

If the input is low, the gate is not charged and current doesn't flow through the MOSFET. The resistor pulls up the output to make it high.

If the input is high, the gate is charged and the MOSFET conducts. This pulls the output low.

![nmos](/nmos.png)

NMOS logic has the advantage that we don't need to manufacture P type transistors and so the processing is cheaper and quicker to perform.

The disadvantage with NMOS logic is that the pullup resistors waste a tiny bit of current when the transistor is on. If you have millions of these then you are wasting electricity as heat and your chips get hot and slow down. [CMOS](/terminology/cmos) was invented to solve this shortcoming. Another disadvantage is that the pulldown and pullup strengths are not well matched, leading to asymmetric waveforms. If we make the resistor smaller, so it pulls up more quickly, this wastes even more power.

To explore how this works for yourself, try my online [SiliWiz tool](https://app.siliwiz.com/?preset=nmos) - there's a [lesson about NMOS here](https://tinytapeout.com/siliwiz/nmos/).

![siliwiz](/siliwiznmos.png)

