---
title: "MPW6 submitted!"
tags: ["mpw", "course" ]
date: 2022-06-08T10:31:53+02:00
images: ["mpw6_multi_macro.png"]
image_pos: 0% 40%
featured_image: "mpw6_multi_macro.png"
---

We submitted for MPW6!

![MPW6 submission](/mpw6_multi_macro.png)

We had 4 submissions from the course, the [shared SRAM](https://docs.google.com/document/d/1wLjU6hkAoYvSWNBAyTj8HmIV70eJWU3apa9_OEpsd3Y/edit) infrastructure, and [I did some work on instrumenting Teo's hardware adders](/post/instrumenting-hardware-adders).

Congratulations to:

* Zorkan ERKAN
* Emre Hepsag
* Gregory Kielian
* Jason K. Eshraghian

for getting your first ASIC designs on the submission!

We also had some people from the course make personal applications for a whole chip:

* Shumpei Kawasaki - [MARMOT SOC](https://platform.efabless.com/projects/853)
* Maximo - [Hardware implementation of the Hack Computer from the Nand to Tetris courses](https://platform.efabless.com/projects/992),
* Proppy - [HSV Mixer](https://platform.efabless.com/projects/1081)

Here's the [github repo for the group submission](https://github.com/mattvenn/zero_to_asic_mpw6) and the [Efabless project](https://platform.efabless.com/projects/833).

## Building and testing the application

To see how I put the application together check the [multi_project_tools](https://github.com/mattvenn/multi_project_tools).

I finally got github actions working on both the main repository and the individual submission template.
The [main repo action](https://github.com/mattvenn/zero_to_asic_mpw6/actions/workflows/multi_tool.yaml) checks the following:

* all tests pass for all the projects
* caravel tests pass
* formal proof of the tristate bus - thanks to [YosysHQ formal verification tools](https://www.yosyshq.com/)
* builds the GDS and runs the precheck

The [submission template github action](https://github.com/mattvenn/wrapped_project_template/actions) checks all the tests are passing for that project. Tests include:

* functional RTL test
* caravel test pass
* project has tristate buffers and they work
* ports are correct for integration into the group submission
* GDS nothing above metal 5
* LVS matches gatelevel verilog to GDS
* documentation is present

# Project Index

And here's a list of the projects - congratulations everyone!

## Function generator

* Author: Matt Venn
* Github: https://github.com/mattvenn/wrapped_function_generator
* Description: arbitary function generator, using shared RAM as the output data

## CPR

* Author: Zorkan ERKAN
* Github: https://github.com/zorkan/cpr
* Description: Developed in accordance with the Aha Standard.

## instrumented adder - behavioural

* Author: Matt Venn & Teo
* Github: https://github.com/mattvenn/wrapped_instrumented_adder
* Description: adds a precise timer to optimised hardware adders to measure how fast they are

## instrumented adder - sklansky

* Author: Matt Venn & Teo
* Github: https://github.com/mattvenn/wrapped_instrumented_adder
* Description: adds a precise timer to optimised hardware adders to measure how fast they are

## instrumented adder - Brent Kung

* Author: Matt Venn & Teo
* Github: https://github.com/mattvenn/wrapped_instrumented_adder
* Description: adds a precise timer to optimised hardware adders to measure how fast they are

## instrumented adder - Ripple carry

* Author: Matt Venn & Teo
* Github: https://github.com/mattvenn/wrapped_instrumented_adder
* Description: adds a precise timer to optimised hardware adders to measure how fast they are

## instrumented adder - Kogge Stone

* Author: Matt Venn & Teo
* Github: https://github.com/mattvenn/wrapped_instrumented_adder
* Description: adds a precise timer to optimised hardware adders to measure how fast they are

## Wavelet Transform

* Author: Gregory Kielian
* Github: https://github.com/opensource-fr/wrapped_wavelet_transform
* Description: Implementation Wavelet Transform with 3 filter banks

## PrimitiveCalculator

* Author: Emre Hepsag
* Github: https://github.com/eemreeh/wrapped_PrimitiveCalculator
* Description: description

## snn-accelerator

* Author: Jason K. Eshraghian
* Github: https://github.com/jeshraghian/snn-accelerator
* Description: Lightweight Spiking Neural Network Accelerator in SKY130

