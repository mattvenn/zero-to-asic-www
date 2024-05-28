---
title: "VGA clock PCB updated for new chips"
date: 2023-12-30T16:26:18+02:00
images: ["vga_clock_pmod.jpg"]
featured_image: "vga_clock_pmod.jpg"
---

My [VGA clock](/post/vga_clock) design is the world's first certified [open source hardware down to the chip level](/post/vga_clock_pcb).

![vga clock](/vga_clock.jpg)

Unfortunately the [MPW1 chips](/post/mpw1_silicon/) were very hard to use and the new ones have a different pinout and footprint. I've been using the clock design as a test project for all the [Tiny Tapeout](https://tinytapeout.com/) chips past TT03. 

To test the new mux structure introduced at TT04, we ran an experimental [TT3.5](https://github.com/TinyTapeout/tinytapeout-03p5) chip. The chips are back and the clock works as expected (phew!)

As we have a hundred chips but no customers, I've decided to create a VGA PMOD that turns the dev board into a dedicated clock.

![VGA clock PMOD](/vga_clock_pmod.jpg)

More information and resources can be found here: https://bit.ly/vga-asic-clock.

The new PCB is here: https://github.com/tinytapeout/tt-vga-clock-pmod.

To buy a kit head to the [Tiny Tapeout store](https://store.tinytapeout.com/products/TT03p5-Development-Kit-VGA-PMOD-p655428056).

For every kit sold, I will donate $100 to [OSHWA](https://www.oshwa.org/).
