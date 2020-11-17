---
title: "Simulation"
description: "simulating your digital design"
date: 2020-11-13T11:58:01+01:00
featured_image: "/simulation.png"
---

Simulation lets us see the design working. It's useful for debugging while designing and it can also be used to verify that the design is working correctly.

There are quite a few Open Source simulators available: [Icarus Verilog](http://iverilog.icarus.com/), [Verilator](https://www.veripool.org/wiki/verilator) and recently [CXXRTL](https://tomverbeure.github.io/2020/08/08/CXXRTL-the-New-Yosys-Simulation-Backend.html).

We provide our [HDL](/terminology/hdl) design and a testbench and we get back a data dump of the results of the simulation.
The data is usually in the form of a VCD (value change dump). This is a way of minimising file sizes, only when and what values changed are dumped. It's not unusual to get multi-gigabyte dump files.

Here's an example dump from the [seven segment seconds](https://github.com/mattvenn/seven-segment-seconds) example.

![simulation](/simulation.png)

The testbench provides a clock and reset if required, and then runs the design for some time, capturing and maybe toggling various signals.
Above you can see the clock toggling too fast to see, and the digits slowly counting up to 9 and rolling over to 0. Underneath you can see the various elements of a 7 segment
display turning on and off to show the digit.

Traditionally testbenches have been written in Verilog, but I am now using a testing framework called [coco-tb](https://docs.cocotb.org/en/stable/). 
This makes it much easier to provide complex stimulus to the device under test (DUT).

Jump to [3:27](https://www.youtube.com/watch?v=dtK-4JZ4Cwc&t=207s) in this video to see a demonstration of cocotb being used to pass wavefiles through a filter implemented for an [FPGA](/terminology/fpga).

{{< youtube dtK-4JZ4Cwc >}}

Simulation on its own can take us a fair way, but to be sure you should also [verify](/terminology/verification) your design.
