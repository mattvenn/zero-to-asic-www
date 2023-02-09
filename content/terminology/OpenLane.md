---
title: "OpenLane"
date: 2020-11-12T17:39:49+01:00
images: ["openlane-flow.png"]
featured_image: "openlane-flow.png"
---

OpenLane is an Open Source ASIC tool. You can download it from [here](https://github.com/efabless/openlane). The 
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

To see more about OpenLane's output files - [check this article](/post/openlane_output_files)

OpenLane is a flow controller built using OpenROAD-- the main application for RTL-GDSII flows: [This is a project funded by DARPA to develop open source ASIC tooling](https://theopenroadproject.org/).
Here is the link to [OpenROAD documentation and Tutorials](https://openroad.readthedocs.io/en/latest/).
Find useful resources here: [OpenROAD Resources](https://theopenroadproject.org/resources/).

You can watch some interviews I did with Tom Spyrou, lead dev of OpenROAD here:

{{< youtube nSNQNp6Mz8Q >}}

Tom also did a presentation for [OpenTapeOut](https://opentapeout.dev/).

{{< youtube p2HVoj6OhaI >}}

