---
title: "LVS"
date: 2020-11-12T17:43:29+01:00
description: Layout vs Schematic (LVS) is a verification step that confirms the physical chip layout matches the intended netlist from synthesis, catching shorts and missing connections before manufacture.
images: ["lvs.png"]
featured_image: "lvs.png"
faq:
  - q: What is Layout vs Schematic (LVS) verification?
    a: LVS compares the netlist extracted from the final physical layout (GDS2) against the netlist produced by synthesis, verifying that the manufactured chip will match the designer's intended circuit.
  - q: What tools are used for LVS in the LibreLane flow?
    a: In LibreLane, Magic extracts the netlist from the layout, and a tool called Netgen compares that extracted netlist with the netlist from the synthesis step.
  - q: What are common LVS errors when using LibreLane?
    a: The most common LVS errors with LibreLane are power supplies not being connected for some reason, and short circuits introduced during routing.
---

Layout vs Schematic (or LVS) is an important [verification](/terminology/verification) step.

After the design has been finished and we have the [GDS2](/terminology/gds2) files that we can send to the [foundry](/terminology/foundry), we want to check that the design is the same as the input that was described by the [HDL](/terminology/hdl) or schematic.

In the [LibreLane](/terminology/librelane) tool, at the end we have the LVS step. The [netlist](/terminology/netlist) is extracted using [Magic](/terminology/magic)
A tool called [Netgen](http://opencircuitdesign.com/netgen/) can compare this extracted netlist with the one we get after the [synthesis](/terminology/synthesis) step.

You will get some reports in the run directory. In the inverter example I have this file: results/lvs/inverter.lvs.log

The end of the file shows the input and output are equivalent.

    Subcircuit pins:
    Circuit 1: inverter                        |Circuit 2: inverter                        
    -------------------------------------------|-------------------------------------------
    in                                         |in                                         
    out                                        |out                                        
    VGND                                       |VGND                                       
    VPWR                                       |VPWR                                       
    ---------------------------------------------------------------------------------------
    Cell pin lists are equivalent.
    Device classes inverter and inverter are equivalent.
    Circuits match uniquely.

The most common types of LVS errors I've seen with LibreLane are:

* when power supplies aren't connected for some reason,
* there is a short circuit during routing.

Verification essentially tries to show that the final design meets the designer's intention. This takes various stages:

1) simulate the initial design (HDL or schematic) to show it behaves in the intended way
2) synthesise this down to a netlist,
3) simulate this again to show it still works - or use other tools such as formal proof to show it is equivalent to the original design 
4) place and route it to get a final design
5) use LVS to show that this design is still the same as the netlist from synthesis
6) use other steps (simulation, or preferably STA) to show the final design performs well enough
