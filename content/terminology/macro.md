---
title: "Macro"
date: 2020-11-12T17:06:52+01:00
images: ["openram.jpg"]
featured_image: "openram.jpg"
description: A macro is a reusable, pre-designed intellectual property block — such as a memory, processor core, or PLL — that designers incorporate into their chip without redesigning the internals.
faq:
  - q: What is a macro in chip design?
    a: A macro is a pre-designed intellectual property block that you can use in your design without designing it yourself. Examples include memories, processor cores, SerDes, and PLLs. Macros may have a fixed function or be parameterised.
  - q: Why use a memory macro instead of building memory from flip-flops?
    a: A memory created from flip-flops is much bigger, slower, and more power hungry than an optimised memory macro. Memory macros can use special function cells outside the standard cell library to achieve much better density and performance.
  - q: What is OpenRAM?
    a: OpenRAM is an open source tool that generates memory macros. It creates a macro you can use in your design without dealing with the internal details, and Skywater 130 support was being added and tested in early tapeouts.
video_id: 9Lw83kFtnc4
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
