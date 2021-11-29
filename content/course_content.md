---
title: "Course content"
description: "What will I learn?"
date: 2021-07-14T15:41:50+02:00
images: ["maximo_render_3.jpeg"]
featured_image: "maximo_render_3.jpeg"
tags: ["course"]
---

{{< coursecontent-tag >}}

# Part 1: MOSFETs and the Skywater130 standard cells

[MOSFETs](/terminology/mosfet) are the building blocks of the chips we will be learning how to make. While we don’t need an in depth knowledge of how they work, it’s useful to see how they are joined together into functional blocks known as standard cells - for example AND gates or Flip-Flops.

* Basic understanding of how MOSFETs work.
* How are they constructed on a silicon wafer.
* How to run a simulation with ngspice.

## Project 1.1: Choose a standard cell and simulate it

* Get an overview of what the [standard cells](/terminology/standardcell) are.
* Choose your favourite cell, simulate it and show it does what it should.
* Measure how fast it can propagate signals from input to output.

## Project 1.2: Draw a mosfet in magic

* Learn the basics of the [Magic VLSI](/terminology/magic) tool.
* Extract the circuit from a drawing.
* Simulate with [ngspice](/terminology/spice).

# Part 2: Building Digital Designs

As we are focussing on digital design for making our ASIC we need to be able to efficiently describe the kind of hardware we want. [Verilog](/terminology/hdl) is one of a few languages used for this purpose. It’s well supported by the Open Source tools.

At the same time we will be learning how to run simulations so you can test your designs as you go.

This part of the course can be done completely with simulation, or you can use an [FPGA](/terminology/fpga) development board to help you. See [FAQ](/contact#fpga).

The following topics will be covered:

* Designing digital circuits, data flow and control.
* Combinatorial logic.
* Sequential logic.
* Finite state machines.
* Modularity.

The labs are split up into the following projects, although if you already have some design skills you are free to choose other projects.

## Project 2.1: RGB Colour mixer

* Build a Digital rotary encoder.
* Build a PWM driver.
* Combine them both to make a 3 channel RGB LED driver.

## Project 2.2: Frequency counter

* Make an edge detector for an incoming digital signal.
* Build a 2 digit seven segment driver.
* Count edges in a fixed number of clock cycles and format to decimal.
* Use a state machine to sequence the conversion from binary to decimal.

# Part 3: Verification

We will take a quick look at [Formal Verification](/terminology/verification) and see how to use it to prove a digital design is working as desired.

* Bounded model checking.
* Assumptions and assertions.
* How to use the Open Source Formal Verification tools.

## Project 3.1: Prove your design is safe

* Write a cover statement to show the timer starting and ending.
* Write some assertions to prove the timer works as designed.

## Project 3.2: Prove the project wrapper is safe

* Put the RGB mixer design inside the project wrapper.
* Write some assertions that prove the design is safe in a multi project environment.
* Run the formal tools to make the proof.

# Part 4: OpenLANE

[OpenLANE](/terminology/openlane) is an automated set of tools to turn a digital design into the files needed for creating an ASIC. It is automated but it needs to be configured correctly to get usable results. We will cover:

* The different stages of the flow.
* How to interpret results, logs and errors.
* Design Rule Check ([DRC](/terminology/drc))
* Layout vs Schematic ([LVS](/terminology/lvs))
* Basic configuration setting.

## Project 4.1: harden an example design

* Choose an example design from the OpenLANE.
* Read the config and check the documentation.
* Run the tools and inspect the results.

## Project 4.2: harden your design

* Use OpenLane to create the [GDS](/terminology/gds2) files for your own design
* Learn how to resolve some basic errors
* Learn how to use the design exploration tools to help find the best results
* Make adjustments to your config for either personal or group submission.

## Part 5: Google/Skywater/Efabless shuttle

The way to make ASIC fabrication cheaper is to parcel out the wafer into chunks and sell each chunk individually, this is known as a shuttle service or an [MPW](/terminology/mpw). Google has sponsored a shuttle service that will be running once every few months during 2021.
Efabless are providing the intermediary services between the Skywater factory and applicants.

All applicants need to make use of a wrapper design called Caravel that encloses your own design. This wrapper includes a RISCV CPU, some memory and some peripherals. This can help take some of the burden off your own design as you can make use of existing peripherals.

We will be combining all the designs together using a special multiplexer harness I have developed. This allows us to put many independent designs into the one application.

You will learn:

* The component parts of [Caravel](/terminology/shuttle).
* How big a space there is inside for your designs.
* How to simulate it, including your own design.
* How to fulfil the application process and make your own application should you wish.

## Project 5.1: Simulate your design inside Caravel

* Run Caravel’s example project’s test.
* Add your design to Caravel: design files, SoC firmware, testbench.
* Simulate your design within Caravel.

## Project 5.2: Making a personal submission to Efabless

* Get your design’s GDS files in place.
* Build the final GDS for Caravel.
* Run the checker script.

## Project 5.3: Making a group submission

* Wrap your small design ready for aggregating into the group submission.
* How to prepare your repository.
* Submit your design.

