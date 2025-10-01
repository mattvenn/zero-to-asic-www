---
title: "PDN"
date: 2021-02-07T18:59:34+01:00
images: ["librelane_pdn.png"]
featured_image: "librelane_pdn.png"
description: "Power Delivery Network"
---

The Power Delivery Network is what provides power for all the [macros](/terminology/macro) in your design.

For the shuttle, [LibreLane](/terminology/librelane) creates a PDN that supplies the 4 rails available to the user project area:

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

![pdn](/librelane_pdn.png)

A common failure for small designs with the [LibreLane](/terminology/librelane) tools is that there isn't enough area for the PDN to get created. A simple fix is setting the absolute size of the die to make sure its large enough.
