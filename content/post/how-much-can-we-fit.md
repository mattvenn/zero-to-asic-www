---
title: "How Much Can We Fit on an ASIC?"
date: 2020-11-13T20:00:11+01:00
featured_image: "/design-size.png"
---

The [Google / Skywater shuttle](/terminology/shuttle) reserves about 10 square mm (10 million square microns) of space for your design.

This comparison that Mohamed from [efabless](https://efabless.com/) put together shows the various areas (and time to generate the [GDS2](/terminology/gds2) files) of some popular designs.

![design size comparison](/design-size.png)

We could fit in about 10 picorv32 RISCV cores!

# My designs

I currently have 3 designs ready to add to the [multi project harness](/post/multi-project-harness):

| Name        | Square microns | How many would fit? |
| ----------- | -------------- | ------------------- |
| [seven segment seconds](https://github.com/mattvenn/seven-segment-seconds) | 10000 | 1000 |
| [vga clock](https://github.com/mattvenn/vga-clock)                         | 32400 | 300  |
| [ws2812 LED driver](https://github.com/mattvenn/ws2812-core)               | 72900 | 140  |

There is a lot of room for simple designs!

# Final ASIC application

You can see the [final application here](/post/asic_submitted), we fit in 8 designs with room for more.
