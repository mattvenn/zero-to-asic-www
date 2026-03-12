---
title: "FPGA"
date: 2020-11-13T15:42:06+01:00
description: A Field Programmable Gate Array (FPGA) is a chip containing programmable logic blocks that can implement any digital circuit without custom fabrication, enabling fast prototyping but at lower performance than a custom ASIC.
images: ["fpga-lut.png"]
featured_image: "fpga-lut.png"
faq:
  - q: What is an FPGA and how does it differ from an ASIC?
    a: An FPGA is a chip with programmable logic that can implement a digital circuit without custom fabrication. Unlike an ASIC it can be reprogrammed over and over, is available off-the-shelf cheaply, and is faster to deploy. However it is slower than an ASIC, has no analog capability, and becomes more expensive if millions of units are needed.
  - q: How does an FPGA implement logic?
    a: An FPGA consists of a huge number of repeated logic elements, each typically containing a lookup table (LUT), a flip-flop, and carry logic. The LUT can be programmed to model any type of gate, such as an inverter or a 4-input NAND.
  - q: What tools does FPGA design share with ASIC design?
    a: FPGAs require synthesis, place and route, simulation, and verification tools — the same categories needed for ASIC design. The main additional tool needed for FPGAs is one that programs the finished bitstream onto the device.
---

An FPGA, or field programmable gate array, is a way to implement a digital circuit on a chip without fabricating it from scratch. This allows the designer to get a result more quickly, which can be useful for prototyping, and is much cheaper if only a small number of the chips need to be produced. If millions of devices need to be made, then an ASIC is probably going to be much cheaper than using FPGAs for the same function, and will have higher performance.

An FPGA is quite like an [ASIC](/terminology/asic), but has some major differences.

* Available to buy blank chips cheaply, off-the-shelf
* Can program your digital design onto them, over and over again
* Have a very limited set of [standard cells](/terminology/standardcell) - at the least lookup tables, flip-flops, memories. Could include multipliers,  memory controllers or other high speed interfaces.
* No analog capability
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
