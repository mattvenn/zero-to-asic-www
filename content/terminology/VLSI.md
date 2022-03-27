---
title: "VLSI"
date: 2020-11-12T17:44:33+01:00
images: ["die.jpg"]
featured_image: "die.jpg"
---

Very Large Scale Integration - this term started getting used in the 70s when millions of [MOSFETs](/terminology/mosfet) were
integrated together to make one [IC](/terminology/ic).

The first book I read about VLSI was by Carver Mead & [Lynn Conway](https://ai.eecs.umich.edu/people/conway/conway.html) - Introduction to VLSI systems. It's pretty dated now but still an interesting read, giving a general overview of the ideas involved.

I thought it would be fun to take our last [group submission for MPW5](/post/mpw5_submitted) and get a cell count for all the designs and the total application. I didn't count the shared ram support or filler cells (they just fill in the space between the cells we actually need for the design to work).

    Function generator       2199 cells
             VGA Clock       1892 cells
     Frequency counter       1146 cells
             RGB Mixer       1381 cells
              Hack soc       4881 cells
                 teras      16970 cells
              ALU74181        866 cells
              vga demo       5823 cells
                SiLife      46874 cells
    wrapped_acorn_prng       3739 cells
             HSV Mixer       4951 cells
              SkullFET        847 cells

Summing across all designs we have a total of 91569 standard cells.

And here's the floorplan of our submission:

![MPW5 submission](/mpw5_multi_macro.png)

You can read more about [VLSI on the wikipedia page](https://en.wikipedia.org/wiki/Very_Large_Scale_Integration)
