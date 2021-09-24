---
title: "DRC"
date: 2020-11-12T17:42:51+01:00
images: ["antenna-rule.png"]
featured_image: "antenna-rule.png"
---

The Design Rule Check is part of the [PDK](/terminology/pdk). Both the [Magic](/terminology/magic) and [OpenLane](/terminology/openlane) tools make use of it.

It contains rules that check things like:

* The gate of the [MOSFET](/terminology/mosfet) are the correct dimensions,
* Wires on the metal layers are not too narrow and not too close,
* Check that MOSFET gates are protected if they have long connecting wires - this is called an [antenna rule](/terminology/antenna-report).

There are a few thousand rules in the Skywater130 PDK DRC. As the [process/node](/terminology/node) gets smaller, the number of rules increases.

You can find out more about the DRC checks performed by OpenLANE in [Mohamed Shalan's OpenLane FOSSI dialup presentation](https://www.youtube.com/watch?v=Vhyv0eq_mLU)
