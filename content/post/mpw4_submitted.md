---
title: "MPW4 submitted!"
date: 2022-01-04T21:56:51+01:00
tags: ["mpw", "course" ]
images: ["mpw4_multi_macro.png"]
featured_image: "mpw4_multi_macro.png"
---

We submitted for MPW4! I was pretty pleased we managed to get so much in with such little time and for a tapeout date of New Year's Eve.

We had 9 submissions from the course, with 1 demo project from me and a new version of Maximo's hacksoc. Uri submitted 3 designs including
some custom standard cells in the shape of skulls!

![skullfet](/skullfet.jpg)

We also implemented the [shared SRAM](https://docs.google.com/document/d/1wLjU6hkAoYvSWNBAyTj8HmIV70eJWU3apa9_OEpsd3Y/edit), which means that
the group projects have access to a local fast memory (like a blockram on an FPGA).

Here's the [github repo for the group submission](https://github.com/mattvenn/zero_to_asic_mpw4) and the [Efabless project](https://platform.efabless.com/projects/596).

It was my first time submitting 2 applications for the shuttle as I also did a rerun of [MPW2](/post/mpw2-submitted) to fix clock issues.

![MPW4 submission](/mpw4_multi_macro.png)

To see how I put the application together check the [multi_project_tools](https://github.com/mattvenn/multi_project_tools).

And here's a list of the projects - congratulations everyone!

## Function generator

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_function_generator
* commit: 0d95d94d816685ab9eea70fbbfb2425a8b91c27e
* Description: arbitary function generator, using shared RAM as the output data

## SPELL

* Author: Uri Shaked
* Github: https://github.com/wokwi/wrapped_spell
* commit: 4db5165ac2e450a62a249285c1a7374a836b5167
* Description: SPELL CPU (https://skullctf.com/spell)

## PPM Coder

* Author: Llorens_MRC
* Github: https://github.com/mattvenn/wrapped_ppm_coder
* commit: bbcb465d5d149a501b1cc67cfe4b344383a15a7e
* Description: Fuentes Codificador PPM configurable

## PPM Decoder

* Author: jospicant
* Github: https://github.com/mattvenn/wrapped_ppm_decoder
* commit: 8d21fed5cbce7c04cdc739226e6ea9167774f7c7
* Description: Fuentes Codificador PPM configurable

## SiLife

* Author: Uri Shaked
* Github: https://github.com/wokwi/wrapped_silife
* commit: 28c2fc901365444c992c94660594b946216ad1ec
* Description: Game of Life, in Silicon

## SkullFET

* Author: Uri Shaked
* Github: https://github.com/wokwi/wrapped_skullfet
* commit: c583f431e0b6f280f91520725f313aebbab86fdd
* Description: Barebone MOSFET transistors

## SPRAID

* Author: Dylan Wadler
* Github: https://github.com/bit0fun/spraid_mpw4
* commit: 69aa8a41cdbf87ca65c8793ba47a924204e8cb88
* Description: SPI RAID Controller

## ASIC watch

* Author: Guillem Cabo & Ledoux Louis
* Github: https://github.com/Bynaryman/wrapped_asic_watch
* commit: d19b10006c3247f6a11fd3e14d854422d85ab37d
* Description: a 7 segment fashion watch targeting asic and sky130 process node

## Hack soc

* Author: Maximo Balestrini
* Github: https://github.com/mbalestrini/wrapped_hack_soc
* commit: 048ca9374c0a7984064827bf1d547191a7e5b50d
* Description: Hardware implementation of the Hack Computer from the Nand to Tetris courses
