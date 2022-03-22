---
title: "MPW5 submitted!"
date: 2022-03-22T17:28:58+01:00
tags: ["mpw", "course" ]
images: ["mpw5_multi_macro.png"]
image_pos: 0% 20%
featured_image: "mpw5_multi_macro.png"
---

We submitted for MPW5!

![MPW5 submission](/mpw5_multi_macro.png)

We had 8 submissions from the course, the [shared SRAM](https://docs.google.com/document/d/1wLjU6hkAoYvSWNBAyTj8HmIV70eJWU3apa9_OEpsd3Y/edit) infrastructure, and I updated my demo designs.

We also had some people from the course make personal applications for a whole chip:

* Steve & Zhenle - [PSRAM (HyperRAM) interface with an ACORN PRNG](https://platform.efabless.com/projects/708),
* Q3K - [simple, microcontroller-style SoC based around a Lanai core](https://platform.efabless.com/projects/760),
* Maximo - [Hardware implementation of the Hack Computer from the Nand to Tetris courses](https://platform.efabless.com/projects/791),
* Zbigniew - [A rendering circuit for three blobs and a playable tetris clone](https://platform.efabless.com/projects/810).

And thanks to Paweł for updating the shared SRAM blocks.

Following Maximo's work on cool GDS renderings, [Proppy has made a few of his hsv2rgb](https://twitter.com/proppy/status/1506085187561848835) converter project:

![render of Proppys design](/mpw5/proppy-render.png)

Here's the [github repo for the group submission](https://github.com/mattvenn/zero_to_asic_mpw5) and the [Efabless project](https://platform.efabless.com/projects/680).

To see how I put the application together check the [multi_project_tools](https://github.com/mattvenn/multi_project_tools).

And here's a list of the projects - congratulations everyone!

# Project Index

## Function generator

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_function_generator
* commit: 9e73784d43a91d70cb1a7c9c5d42037f49ed9e67
* Description: arbitary function generator, using shared RAM as the output data

![Function generator](/mpw5/function_generator.png)

## VGA Clock

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_vga_clock
* commit: 6c7f12b8be62d34d4f4221e18b9408b3c5ac8fcd
* Description: shows the time on a 640x480 panel

![VGA Clock](/mpw5/vga_clock.jpg)

## Frequency counter

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_frequency_counter
* commit: 94cd6e626492dc2f623bf06163e90a84bde553cb
* Description: Counts pulses on input and displays frequency on 2  seven segment displays

![Frequency counter](/mpw5/frequency_counter.png)

## RGB Mixer

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_rgb_mixer
* commit: 2676a8904591e92613fbfadf8c7f57fdfd79b1a4
* Description: reads 3 encoders and generates PWM signals to drive an RGB LED

![RGB Mixer](/mpw5/schematic.jpg)

## Hack soc

* Author: Maximo Balestrini
* Github: https://github.com/mbalestrini/wrapped_hack_soc
* commit: 54395c53d52f253bd71b35d0a1c2049c87d31103
* Description: Hardware implementation of the Hack Computer from the Nand to Tetris courses

![Hack soc](/mpw5/project.jpg)

## teras

* Author: Louis Ledoux AKA Binaryman
* Github: https://github.com/Bynaryman/wrapped_teras
* commit: c119cb48d76e8a4a62c80f98323efb114553c417
* Description: matrix multiply unit with exact accumulators, no intermediate roundings, fused-dot-products, and posit arithmetic

![teras](/mpw5/teras_4x3.png)

## ALU74181

* Author: Thorsten Knoll
* Github: https://github.com/ThorKn/wrapped_alu74181
* commit: 6e935d2d32acdcc66ab18c5894cb628b6c6b9048
* Description: Rebuild of the 4-bit Arithmetic Logic Unit 74181

![ALU74181](/mpw5/alu74181_gds.png)

## vga demo

* Author: Zbigniew Drozd
* Github: https://github.com/zbigos/wrapped-vgademo-on-fpga
* commit: 7fb9353f1a9f5120a0bd7907963a1c65919f33c0
* Description: quick demo displaying three floating blobs

![vga demo](/mpw5/screen.png)

## SiLife

* Author: Uri Shaked
* Github: https://github.com/wokwi/wrapped_silife
* commit: 53c45898bd6fc04530bf6e9d17153418db5dd175
* Description: Game of Life, in Silicon

![SiLife](/mpw5/silife.png)

## wrapped_acorn_prng

* Author: Zhenle Cao
* Github: https://github.com/ZhenleC/wrapped_acorn_prng
* commit: 5f7d3e5d0fcc9ffc3845dd7e97f55219ebd112ec
* Description: ACORN (Additive Congruential Random Number) generator, a pseudo random number generator made for the ZerotoASIC course to be taped out on SkyWater Open Source PDK SKY130 process. Design inspired from: http://acorn.wikramaratna.org/ . Huge shoutout and appreciation to Steven Goldsmith for his invaluable assistance with Caravel. 

![wrapped_acorn_prng](/mpw5/acorn_prng.png)

## HSV Mixer

* Author: @proppy (forked from Matt Venn)
* Github: https://github.com/proppy/wrapped_hsv_mixer
* commit: 05ab3cfb40c1d934dceb3fe46740a491d4660f6f
* Description: reads HSV values from 3 encoders, convert to them RGB, and generates PWM signals to drive an RGB LED

![HSV Mixer](/mpw5/hsv2rgb.jpg)

## SkullFET

* Author: Uri Shaked
* Github: https://github.com/wokwi/wrapped_skullfet
* commit: 927e7275e6ba42f02fec99f5928941eeb985ee29
* Description: Barebone MOSFET transistors

![SkullFET](/mpw5/skullfet_inverter.png)

