---
title: "Google / Skywater Shuttle"
description: "free ASIC service"
date: 2020-11-12T17:44:07+01:00
images: ["wafer.jpg"]
featured_image: "wafer.jpg"
---

A shuttle service is the same as a [multi project wafer](/terminology/mpw).

On 30th June 2020, [Tim Ansell](https://twitter.com/mithro) announced the collaboration between Google and Skywater to provide a free shuttle service in his FOSSI dialup talk.

{{< youtube EczW2IWdnOM >}}

These [slides taken from his talk](https://docs.google.com/presentation/d/e/2PACX-1vRtwZPc8ykkkgtUkHkoJZrP9jKOo3FYdKqbg-So0ic6_kx7ha1vHnxrWmuxWkTc9GfC8xl0TfEpMLwK/pub?start=false&loop=false&delayms=3000#slide=id.g8a02ce4cad_0_238) show the overview:

![shuttle](/shuttle.png)

## Caravel

Normally in an MPW you would have the whole [die](/terminology/die) to yourself. In the Google/Skywater Shuttle all the designs will be within the user project area of the [Caravel harness](https://github.com/efabless/caravel). 
Caravel has its own RISCV processor and a neat [datasheet](https://caravel-harness.readthedocs.io/en/latest/?badge=latest). 
The idea here is to make it easier to bring up and debug your designs at the cost of some area.

![Caravel harness](/ciic_harness.png)

Read [this post to find out what you could fit in](/post/how-much-can-we-fit) the user space.

The Google shuttle will return chips in type of packaging called [Wafer Level Chip Scale Packaging](/terminology/wlcsp).

## Requirements

[Efabless have put up a page](https://efabless.com/open_shuttle_program) that has more details on the requirements for entry to the shuttle.
