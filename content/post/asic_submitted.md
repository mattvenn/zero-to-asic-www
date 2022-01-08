---
title: "My first ASIC - MPW1 submitted"
date: 2020-12-23T18:07:33+01:00
images: ["caravel-numbered.png"]
featured_image: "caravel-numbered.png"
tags: ["mpw"]
---

Wow! What a journey. I'm very happy to announce our submission is in and accepted. Now we have a long wait to see if it works!

Here's a picture of the final design. The outer edge and the block at the bottom are all part of [Caravel](/terminology/shuttle#caravel), the standard chip format that everyone on the shuttle has to use.  It includes a RISCV processor, RAM, UART, a wishbone bus and more.

The cross hatching between all the project [macros](/terminology/macro) (yellow blocks) is the power distribution network. It's a fine grid of the 4 power supplies. As they pass over macro, a via connects the power lines of the macro to the power distribution network.

![ASIC](/caravel-numbered.png)

## 1 seven-segment-seconds

* shows seconds on a seven segment LED display.
* author: Matt Venn
* https://github.com/mattvenn/seven-segment-seconds

## 2 mm2hdmi

* HDMI driver
* author: Aleksandar Pajkanovic
* https://github.com/nanoluka/mm2hdmi.git

## 3 asicfreq

* Frequency counter
* author: Michael Betz & Vamsi Vytla
* https://git.sr.ht/~jersey99/asicfreq

## 4 TPM2137

* Reverse Engineering challenge
* author: Q3K
* https://github.com/mattvenn/TPM2137

## 5 ws2812

* ws2812 LED interface for 8 addressable LEDs
* author: Matt Venn
* https://github.com/mattvenn/ws2812-core.git

## 6 spinet

* multi node computer controller
* author: Richard Miller
* https://github.com/millerresearch/spinet

## 7 ASIC_watch

* 4 digit 7 segment clock
* authors: Louis Ledoux & Guillem Cabo
* https://github.com/GuillemCabo/ASIC_watch.git

## 8 vga-clock

* show the time on a VGA panel
* author: Matt Venn
* url: https://github.com/mattvenn/vga-clock.git

## 9 multi project harness

* The multiplexer that connects each project in turn to the inputs and outputs. 
* author: Matt Venn
* https://github.com/mattvenn/multi-project-harness/tree/separate-macro

# OpenLane configuration

The configuration for each of the above [project macros is here](https://github.com/mattvenn/multi-project-harness/tree/separate-macro/openlane/macroconfig).

For the details on joining them all together and placing on the Caravel harness, you can check the [application repository here](https://github.com/mattvenn/caravel-mph). 
The configuration is on a different branch [here](https://github.com/mattvenn/caravel-mph/tree/release/openlane/user_project_wrapper).

It all got a bit messy at the end because there was a last minute change of the Caravel harness. This meant that I had to use one branch (release) for building the user project area, and then another branch (release-mpw-one-b) for building the final GDS files for submission.

# Stuff that didn't get done

Unfortunately I didn't manage to get any [artwork](/post/gds-artwork) placed. There wasn't a good way to integrate it with the tools, so it would have meant manually altering the power distribution network to remove wires, and then manually place the artwork blocks. I just didn't feel confident enough to do it without wrecking something - and I was really tired! So hopefully next time I will have worked it out.

