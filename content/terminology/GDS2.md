---
title: "GDS2"
date: 2020-11-12T17:42:46+01:00
featured_image: '/hackaday-gds.png'
---

GDSII/GDS2 is a binary file format that represents the layers needed to produce an [ASIC](/terminology/asic).

In the [OpenLane](/terminology/openlane) flow, [Magic](/terminology/magic) is used to 'stream' the final GDS2 files.

We can use other programs or even software libraries to generate valid GDS2 files. Here I've used [gdspy](https://gdspy.readthedocs.io/en/stable/) to convert
the Hackaday logo into GDS2.

![hackaday logo](/hackaday-gds.png)

You can check the very simple program out [here](https://github.com/mattvenn/logo-to-gds2)

The Skywater [PDK](/terminology/pdk) defines all the layers that we can use in the GDS2 files.
