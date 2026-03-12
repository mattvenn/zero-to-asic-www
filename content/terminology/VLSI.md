---
title: "VLSI"
date: 2020-11-12T17:44:33+01:00
images: ["die.jpg"]
featured_image: "die.jpg"
description: Very Large Scale Integration (VLSI) refers to ICs containing thousands or more MOSFETs on a single chip, a term that emerged in the 1970s as transistor counts grew into the thousands and beyond.
faq:
  - q: What does VLSI stand for and when did it originate?
    a: VLSI stands for Very Large Scale Integration. The term started being used in the 1970s when thousands of MOSFETs were being integrated together to make a single IC.
  - q: How many transistors are in a modern VLSI chip?
    a: Transistor counts have grown enormously over time. The Intel 4004 in 1971 had 2300 transistors, the Intel Pentium 4 in 2002 had 551 million, and the Apple M1 Ultra in 2022 has 114 billion transistors.
  - q: How many standard cells are in a typical open source ASIC submission?
    a: A group MPW5 submission described on the site totalled 91569 standard cells across all designs. The number of transistors is much higher — a flip-flop alone contains around 30 transistors.
---

Very Large Scale Integration - this term started getting used in the 70s when thousands of [MOSFETs](/terminology/mosfet) were
integrated together to make one [IC](/terminology/ic).

![timeline](/timeline.jpg)

Image from https://www.computerhistory.org/

Some notable dates:

| What                                  | Who                             | When     |
|---------------------------------------|---------------------------------|----------|
| First transistor                      | Morris Tanenbaum                | 1954     |
| First [IC](/terminology/ic)           | Kilby & Noyce                   | 1958     |
| First [MOSFET](/terminology/mosfet)   | Mohamed M. Atalla & Dawon Kahng | 1959     |
| [CMOS](/terminology/cmos) invented    | Frank Wanlass                   | 1963     |
| Intel 4004, 2300 transistors          | Federico Faggin                 | 1971     |
| 6502 CPU with 3510 transistors        | MOS technolog y                 | 1975     |
| Z80 CPU with 8500 transistors         | Federico Faggin                 | 1976     |
| Introduction to VLSI Systems published| Mead & Conway                   | 1980     |
| Intel 486 with 1M transistors         | Intel                           | 1988     |
| Intel Pentium 3.1M transistors        | Intel                           | 1993     |
| Intel Pentium 4 551M transistors      | Intel                           | 2002     |
| Mac M1 Ultra 114B transistors         | Apple                           | 2022     |

---

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

Summing across all designs we have a total of 91569 [standard cells](/terminology/standardcell), but the number of transistors will be a lot higher.
A flip flop has around 30 transistors, whereas a single inverter has only 2.

Here's the floorplan of our MPW5 submission:

![MPW5 submission](/mpw5_multi_macro.png)

You can read more about [VLSI on the wikipedia page](https://en.wikipedia.org/wiki/Very_Large_Scale_Integration)
