---
title: "WLCSP"
date: 2020-11-13T13:03:31+01:00
description: Wafer Level Chip Scale Packaging is an extremely compact, low-cost IC package that eliminates bond wires, reducing parasitic inductance and improving high-speed performance.
images: ["wlcsp-package.png"]
featured_image: "wlcsp-package.png"
faq:
  - q: What is WLCSP packaging?
    a: WLCSP (Wafer Level Chip Scale Packaging) is a very small, cheap IC package where the chip is packaged at the wafer level, without the bond wires used in traditional packaging.
  - q: What are the advantages of WLCSP over wire-bonded packages?
    a: WLCSP eliminates bond wires, which reduces parasitic inductance that can cause problems for high-speed designs, while also being smaller and cheaper to produce.
  - q: How is WLCSP defined in the Skywater PDK?
    a: The last 5 layers of the Skywater PDK define the layers necessary to build the WLCSP package.
---

This package is very small and cheap to produce. It also has benefits due to the lack of bond wires. 
Bond wires increase parasitic inductance, and can be a problem for high speed designs.

![package](/wlcsp-package.png)

The downside is that they are very tiny!

![cross section](/wlcsp-cross-section.jpg)

The last 5 layers of the Skywater [PDK](/terminology/pdk) define the layers necessary to build the WLCSP package.
