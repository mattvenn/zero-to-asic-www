---
title: "OpenLANE"
date: 2020-11-12T17:39:49+01:00
featured_image: "/openlane-flow.png"
---

OpenLANE is an Open Source ASIC tool. You can download it from [here](https://github.com/efabless/openlane). The 
installation instructions are pretty straight forwards and it takes about 15 minutes and 3GB of disk space.

For a lot of great information on how it works and what it does, please watch [Mohamed Shalan's OpenLane FOSSI dialup presentation](https://www.youtube.com/watch?v=Vhyv0eq_mLU)

Here's the overview:

![Openlane flow](/openlane-flow.png)

We put our [HDL](/terminology/hdl) in at one end, and out the other comes the [GDS2](/terminology/gds2) files that are the standard file format for the [foundry](/terminology/foundry). 

The most fundamental steps are:

* [Synthesis](/terminology/synthesis)
* [Floor planning](/terminology/floorplan)
* [Place and Route](/terminology/place_and_route)
* sign off: [Layout vs Schematic](/terminology/lvs), [Design Rule Check](/terminology/drc), [Static Timing Analysis](/terminology/sta)

To see more about OpenLANE's output files - [check this article](posts/openlane_output_files)
