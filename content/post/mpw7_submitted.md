---
title: "MPW7 submitted!"
date: 2022-09-14T08:00:00+01:00
tags: ["mpw", "course" ]
images: ["mpw7_multi_macro.png"]
featured_image: "mpw7_multi_macro.png"
---

We submitted for MPW7! I am particularly excited about this submission because we were able to submit the Zero to ASIC course designs as well as the first [Tiny Tapeout](https://mailchi.mp/574276e3c9d7/tinytapeout) design. 

MPW7 has by far had the most submissions of the MPW shuttles so far with 72 submitted projects as of 13 September.

Congratulations to everyone on the course submission! We had 9 projects from the course, with 1 demo arbitrary function generator from me, a 32-bit RISC-V based processor by Farhad, an in silicon version of [Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) from Uri and a [Spiking Neural Network](https://en.wikipedia.org/wiki/Spiking_neural_network) (SNN) accelerator by Peng Zhou. We also implemented 1kByte of RAM with open-source [OpenRAM](https://openram.org/).
     
     
![MPW7 submission](/mpw7_multi_macro.png)

Here's the [github repo for the group submission](https://github.com/mattvenn/zero_to_asic_mpw7) and the [Efabless project](https://platform.efabless.com/projects/1180).

Curious about Tiny Tapeout? Check out the [github repo](https://github.com/mattvenn/tinytapeout-mpw7) and the [Efabless project](https://platform.efabless.com/projects/1229).

And here's a list of the projects - congratulations again everyone!

## Function generator

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_function_generator
* commit: 701095fd880ad3bb80d6cec1d214a04e5676a65d
* Description: arbitary function generator, using shared RAM as the output data

## ibnalhaytham

* Author: Farhad Modaresi
* Github: https://github.com/sfmth/wrapped_ibnalhaytham
* commit: 0627452464db56b813a3aae8899e8339a358fac9
* Description: 32-bit RISC-V based processor

## Educational tpu
* Author: Camilo Soto
* Github: https://github.com/tucanae47/wrapped_etpu
* commit: d25b41070e74c47a00c1f264af068523c52c584a
* Description: 3x3 systolic array over wishbone bus

## SiLife
* Author: Uri Shaked
* Github: https://github.com/wokwi/wrapped_silife
* commit: aec0f0f7ad458675d961a8289d16064bf15964f6
* Description: Game of Life, in Silicon

## snn-asic
* Author: Peng Zhou
* Github: https://github.com/pengzhouzp/wrapped_snn_network
* commit: d0f3a80e664bf6327274c5fef0ace2af40db311b
* Description: asic snn accelerator with adaptive threshold neurons and recurrent connective synapses

## wrapped mbs fsk
* Author: James Rosenthal
* Github: https://github.com/jdrosent/wrapped_mbsFSK
* commit: ac3713d3220f225a6de8481bd3b72e245614e064
* Description: baseband signal engine for a backscatter uplink

