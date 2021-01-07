---
title: Sign up
featured_image: '/die.jpg'
type: page
menu: main
---

Sign up to the newsletter to keep up to date with all things Zero to ASIC and to get alerted when new tickets are released.

{{< mail-chimp >}}

# 0 to ASIC course

{{< youtube 50kPORZlFzU >}}

Design and fabricate your own [ASIC](/terminology/asic)! Thanks to the new Open Source [Process Development Kit](/terminology/pdk) from Google and Skywater along with the latest Open Source ASIC tools from [Efabless](https://efabless.com/).

GCC revolutionised compiling, Linux revolutionised computing. Arduino revolutionised microcontrollers. RISCV is revolutionising ISAs. The next step is Open Source Silicon. 

This workshop will allow the opportunity for people to experience creating their own microchips, using free and Open Source tools. We will concentrate on digital design.

# Overview

## Format

* 7 hands-on projects, each with video and text guides.
* 6 weeks support via discord server and weekly office hours.
* Asynchronous - do in your own time.
* A PCB will be optionally available to buy with ASIC pre-soldered for you - see [FAQ](#faq).
* High resolution set of digital images of the decapped ASIC - see [FAQ](#faq).
* Course completion certificate.

## Prerequisites

* Basic Linux command line experience helpful.
* Some Linux exposure helpful.

## Cost

$500.

# Part 1: MOSFETs and the Skywater130 standard cells

MOSFETs are the building blocks of the chips we will be learning how to make. While we don’t need an in depth knowledge of how they work, it’s useful to see how they are joined together into functional blocks known as standard cells - for example AND gates or Flip-Flops.

* Basic understanding of how MOSFETs work.
* How are they constructed on a silicon wafer.
* How to run a simulation with ngspice.

## Project 1.1: Choose a standard cell and simulate it

* Get an overview of what the standard cells are.
* Choose your fighter!
* Simulate the cell and show it does what it should.
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

* Build a 4 digit seven segment driver.
* Debounce a digital input.
* Combine them both with a clock and a register to make a frequency counter.

# Part 3: Verification

We will take a quick look at Formal Verification and see how to use it to prove a digital design is working as desired.

* Bounded model checking.
* Assumptions and assertions.
* How to use the Open Source Formal Verification tools.

## Project 3.1: prove your design is safe

* Add a feature to one of your projects so that when reset is active the outputs are low.
* Use formal verification to prove it.

# Part 4: OpenLane

OpenLANE is an automated set of tools to turn a digital design into the files needed for creating an ASIC. It is automated but it needs to be configured correctly to get usable results. We will cover:

* The different stages of the flow.
* How to interpret results, logs and errors.
* Design Rule Check (DRC)
* Layout vs Schematic (LVS)
* Basic configuration setting.

## Project 4.1: harden your design

* Setup OpenLane on your computer.
* Configure the config file.
* Run the flow.
* Inspect the results and check the design fits within your allotted area.

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

## Project 5.1: Prepare a Shuttle submission for your own design

* Integrate your previously hardened project into the Caravel design.
* Make sure it passes pre-check requirements.
* Make the application using efabless’s site.

# FAQ

Q. Will I definitely get an ASIC with my design on it?

No, an ASIC is not guaranteed. To keep the cost of the course reasonable we have to rely on the Google/Skywater free shuttle. The shuttle is currently run as a lottery and while we have a good chance of getting in there is no guarantee. You are able to make your own application separately to the group if you wish.

If the application doesn’t make it onto the shuttle, then that also means we don’t get the decapped photos.

Q. How much will the PCB be?

If we are successful and get on the shuttle, then I will organise mounting and posting a PCB with a sample ASIC to people who want one. This will cost $50 + $15 postage and packing.

Q. How big can I make my custom project?

You will have at least 300 x 300 um which is quite a lot of space for a small digital design. If you need bigger then you can separately apply to the Google/Skywater shuttle.

Q. Can I team up with other course participants and get more space?

Yes, that’s fine.

Q. How long does the whole course take to complete?

It depends on your existing level of experience and how deep you want to go on your own project. I would say between 20 and 100 hours.

Q. Is there a time limit to complete the course?

You can take as long as you want with the course materials, but I will only be able to support you on discord or office hours for the 6 week length of the course.

Q. Do I need an FPGA to develop my design?

For simple and small designs like the ones I include in the course, you can use simulation to check everything is working fine. If you want to make a more complex project, then it’s probably a good idea to test your design on an FPGA.

Q. Refunds?

Attendees can receive refunds up to 7 days before the event start date.

In the case that there are not enough participants, the course may be cancelled and a full refund given.

{{< mail-chimp >}}
