---
title: "LibreLane"
date: 2020-11-12T17:39:49+01:00
description: "LibreLane (formerly OpenLane) is an open source automated ASIC flow that takes RTL Verilog and produces GDS2 layout files ready for chip fabrication, using tools like Yosys, OpenROAD, and Magic."
images: ["librelane-flow.png"]
featured_image: "librelane-flow.png"
aliases:
    - /terminology/openlane
faq:
  - q: What is LibreLane?
    a: LibreLane is an open source automated ASIC toolchain that takes RTL (Verilog) as input and produces GDS2 layout files ready for chip fabrication. It orchestrates tools including Yosys for synthesis, OpenROAD for place and route, and Magic for DRC and layout.
  - q: What is the difference between LibreLane and OpenLane?
    a: LibreLane is the new name for OpenLane. After Efabless shut down in 2025, the project was transferred to the FOSSi Foundation and renamed LibreLane. It is the same open source ASIC flow, now maintained by the broader open source silicon community.
  - q: What are the main steps in the LibreLane flow?
    a: The LibreLane flow covers synthesis (Yosys), floorplanning, placement, clock tree synthesis, routing (OpenROAD), and sign-off checks including LVS, DRC, and static timing analysis. The output is a GDS2 file ready to submit to a foundry.
video_id: nSNQNp6Mz8Q
---

LibreLane is an Open Source ASIC tool. You can download it from [here](https://github.com/librelane/librelane). 

LibreLane is the new name for OpenLane. After [Efabless shutdown](https://www.linkedin.com/posts/tinytapeout_were-very-sad-to-hear-that-efabless-corporation-activity-7301638170297720832-n7Ru/) the project was transferred to the [FOSSi Foundation](https://fossi-foundation.org/).

OpenLane was released in 2021 and you can watch [Mohamed Shalan's OpenLane FOSSI dialup presentation](https://www.youtube.com/watch?v=Vhyv0eq_mLU) to find out more about it.

Here's the overview:

![LibreLane flow](/librelane-flow.png)

We put our [HDL](/terminology/hdl) in at one end, and out the other comes the [GDS2](/terminology/gds2) files that are the standard file format for the [foundry](/terminology/foundry). 

The most fundamental steps are:

* [Synthesis](/terminology/synthesis)
* [Floor planning](/terminology/floorplan)
* [Place and Route](/terminology/place_and_route)
* sign off: [Layout vs Schematic](/terminology/lvs), [Design Rule Check](/terminology/drc), [Static Timing Analysis](/terminology/sta)

To see more about LibreLane's output files - [check this article](/post/librelane_output_files)

## OpenROAD

LibreLane is an open source ASIC flow built using OpenROAD. [OpenROAD is a project funded by DARPA to develop open source ASIC tooling](https://theopenroadproject.org/).

Here is the [OpenROAD documentation and Tutorials](https://openroad.readthedocs.io/en/latest/) and some 
[useful resources](https://theopenroadproject.org/resources/).

You can watch some interviews I did with Tom Spyrou, lead dev of OpenROAD here:

{{< youtube nSNQNp6Mz8Q >}}

Tom also did a presentation for [OpenTapeOut](https://opentapeout.dev/).

{{< youtube p2HVoj6OhaI >}}

