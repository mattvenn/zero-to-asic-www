---
title: "Multi Project Harness"
date: 2020-11-12T14:54:58+01:00
featured_image: '/ciic_harness.png'
---

I've been working on the [multi project harness](https://github.com/mattvenn/multi-project-harness).
Normally in a [multi project wafer](https://en.wikipedia.org/wiki/Multi-project_wafer_service) you would have the entire space for your own design.

The Google/Skywater Shuttle is a bit different. First of all, there is the [Caravel harness](https://github.com/efabless/caravel2), which even has its own [datasheet](https://raw.githubusercontent.com/efabless/caravel/release/doc/caravel_datasheet.pdf)

![Caravel harness](/ciic_harness.png)

For this course, I want to put all your designs together into that area, so we need to do some extra bits:

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
