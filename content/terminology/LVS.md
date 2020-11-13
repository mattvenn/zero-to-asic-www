---
title: "LVS"
date: 2020-11-12T17:43:29+01:00
description: "Layout vs Schematic"
featured_image: "/lvs.png"
---

Layout vs Schematic is an important [verification](/terminology/verification) step.

After the design has been finished and we have the [GDS2](/terminology/gds2) files that we can send to the [foundry](/terminology/foundry), we want to check that the design is the same as the input that was described by the [HDL](/terminology/hdl).

In the [OpenLane](/terminology/openlane) tool, at the end we have the LVS step. The [netlist](/terminology/netlist) is extracted using [Magic](/terminology/magic)
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

