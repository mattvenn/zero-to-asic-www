---
title: "RTL"
date: 2020-11-12T17:43:56+01:00
images: ["rtl.png"]
featured_image: "rtl.png"
description: Register Transfer Level
---
People often use the terms RTL and [HDL](/terminology/hdl) interchangably.

I see it in a bit of a different way, influenced by Mead & Conway's book "Introduction to VLSI systems". It's more of a design methodology. 

For reasons of speed and debugging, it makes sense to split up the data processing into smaller steps and buffer the results in registers (small memories usually made up of a stack of flip-flops). As the data flows between registers, it's called register transfer level.

Here's a quote from page 105 of the pdf of the book:

![rtl](/rtl.png)

For a different viewpoint, this [thread in stackexchange](https://electronics.stackexchange.com/questions/69022/rtl-vs-hdl-whats-the-difference) tries to answer the question - what is the difference between [RTL and HDL](/terminology/hdl).

I made a video about how flip-flops work, and cover a bit about the difference between combinatorial and sequential logic at the beginning.

{{< youtube 5PRuPVIjEcs >}}

Verilog and VHDL are both hardware description langauages (HDLs). They can describe all sorts of things, some of which are implementable by logic synthesis (ie synthesizable) and lots of things which are not. They can both describe netlists, ie the wiring together of pre-existing cells, and can also describe test harnesses and stimuli. The subset of these HDLs that is meant to describe real hardware behaviour (other than as netlist) is often referred to as RTL, but not all of this is synthesizable.
