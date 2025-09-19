---
title: "Synthesis"
date: 2020-11-12T17:43:01+01:00
images: ["show_rtl.png"]
featured_image: "show_rtl.png"
---

Synthesis converts a behavioral description of the circuit, in the form of RTL, into an equivalent netlist made of cells from the standard cell library. It is analogous to the compilation process used for turning programming languages like C into binaries. The compiler knows how to read the language and maps it to the instructions we have available in the CPU, and synthesis translates from what we want the design to do, into a set of available cells that will perform it.

Synthesis reads the [HDL](/terminology/hdl) and creates a [netlist](/terminology/netlist) of wires and components that we have available in the target. 
In an FPGA those will be lookup tables (LUTs) and flip-flops. 
For ASIC, we have a large library of [standard cells](/terminology/standardcell); things like AND, OR, NOT and MUX gates as well as lots of flip-flop variants.

Synthesis proceeds in roughly this sequence:
1) convert the RTL into a set of equivalent logical operations, or generic cells
2) map the generic cells to ones available in the library
3) analyse the timing of the circuit and identify areas that need improvement
4) change the way the troublesome areas are implemented aiming to fix timing
5) iterate to (3) until timing is fixed or we run out of effort

It is a very complex and detailed process with lots of tuning options to trade off area vs speed. Until Claire Wolf wrote yosys, it was thought that only huge semiconducter companies
had the resouces to write a synthesis tool.

[Yosys](https://github.com/YosysHQ/yosys) is the Open Source tool that has been crucial in enabling the Open Source ASIC flow we have in [LibreLane](/terminology/librelane).

If things are going well, you normally don't need to interact much with yosys. It will be part of a tool flow or Makefile.

If your design is broken in some way, then it is definitely worth learning how to use the built in _show_ tool.

<!-- {{< youtube a2sLfoinQds >}} -->

You can read the [documentation about design investigation here](https://yosyshq.readthedocs.io/projects/yosys/en/0.35/appendix/APPNOTE_011_Design_Investigation.html).
