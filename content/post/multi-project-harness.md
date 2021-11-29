---
title: "Multi Project Harness"
date: 2020-11-12T14:54:58+01:00
images: ["multi-project-harness.png"]
tags: ["mpw", "tools"]
featured_image: "multi-project-harness.png"
---

The Google/Skywater [Shuttle](/terminology/shuttle) has about 10 square mm of space for your project. This sounds tiny but is actually HUGE for many beginner projects.
Read [this post to find out what you could fit in](/post/how-much-can-we-fit) the user space.

For the Zero to ASIC course, I want to aggregate all your designs together into that area, so we need to do some extra bits:

* Multiplex all the inputs and outputs of your project to the GPIO pins of the [Caravel](/terminology/shuttle#caravel) harness.
* Connect important signals like clocks and make sure the tools know they are special
* there will need to be a bit of firmware on the SoC that sets up the GPIOs for each design and sets it active.

![multi project harness](/multi-project-harness.png)

I was even able to [harden](/terminology/harden) the [Verilog](/terminology/hdl) into the [GDS2](/terminology/gds2) files of 2 of my
[previously laid out modules](https://github.com/mattvenn/seven-segment-seconds).

I did this by following [this example pattern](https://github.com/efabless/openlane/tree/master/designs/manual_macro_placement_test).

![multi macro](/multi-project-gds.png)

We have 2 other people contributing designs for 5 in total. I'll be documenting this in the github repo
here [multi project harness](https://github.com/mattvenn/multi-project-harness).
