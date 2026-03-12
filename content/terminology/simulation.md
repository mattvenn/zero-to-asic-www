---
title: "Simulation"
description: Simulation runs a design against test stimuli to observe its behaviour, with digital simulators checking logic at scale and analog simulators like SPICE modelling voltages and currents at the transistor level.
date: 2020-11-13T11:58:01+01:00
images: ["simulation.png"]
featured_image: "simulation.png"
faq:
  - q: What are the two main types of chip simulation?
    a: Digital simulation models all signals as 1s and 0s (with additional values for tristates and uninitialised signals) and is designed to verify large circuits functionally. Analog simulation models voltages and currents in detail but is very compute-intensive, typically limited to circuits of a few hundred transistors.
  - q: What open source digital simulators are available?
    a: Several open source digital simulators are available including Icarus Verilog, Verilator, and CXXRTL. For writing testbenches, cocotb is a popular framework that allows complex stimulus to be written in Python rather than Verilog.
  - q: What is a VCD file in digital simulation?
    a: A VCD (Value Change Dump) is the data format used to store simulation results. Values are only recorded when a signal changes rather than at every time step, minimising file sizes — though multi-gigabyte dump files are not unusual.
video_id: dtK-4JZ4Cwc
---

Simulation lets us see the design working. It's useful for debugging while designing and it can also be used to verify that the design is working correctly.

There are two main types of simulations: digital simulation, and analog or circuit simulation. Digital simulation models all signals as either 1's and 0's or a small number of values to model tristates and uninitialised values. Analog simulation model voltages and currents and look in detail at the way devices work. Analog simulations are very compute intensive - it is unusual to simulate circuits larger than a few hundred transistors. Digital simulators are designed to verify the functionality of large circuits, but are not accurate on voltages and may not even estimate timing delays at all. The fastest digital simulators only capture the values at the end of each clock cycle (cycle-based simulators). 

The classic analog chip simulator is [SPICE](/terminology/spice) (Simulation Program with Integrated Circuit Emphasis). It is often used to characterise standard cells, to build the timing models that underly STA.

There are quite a few Open Source digital simulators available: [Icarus Verilog](http://iverilog.icarus.com/), [Verilator](https://www.veripool.org/wiki/verilator) and recently [CXXRTL](https://tomverbeure.github.io/2020/08/08/CXXRTL-the-New-Yosys-Simulation-Backend.html).

For digital simulation, we provide our [HDL](/terminology/hdl) design and a testbench and we get back a data dump of the results of the simulation.
The data is usually in the form of a VCD (value change dump). This is a way of minimising file sizes, values are only recorded when a signal changes, not at every time step. It's not unusual to get multi-gigabyte dump files.

Here's an example dump from the [seven segment seconds](https://github.com/mattvenn/seven-segment-seconds) example.

![simulation](/simulation.png)

The testbench provides a clock and reset if required, and then runs the design for some time, capturing and maybe toggling various signals.
Above you can see the clock toggling too fast to see at this scale, and the digits slowly counting up to 9 and rolling over to 0. Underneath you can see the various elements of a 7 segment
display turning on and off to show the digit.

Traditionally testbenches have been written in Verilog, but I am now using a testing framework called [coco-tb](https://docs.cocotb.org/en/stable/). 
This makes it much easier to provide complex stimulus to the device under test (DUT).

Jump to [3:27](https://www.youtube.com/watch?v=dtK-4JZ4Cwc&t=207s) in this video to see a demonstration of cocotb being used to pass wavefiles through a filter implemented for an [FPGA](/terminology/fpga).

{{< youtube dtK-4JZ4Cwc >}}

Simulation on its own can take us a fair way, but to be sure you should also [verify](/terminology/verification) your design.
