---
title: "PDN"
date: 2021-02-07T18:59:34+01:00
images: ["librelane_pdn.png"]
featured_image: "librelane_pdn.png"
description: The Power Delivery Network (PDN) is the grid of metal rails and vias that distributes power and ground to every cell in an ASIC design, built automatically by LibreLane during the flow.
faq:
  - q: What is a Power Delivery Network (PDN) in an ASIC?
    a: The PDN is what provides power for all the macros in your design. It is a structured network of metal rails that carries supply voltages and ground to every cell across the chip.
  - q: How does LibreLane build the PDN for a Tiny Tapeout shuttle submission?
    a: LibreLane creates a PDN that supplies the 4 rails available to the user project area — two 3.3V analog supplies, two analog grounds, two 1.8V digital supplies, and two digital grounds. Metal 4 is used for vertical lines and Metal 5 routes over everything, dropping vias to connect macros.
  - q: What is a common PDN failure with LibreLane for small designs?
    a: A common failure for small designs is that the die area is not large enough for the PDN to be created. A simple fix is setting the absolute die size to ensure it is big enough.
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
