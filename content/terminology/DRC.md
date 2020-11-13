---
title: "DRC"
date: 2020-11-12T17:42:51+01:00
featured_image: '/antenna-rule.png'
---

The Design Rule Check is part of the [PDK](/terminology/pdk). Both the [Magic](/terminology/magic) and [OpenLane](/terminology/openlane) tools make use of it.

It contains rules that check things like:

* The gate of the [MOSFET](/terminology/mosfet) are the correct length
* Wires on the metal layers are not too narrow and not too close
* Check that MOSFET gates are protected if they have long connecting wires.

This last rule is my favourite.

![antenna rule](/antenna-rule.png)

When the ASIC is being built up layer by layer, we have the gates of the MOSFETS built first. Then we use the metal layers to connect them into bigger blocks.
Between layers, the [wafer](/terminology/wafer) is often flattened. This process can induce enough electrical charge to destroy the connected gate.
In order to avoid this, the antenna DRC rule makes sure that a protection diode is added close to the gate. This allows build up of charge to dissipate into the wafer.

The image above is from [Mohamed Shalan's OpenLane FOSSI dialup presentation](https://www.youtube.com/watch?v=Vhyv0eq_mLU)
