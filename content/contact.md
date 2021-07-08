---
title: Buy a ticket
featured_image: 'maximo_render_3.jpeg'
image_pos: 0px -100px
type: page
menu: main
---

{{< youtube Jf3ltgG5uck >}}

# Want to learn to make your own chips?

Learn to design and fabricate your own [ASIC](/terminology/asic)! Thanks to the new Open Source [Process Development Kit](/terminology/pdk) from Google and Skywater along with the OpenLANE ASIC tools from [Efabless](https://efabless.com/).

GCC revolutionised compiling, Linux revolutionised computing. Arduino revolutionised microcontrollers. RISCV is revolutionising ISAs. The next step is Open Source Silicon. 

This course will give you the experience creating your own microchip, using free and Open Source tools. 


14 people who took the course in the last 6 months have [already submitted designs for MPW2](/post/mpw2-submitted/).

* [$550 standard ticket with 1 hour of office hours](https://buy.stripe.com/7sIdTHedSaKe9NubIJ)
* [$850 pro ticket with 4 hours of office hours](https://buy.stripe.com/6oE3f3b1GaKe4ta146)

# What do people say about the course?

{{< youtube fjpFWogQl8Y >}}

# Course Overview

* We will concentrate on digital design.
* A virtual machine is available or you can install the tools manually. 
* The course has now been updated to match the MPW2 submission process.

## Format

* 11 hands-on projects, supported with text guides and over 6 hours of videos.
* Support via discord community server and 1 to 1 office hours.
* Weekly course hangout call.
* Asynchronous - do in your own time.
* A PCB will be optionally available to buy with ASIC pre-soldered for you - see [FAQ](#faq).
* High resolution set of digital images of the decapped ASIC - see [FAQ](#faq).
* Access to the course materials for the lifetime of the course.
* Course completion certificate.

## Prerequisites

* Basic Linux command line experience helpful.
* Some programming experience helpful.

# Part 1: MOSFETs and the Skywater130 standard cells

MOSFETs are the building blocks of the chips we will be learning how to make. While we don’t need an in depth knowledge of how they work, it’s useful to see how they are joined together into functional blocks known as standard cells - for example AND gates or Flip-Flops.

* Basic understanding of how MOSFETs work.
* How are they constructed on a silicon wafer.
* How to run a simulation with ngspice.

## Project 1.1: Choose a standard cell and simulate it

* Get an overview of what the standard cells are.
* Choose your favourite cell, simulate it and show it does what it should.
* Measure how fast it can propagate signals from input to output.

## Project 1.2: Draw a mosfet in magic

* Learn the basics of the Magic VLSI tool.
* Extract the circuit from a drawing.
* Simulate with ngspice.

# Part 2: Building Digital Designs

As we are focussing on digital design for making our ASIC we need to be able to efficiently describe the kind of hardware we want. Verilog is one of a few languages used for this purpose. It’s well supported by the Open Source tools.

At the same time we will be learning how to run simulations so you can test your designs as you go.

This part of the course can be done completely with simulation, or you can use an FPGA development board to help you. See [FAQ](#faq).

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

We will take a quick look at Formal Verification and see how to use it to prove a digital design is working as desired.

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

OpenLANE is an automated set of tools to turn a digital design into the files needed for creating an ASIC. It is automated but it needs to be configured correctly to get usable results. We will cover:

* The different stages of the flow.
* How to interpret results, logs and errors.
* Design Rule Check (DRC)
* Layout vs Schematic (LVS)
* Basic configuration setting.

## Project 4.1: harden an example design

* Choose an example design from the OpenLANE.
* Read the config and check the documentation.
* Run the tools and inspect t

## Project 4.2: harden your design

* Use OpenLane to create the GDS files for your own design
* Learn how to resolve some basic errors
* Learn how to use the design exploration tools to help find the best results
* Make adjustments to your config for either personal or group submission.

## Part 5: Google/Skywater/Efabless shuttle

The way to make ASIC fabrication cheaper is to parcel out the wafer into chunks and sell each chunk individually, this is known as a shuttle service or an MPW. Google has sponsored a shuttle service that will be running once every few months during 2021.
Efabless are providing the intermediary services between the Skywater factory and applicants.

All applicants need to make use of a wrapper design called Caravel that encloses your own design. This wrapper includes a RISCV CPU, some memory and some peripherals. This can help take some of the burden off your own design as you can make use of existing peripherals.

We will be combining all the designs together using a special multiplexer harness I have developed. This allows us to put many independent designs into the one application.

You will learn:

* The component parts of Caravel.
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

# FAQ

Q. Will I definitely get an ASIC with my design on it?

No, an ASIC is not guaranteed. To keep the cost of the course reasonable we have to rely on the Google/Skywater free shuttle. The shuttle is currently run as a lottery and while we have a good chance of getting in there is no guarantee. You are able to make your own application separately to the group if you wish.

If the application doesn’t make it onto the shuttle, then that also means we don’t get the decapped photos.

Q. How much will the PCB be?

If we are successful and get on the shuttle, then I will organise mounting and posting a PCB with a sample ASIC to people who want one. This will cost around $50 + $15 postage and packing.

Q. How big can I make my custom project?

You will have at least 300 x 300 um which is quite a lot of space for a small digital design. If you need bigger then you can make an individual application to Efabless.

Q. Can I team up with other course participants and get more space?

Maybe, it's easier for me if all the projects are the same size with the same pinout.

Q. How long does the whole course take to complete?

It depends on your existing level of experience and how deep you want to go on your own project. Most people complete each section in 4 hours, so about 20 hours for coursework. 
Then you will need some amount of time to prepare your own project.

Q. Is there a time limit to complete the course?

You can take as long as you want with the course materials, but your office hours will expire after 6 months.

Q. When do I need to submit my final design?

It depends on the next shuttle. As we don't know this in advance I will check with you at the end of the course. If you want to submit to the group project I will give you a deadline of 1 month
before the shuttle closing date to make sure I have enough time to aggregate all the designs into a single submissions.

Q. Do I need an FPGA to develop my design?

For simple and small designs like the ones I include in the course, you can use simulation to check everything is working fine. If you want to make a more complex project, then it’s probably a good idea to test your design on an FPGA.

Q. Refunds?

If for any reason you are unhappy with the course you can ask for a refund.
