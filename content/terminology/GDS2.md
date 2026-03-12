---
title: "GDSII"
date: 2020-11-12T17:42:46+01:00
images: ["hackaday-gds.png"]
featured_image: "hackaday-gds.png"
aliases:
    - gds
description: GDSII (GDS2) is the binary file format used to describe the physical layout of an ASIC, with each layer of shapes corresponding to a photolithographic mask used during chip fabrication.
faq:
  - q: What is a GDSII file used for in chip design?
    a: A GDSII file is a binary format that represents all the shapes on all the layers needed to produce an ASIC. It is the final output of the chip design flow and is sent to the foundry for fabrication.
  - q: How do GDSII layers relate to physical masks?
    a: Each shape in a GDSII file is assigned to a layer, and each layer is used to create a photolithographic mask. Often one or more GDSII layers are combined, grown, or shrunk to produce a single mask, so the mask may differ from what the designer originally drew.
  - q: What tool produces the GDSII file in the LibreLane flow?
    a: In the LibreLane flow, Magic is used to stream the final GDSII files. The Skywater PDK defines all the layers that can be used in those files.
---

GDSII/GDS2 is a binary file format that represents the layers needed to produce an [ASIC](/terminology/asic).

In the [LibreLane](/terminology/librelane) flow, [Magic](/terminology/magic) is used to 'stream' the final GDSII files.

All shapes are assigned to a given GDSII layer, and each layer ends up being used to create a [mask](/terminology/maskset), although often this may involve the combination of one or more GDSII layers to form one mask, and the shapes are often grown, or shrunk, or merged and thus what ends up on the mask may not be the same as what was drawn by the designer. Each mask is then used in a photolithographic step to produce the chip.

We can use other programs or even software libraries to generate valid GDSII files. Here I've used [gdspy](https://gdspy.readthedocs.io/en/stable/) to convert
the Hackaday logo into GDSII.

![hackaday logo](/hackaday-gds.png)

You can check the very simple program out [here](https://github.com/mattvenn/logo-to-gds2)

The Skywater [PDK](/terminology/pdk) defines all the layers that we can use in the GDSII files.
