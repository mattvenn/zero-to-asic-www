---
title: "Macro"
date: 2020-11-12T17:06:52+01:00
images: ["openram.jpg"]
featured_image: "openram.jpg"
---

From http://88physicaldesign.blogspot.com/2015/10/what-is-macro.html:

> Macros are intellectual properties that you can use in your design. You do not need to design it.
For example, memories, processor core, serdes, PLL etc. Macros might have a fixed function, or being parameterised. Your own design could become a fixed-function macro that some other designer could use, but a parameterised macro includes design elements and code that says how to build a macro to suit a particular set of parameters - for instance the number of words in a memory and how many bits wide it is.

A good example would be memory that's been created by OpenRAM. Typically for larger memories in a design you
want to avoid using lots of flip-flops. A memory created from flip-flops is much bigger than something that has
been optimised just for data storage. A memory made with flops would also likely be slower and much more power hungry than a sensibly designed memory macro, which might make use of special function cells that are not part of the standard cell library used by synthesis.

OpenRAM creates a macro that you can then use in your design without having to deal with the details inside.

![openram](/openram.jpg)

This talk by Matt Guthaus explains OpenRAM and its current status. [Skywater 130](/terminology/pdk) support is being added
and is being tested in the first [tapeouts](/terminology/tapeout).

{{< youtube 9Lw83kFtnc4 >}}
