---
title: "My analog microelectronics journey"
tags: ["course", "analog"]
images: ["analog_journey.png"]
featured_image: "analog_journey.png"
date: 2024-09-09T13:49:56+02:00
---

This article will give you some insight into my journey into the world of analog microelectronics, as told in my recent talk at [ORConf 2024](https://fossi-foundation.org/orconf/2024).

Back in 2020, inspired by Tim Ansell's announcement of free tapeouts, [I jumped headfirst into the world of open-source ASIC design](https://www.mattvenn.net/stem/zero-to-asic-course/). My first chip was a digitally focused project, reflecting my background in FPGA programming. It was amazing to see the power of digital abstraction—designing with ones and zeros, instantiating tons of transistors with a single line of code—but it also made me appreciate the incredible complexity hidden beneath the surface.

{{< youtube DoFL6PPlErw >}}

This led me to my analog journey. I started with the seemingly simple task of hand-drawing an inverter in Magic. It was a humbling experience, taking days to get a DRC-clean layout and even longer to simulate it. This highlighted the need for more accessible analog design tools, prompting me to collaborate with Uri Shaked to create [SiliWiz](https://siliwiz.com).

As I dug deeper into analog, I realised that [Tiny Tapeout](https://tinytapeout.com), which had been solely focused on digital designs, needed to evolve. The release of Tiny Tapeout 6 marked a turning point, [introducing support for analog and mixed-signal ASICs](/post/tinytapeout_goes_analog). This required a significant infrastructure overhaul, including the implementation of power gating for every design to ensure safety and reliability.

Along the way, I challenged myself to design and tape out various analog circuits, including an [R2R DAC](https://tinytapeout.com/runs/tt06/tt_um_mattvenn_r2r_dac), a [relaxation oscillator](https://tinytapeout.com/runs/tt06/tt_um_mattvenn_relax_osc), and a [voltage reference](https://tinytapeout.com/runs/tt07/tt_um_mos_bandgap). Each project was a learning experience, highlighting the iterative nature of analog design and the importance of thorough simulation and characterization.

I'm excited to see what the future holds for open-source analog and mixed-signal ASIC design. I believe this is where the open-source community can truly shine, creating unique and innovative circuits that push the boundaries of what's possible. I’m particularly interested in exploring radio applications and hope to start trying some radio experiments soon.

If you're interested to start your own journey, I've just released the [Zero to ASIC analog course](/analog).
