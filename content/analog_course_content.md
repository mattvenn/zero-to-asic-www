---
title: "Full Analog Course Content"
description: "What will I learn on the Analog Course?"
date: 2021-07-14T15:41:50+02:00
featured_image: 'analog_background.png'
image_pos: 0% 50%
tags: ["analog", "course"]
type: page
---

# Part 1: Schematic Capture with Xschem

While it’s possible to just draw transistors directly - for example in [SiliWiz](https://app.siliwiz.com/), this doesn’t scale well and gets confusing fast. We want to draw a circuit diagram first, with levels of hierarchy for more complex designs. These can then be simulated and checked that specifications are met before moving onto layout.


## Lab 1.1: Try the Xschem demos

* Build [Xschem](https://xschem.sourceforge.io/stefan/index.html) familiarity.
* Experiment with some of the demos that come with the [PDK](/terminology/pdk).

## Lab 1.2: Draw your own circuit

* Draw your own circuit and get it ready for simulation.
* If you don't have a circuit ready, you can use one of the demos.
* Follow best practices.

# Part 2: Simulation

After you have a schematic and have exported the netlist to a [spice](/terminology/spice) file, we can use [ngspice](https://ngspice.sourceforge.io/) to simulate it. 
In this part of the course you will start to learn spice, using it to simulate demo designs and then your own.

## Lab 2.1: DC, AC and Transient analysis

* Learn the main simulation types.
* Experiment with changing parameters.
* Common problems and how to troubleshoot them.
* Graphing with Xschem.

## Lab 2.2: Create your own testbench

* Use Xschem to create a testbench that provides stimulus for your design.
* Simulate your design and make some measurements.

# Part 3: Layout with Magic

In Part 3 you will learn how to use the [Magic VLSI tool](/terminology/magic/) to do layout. 
Magic has a definite learning curve, and will probably be quite unlike most GUI tools you’ve used. It takes a bit of getting used to, but as you gain familiarity it will get faster and easier to use.

## Lab 3.1: Magic Challenge!

* Get some experience with using Magic.
* Learn how to wire up basic components by completing the challenge.

## Lab 3.2: Layout your own design

* Create the components needed by your schematic and wire them up.
* Grow your understanding of how to wire up each type of component.
* Run [DRC](/terminology/drc) checks and solve any problems.

# Part 4: LVS

[LVS](/terminology/lvs) stands for Layout versus Schematic. It’s used in both the digital and analog flows. We compare the finished layout with the intended design. In the digital flow, we’re comparing the extracted circuit of the design with the gate level netlist. With the analog flow, we compare the drawn layout with the spice circuit.

## Lab 4.1.1 to 4.1.4: Solve LVS problems

* Each lab has its own problem and you will learn how to solve them and read the error reports.

## Lab 4.2: Run LVS on your own design

* Following on from part 3, you will make sure your design is LVS clean.

# Part 5: Post layout simulation

After the layout is done and we’ve shown that it matches the schematic with LVS, it’s a good idea to extract the circuit from the layout and see how it compares with the results we found in part 2. This is because the physical layout can impact the circuit, especially the parasitic resistances and capacitances.

## Lab 5.1: Inverter demo

* Run post layout simulation on the inverter demo.
* Add the extracted netlist into your testbench and simulate it.

## Lab 5.2: Run post layout simulation on your own design

* Extract the parasitics from your own layout.
* Simulate the final layout in your testbench.

# Part 6: Tapeout with Tiny Tapeout

Part of what makes this course unique and exciting is that you will be able to put your design onto a real ASIC. We use the [Tiny Tapeout](https://tinytapeout.com) shuttle service. In this part of the course you will learn the capabilities and limitations of Tiny Tapeout for analog design, and get your design ready to submit to the next shuttle.

## Lab 6.1

* Get your design ready to submit.
* Create the [GDS](/terminology/gds2) and LEF files needed.
* Document your design.
* Submit to the next Tiny Tapeout shuttle!

# Bonus Part 7: Mixed signal

A truly unique selling point of custom ASIC design is mixed signal. We can build circuits that are not possible any other way. This section will guide you through a mixed signal design I made, and show you how to make your own.

## Lab 7.1

* Guided walkthrough of a mixed signal design.
* Best practice structure of your files.
* How to do cosimulation of digital and analog together.
* A brief introduction to OpenLane for building the digital block.

{{% random_analog_quote %}}
