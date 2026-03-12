---
title: "SPICE"
date: 2020-11-12T17:39:43+01:00
images: ["inverter-current.png"]
featured_image: "inverter-current.png"
description: SPICE (Simulation Program with Integrated Circuit Emphasis) is an open source analog circuit simulator used to model transistor-level behaviour, characterise standard cells, and build the timing models that underlie STA.
faq:
  - q: What is SPICE used for in chip design?
    a: SPICE is a general-purpose open source analog electronic circuit simulator. It is used to explore transistor-level circuit behaviour, characterise standard cells, and build the timing models that underlie Static Timing Analysis.
  - q: What is ngspice?
    a: ngspice is a successor to the original SPICE simulator that is easily installable on Linux. It is the simulator used on this site to explore the Skywater 130 PDK.
  - q: Can SPICE simulate digital circuits and flip-flops?
    a: Yes, SPICE can simulate digital circuits at the transistor level. The site includes a demo of simulating a Sky130 D-type flip-flop with SPICE to show how it works.
---

SPICE is a general-purpose, open-source analog electronic circuit simulator. It stands for Simulation Program with Integrated Circuit Emphasis.
ngspice is a successor, and is easily installable on Linux. It's the simulator I've used to explore the Skywater 130 [PDK](/terminology/pdk).

Here's an [example spice simulation file](https://github.com/mattvenn/magic-inverter/blob/main/simulation.spice) that I used to [simulate the inverter I drew](/post/inverter).

And here's a nice demo of me showing how a flip-flop works by simulating a Sky130 D type flip flop with SPICE.

{{< youtube id="5PRuPVIjEcs" start=621 >}}
