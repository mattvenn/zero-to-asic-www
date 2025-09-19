---
title: "DRC"
date: 2020-11-12T17:42:51+01:00
images: ["antenna-rule.png"]
featured_image: "antenna-rule.png"
---

The Design Rule Check is part of the [PDK](/terminology/pdk). Both the [Magic](/terminology/magic) and [LibreLane](/terminology/librelane) tools make use of it.

It contains rules that check things like:

* The gate of the [MOSFET](/terminology/mosfet) are the correct dimensions,
* Wires on the metal layers are not too narrow and not too close,
* Check that MOSFET gates are protected if they have long connecting wires - this is called an [antenna rule](/terminology/antenna-report).

The design rules are generally a description of the smallest items that can be reliably manufactured so that a whole chip is functional. If items are drawn thinner than these rules they may have gaps in them, or break off during production or later, or break when placed under electrical stress at some point in the product's life. These are referred to as 'opens' (meaning gaps in the wiring etc), 'yield risks' (meaning that less than 100% of devices will work) or 'reliability issues' (meaning that devices may fail once in use). If items are drawn closer together than the rules allow then they may not be formed as separate items and hence short together, or suffer from other long term reliability issues. Generally the design rules are set so that all chips of a reasonable size will function correctly, all remaining yield issues being due to contamination (dirt and dust) in the production facility.

There are a few thousand rules in the Skywater130 PDK DRC. As the [process/node](/terminology/node) gets smaller, the number of rules increases.

You can find out more about the DRC checks performed by LibreLane in [Mohamed Shalan's OpenLane FOSSI dialup presentation](https://www.youtube.com/watch?v=Vhyv0eq_mLU)
