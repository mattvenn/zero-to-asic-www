---
title: "Synthesis"
date: 2020-11-12T17:43:01+01:00
images: ["show_rtl.png"]
featured_image: "show_rtl.png"
---

Synthesis is kind of analogous to the compiler used for sequential programming languages like C.
It reads the [HDL](/terminology/hdl) and creates a [netlist](/terminology/netlist).

It is a very complex and detailed process. Until Claire Wolf wrote yosys, it was thought that only huge semiconducter companies
had the resouces to write a synthesis tool.

[yosys](https://github.com/YosysHQ/yosys) is the Open Source tool that has been crucial in enabling the Open Source ASIC flow we have in [OpenLane](/terminology/openlane).

If things are going well, you normally don't need to interact much with yosys. It will be part of a tool flow or Makefile.

If your design is broken in some way, then it is definitely worth learning how to use the built in _show_ tool.

{{< youtube a2sLfoinQds >}}

You can read the [white paper here](http://bygone.clairexen.net/yosys/files/yosys_appnote_011_design_investigation.pdf)
