---
title: "Multi Project Harness"
date: 2020-11-12T14:54:58+01:00
featured_image: '/ciic_harness.png'
---

I've been working on the Zero to ASIC [multi project harness](https://github.com/mattvenn/multi-project-harness).

The Google/Skywater [Shuttle](/terminology/shuttle) has about 10 square mm of space for your project. This sounds tiny but is actually HUGE for many beginner projects.
Read [this post to find out what you could fit in](/post/how-much-can-we-fit) the user space.

For the Zero to ASIC course, I want to aggregate all your designs together into that area, so we need to do some extra bits:

* hold all the designs except 1 in reset
* connect all the inputs and outputs
* make sure the inputs and outputs don't clash with each other
* connect important signals like clocks and make sure the tools know they are special

Then there will need to be a bit of firmware on the SoC that sets up the GPIOs for each design.

You can see my progress here [multi project harness](https://github.com/mattvenn/multi-project-harness).

![multi project harness](/multi-project-harness.png)

I was even able to [harden](/terminology/harden) (turn the Verilog into the GDS files for the factory) the 2 top level module to include 
2 [previously laid out modules](https://github.com/mattvenn/seven-segment-seconds).

I did this by following [this example pattern](https://github.com/efabless/openlane/tree/master/designs/manual_macro_placement_test)

![multi macro](/multi-project-gds.png)
