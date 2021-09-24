---
title: "PDN"
date: 2021-02-07T18:59:34+01:00
images: ["openlane_pdn.png"]
featured_image: "openlane_pdn.png"
description: "Power Delivery Network"
---

The Power Delivery Network is what provides power for all the [macros](/terminology/macro) in your design.

For the shuttle, [OpenLANE](/terminology/openlane) creates a PDN that supplies the 4 rails available to the user project area:

    inout vdda1,    // User area 1 3.3V supply
    inout vdda2,    // User area 2 3.3V supply
    inout vssa1,    // User area 1 analog ground
    inout vssa2,    // User area 2 analog ground
    inout vccd1,    // User area 1 1.8V supply
    inout vccd2,    // User area 2 1.8v supply
    inout vssd1,    // User area 1 digital ground
    inout vssd2,    // User area 2 digital ground

Metal 4 is used for vertical lines that are cut for the macros, and Metal 5 routes over the top of everything.
When the metal 5 lines pass over the macro, vias are dropped to connect the macro's internal PDN to the user project area's PDN.

![pdn](/openlane_pdn.png)
