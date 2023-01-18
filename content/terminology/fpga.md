---
title: "FPGA"
date: 2020-11-13T15:42:06+01:00
description: "Field Programmable Gate Array"
images: ["fpga-lut.png"]
featured_image: "fpga-lut.png"
---

An FPGA, or field programmable gate array, is a way to implement a digital circuit on a chip without fabricating it from scratch. This allows the designer to get a result more quickly, which can be useful for prototyping, and is much cheaper if only a small number of the chips need to be produced. If millions of devices need to be made, then an ASIC is probably going to be much cheaper than using FPGAs for the same function, and will have higher performance.

An FPGA is quite like an [ASIC](/terminology/asic), but has some major differences.

* Available to buy blank chips cheaply, off-the-shelf
* Can program your digital design onto them, over and over again
* Have a very limited set of [standard cells](/terminology/standardcell) - at the least lookup tables, flip-flops, memories. Could include multipliers,  memory controllers or other high speed interfaces.
* No analogue capability
* Slower than an ASIC

They have a reasonable overlap of the tools required to design for them. FPGAs need [synthesis](/terminology/synthesis), [place and route](/terminology/place_and_route), [simulation](/terminology/simulation) and [verification](/terminology/verification) tools. Additionally you need a tool that can take the finished bitstream and send that to the FPGA for programming.

An FPGA consists of a huge amount of repeated logic elements/blocks/slices. These pictures are of the Lattice iCE40 FPGA.

![FPGA overview](/fpga-overview.png)

These usually contain a lookup table, a flip-flop and some carry-logic (speeds up addition).
The lookup table can be programmed to model any type of gate - for example an inverter or a 4 input NAND.

![FPGA LUT](/fpga-lut.png)

# FPGA boards

An FPGA board can help you test your digital design at speed. For example I can simulate my [vga clock](/post/vga_clock), and even simulate the screen. But with an FPGA I can actually plug it into a real screen and see it works.

If you want to buy an FPGA board to play with and help you learn digital design, I recommend going for one with an active, supportive community:

* [iCEBreaker](https://www.crowdsupply.com/1bitsquared/icebreaker-fpga)
* [TinyFPGA](https://tinyfpga.com/)
* [Black Ice](https://www.tindie.com/products/Folknology/blackice-mx/)

# Learn more

If you're interested in learning how the Open Source FPGA tool flow works from end to end, check this video series I did for Symbiotic EDA.

{{< youtube A5AHglpfdtQ >}}
