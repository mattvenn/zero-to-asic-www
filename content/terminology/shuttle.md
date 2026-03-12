---
title: "Shuttle"
description: A chip shuttle is a shared fabrication run (multi project wafer) where multiple designers submit designs to be manufactured together, spreading the cost of the mask set across all participants.
date: 2020-11-12T17:44:07+01:00
images: ["wafer.jpg"]
featured_image: "wafer.jpg"
faq:
  - q: What is a chip shuttle service?
    a: A shuttle service is the same as a multi project wafer — a shared fabrication run where multiple designers submit their designs to be manufactured together on one wafer, sharing the cost of the mask set.
  - q: What is the Caravel harness used in the ChipFoundry shuttle?
    a: In the ChipFoundry Shuttle designs can be placed within the user project area of the Caravel harness, which includes its own RISCV processor. This makes it easier to bring up and debug designs, at the cost of some available area.
  - q: What packaging did the Google shuttle provide?
    a: The Google shuttle returned chips in Wafer Level Chip Scale Packaging (WLCSP) and later easier-to-handle QFN package format.
---

A shuttle service is the same as a [multi project wafer](/terminology/mpw).

On 30th June 2020, [Tim Ansell](https://twitter.com/mithro) announced the collaboration between Google and Skywater to provide a free shuttle service in his FOSSI dialup talk.

{{< youtube EczW2IWdnOM >}}

These [slides taken from his talk](https://docs.google.com/presentation/d/e/2PACX-1vRtwZPc8ykkkgtUkHkoJZrP9jKOo3FYdKqbg-So0ic6_kx7ha1vHnxrWmuxWkTc9GfC8xl0TfEpMLwK/pub?start=false&loop=false&delayms=3000#slide=id.g8a02ce4cad_0_238) show the overview:

![shuttle](/shuttle.png)

## Chip Foundry Shuttle

Normally in an MPW you would have the whole [die](/terminology/die) to yourself. In the [ChipFoundry](https://chipfoundry.io/) Shuttle all the designs will be within the user project area of the [Caravel harness](https://github.com/chipfoundry/caravel). 

Caravel has its own RISCV processor and a neat [datasheet](https://caravel-harness.readthedocs.io/en/latest/). 
The idea here is to make it easier to bring up and debug your designs at the cost of some area.

![Caravel harness](/ciic_harness.png)

Read [this post to find out what you could fit in](/post/how-much-can-we-fit) the user space.

The Google shuttle returned chips in type of packaging called [Wafer Level Chip Scale Packaging](/terminology/wlcsp) and then the easier to handle QFN.
