---
title: "Padring"
date: 2020-11-13T16:09:29+01:00
images: ["raven.png"]
featured_image: "raven.png"
description: The padring is the ring of large bond pads around the edge of an IC die that includes ESD protection, I/O drivers, and power/ground connections for packaging.
faq:
  - q: What is a padring on a chip?
    a: A padring is the structure around the outside edge of an IC die that contains large bond pads, ESD protection diodes, and input/output drivers used to connect the die to its package.
  - q: How does a padring connect a chip to its package?
    a: Tiny wires are bonded between the leads of the leadframe and the bond pads in the padring, electrically connecting the die to the outside world.
  - q: What padring was used in the Google shuttle?
    a: The Google shuttle used the Caravel harness, which includes a padring provided as part of the Caravel design from Efabless.
  - q: What padring is used in the Tiny Tapeout shuttles?
    a: For SKY130, the OpenFrame padring is used. For IHP and GF180 custom padframes are used.
---

We need to make sure we can package the [IC](/terminology/ic) after the [wafer](/terminology/wafer) has been diced into individual [dies](/terminology/die).

A common way of packaging ICs is to connect them to a [leadframe](/terminology/die#leadframe) by bonding tiny wires between the leads of the leadframe and the pads on the die.

The big bond pads around the outside of the IC often include [ESD protection diodes](https://en.wikipedia.org/wiki/Electrostatic_discharge), Input/Output drivers and so on.

This picture shows _raven_, an IC from Efabless. You can see around the edge there are the big bond pads and the power and ground lines. This structure is called a padring.

![raven](/raven.png)

The padring used in the [Google shuttle is included in Caravel](/terminology/shuttle#caravel).
