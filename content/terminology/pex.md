---
title: "PEX"
date: 2021-01-07T11:41:15+01:00
images: ["inverter-sim.png"]
featured_image: "inverter-sim.png"
---

PEX stands for Parastic Extraction (often called just 'extraction').
When we build a circuit on a chip we have an intention in mind, for example an ideal inverter inverts the incoming signal immediately and with no delay.

In reality the inverter will have capacitance on both the input (due to the gate) and the output (due to the diode in the drain) and the wiring of the circuit will have both (parallel) capacitance and (series) resistance. Typically, the modelling of the devices or standard cells takes into account the elements due to the transistors, but knows nothing about the wiring we add later. 

These extra unwanted circuit elements are referred to as 'parasitics', and they slow signals down and increase power dissipation. By extracting the parasitics, we can annotate them into the ideal circuit to get a model of the real circuit, and we can then analyse its performance using simulation or [STA](/terminology/sta).

At [22:35](https://youtu.be/QyXcVrPGomw?t=1355) of my #remoticon talk you can hear me explain about parasitic extraction and show a demo with [magic](/terminology/magic).

{{< youtube QyXcVrPGomw >}}
