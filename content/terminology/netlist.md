---
title: "Netlist"
date: 2020-11-13T10:13:03+01:00
images: ["show_rtl.png"]
featured_image: "show_rtl.png"
---
A netlist is a machine readable file that contains all the connections between all the components in your design.

They are one of the outputs of a [Synthesis](/terminology/synthesis) tool like Yosys.

These examples are taken from http://bygone.clairexen.net/yosys/screenshots.html

If you have a counter design written in an [HDL](/terminology/hdl) like Verilog

    module counter (clk, rst, en, count);

       input clk, rst, en;
       output reg [3:0] count;
       
       always @(posedge clk)
          if (rst)
             count <= 4'd0;
          else if (en)
             count <= count + 4'd1;

    endmodule

The output netlist can be visualised like this:

![show RTL](/show_rtl.png)

You can see the blocks are fairly 'high level', like multiplexors ($mux), or adders ($add). These types of blocks are not part of
the Skywater [PDK](/terminology/pdk), so they need to be broken down into more simple blocks.

![show RTL](/show_cmos.png)

These blocks are now simple enough that they can be mapped onto the [standard cells](/terminology/standardcell) we have in the PDK.
The synthesis process is the first step in the [OpenLane](/terminology/openlane) tool.
