---
date: 2020-11-01
description: "Learn how to make your own inverter in Magic"
featured_image: '/inverter-speedrun.png'
tags: ["magic", "videos"]
title: "Inverter"
---

A [standard cell](/terminology/standardcell) is a building block that contains some basic digital or analogue functionality.
These blocks are then tiled together to make the final design.

Since finding out about the Skywater [PDK](/terminology/pdk), I wanted to try drawing my own 'standard cell' using the Skywater transistor
models. 

An inverter is one of the simplest and even that was quite difficult! As you can see below it contains an N and P type [MOSFET](/terminology/mosfet).

![inverter schematic](/inverter-schematic.png)

In this video I tried to build one as fast as possible, an inverter speedrun!

{{< youtube IQ_DcWT_cbc >}}

See the [repository](https://github.com/mattvenn/magic-inverter) for more information on the [Magic](/terminology/magic) commands.

After I have it in Magic, I can extract the circuit for simulation. Here I use [ngspice](/terminology/spice) to do the simulation and
as you can see we have an inverter! The red line is the input and the blue is the output.

![inverter voltage simulation](/inverter-sim.png)

A super cool thing I only realised after making my own and simulating it is that [CMOS](/terminology/cmos) only uses current to change state.
In fact that's the big reason why it was invented. The previous technology, [NMOS](/terminology/nmos) uses current whenever it's in the low output state.

This graph is a simulation of current usage as the inverter changes state:

![inverter current simulation](/inverter-current.png)
