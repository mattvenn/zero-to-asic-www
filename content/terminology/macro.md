---
title: "Macro"
date: 2020-11-12T17:06:52+01:00
featured_image: "/openram.jpg"
---

From http://88physicaldesign.blogspot.com/2015/10/what-is-macro.html:

> Macros are intellectual properties that you can use in your design. You do not need to design it.
For example, memories, processor core, serdes, PLL etc. 

A good example would be memory that's been created by OpenRAM. Typically for larger memories in a design you
want to avoid using lots of flip-flops. A memory created from flip-flops is much bigger than something that has
been optimised just for data storage.

OpenRAM creates a macro that you can then use in your design without having to deal with the details inside.

![openram](/openram.jpg)

This talk by Matt Guthaus explains OpenRAM and its current status. [Skywater 130](/terminology/pdk) support is being added
and is being tested in the first [tapeouts](/terminology/tapeout).

{{< youtube 9Lw83kFtnc4 >}}
