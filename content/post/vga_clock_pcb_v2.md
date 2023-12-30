---
title: "VGA clock PCB updated for new chips"
date: 2023-12-30T16:26:18+02:00
images: ["vga_clock_pcbv2_render.png"]
featured_image: "vga_clock_pcbv2_render.png"
---

I've just updated the VGA clock PCB to take advantage of a batch of new chips.

I think my [VGA clock](/post/vga_clock) design might be the world's first certified [open source hardware down to the chip level](/post/vga_clock_pcb).

![vga clock](/vga_clock.jpg)

Unfortunately the [MPW1 chips](/post/mpw1_silicon/) were very hard to use and the new ones have a different pinout and footprint. I've been using the clock design as a test project for all the [Tiny Tapeout](https://tinytapeout.com/) chips past TT03. To test the new mux structure introduced at TT04, we ran an experimental [TT3.5](https://github.com/TinyTapeout/tinytapeout-03p5) chip. The chips are back and the clock works as expected (phew!)

As we have a hundred chips but no customers, I've decided re-spin the board and finally fulfill my plan to sell a few and donate the proceeds to [OSHWA](https://www.oshwa.org/).

![3d render of the clock pcb](/vga_clock_pcbv2_render.png)

The new board's repo is here: https://github.com/mattvenn/tt-vga-clock-pcb

Until the docs are updated the [OSHWA certification](https://certification.oshwa.org/es000023.html) refers to the previous version.

If you're interested to know when the boards go on sale, [leave your email on this form](https://docs.google.com/forms/d/1T6BmjGyFQyqTNji1qao1T61LZW5fL_B2eHlydXzalR4/edit).
