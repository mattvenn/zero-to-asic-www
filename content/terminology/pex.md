---
title: "PEX"
date: 2021-01-07T11:41:15+01:00
images: ["inverter-sim.png"]
featured_image: "inverter-sim.png"
---

PEX stands for Parastic Extraction.
When we build a circuit on a chip we have an intention in mind, for example an ideal inverter inverts the incoming signal immediately and with no delay.

The reality is that we have various 'parasitics' for example unwanted capacitance in the [MOSFET's](/terminology/mosfet) gates, or unwanted resistance in the connections
between the MOSFETs. These parasitics slow the inverter down. We can extract the parasitics so we can model them and take them into account when building larger circuits.

At [22:35](https://youtu.be/QyXcVrPGomw?t=1355) of my #remoticon talk you can hear me explain about parasitic extraction and show a demo with [magic](/terminology/magic).

{{< youtube QyXcVrPGomw >}}
