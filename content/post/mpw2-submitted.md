---
title: "MPW2 Submitted"
date: 2021-06-24T16:51:19+02:00
images: ["multi_macro.png"]
featured_image: "multi_macro.png"
tags: ["mpw", "course"]
image_pos: 0% 20%
---

We did it! 14 people from the course got their designs into the group submission, and the project was accepted for fabrication. Silicon here we come!

![MPW2 submission](/multi_macro.png)

You can get all the details on all the projects submitted to MPW2 [here](https://platform.efabless.com/projects/shuttle_name/MPW-2).

And see how I put the application together [here](#multi-project-tools), with the [repo here](https://github.com/mattvenn/caravel_user_project).

# Project listing

## RGB Mixer

* Author: Matt Venn
* Github: [https://github.com/mattvenn/wrapped_rgb_mixer/tree/caravel-mpw-two-c](https://github.com/mattvenn/wrapped_rgb_mixer/tree/caravel-mpw-two-c)
* Description: reads 3 encoders and generates PWM signals to drive an RGB LED

## Frequency counter

* Author: Matt Venn
* Github: [https://github.com/mattvenn/wrapped_frequency_counter/tree/caravel-mpw-two-c](https://github.com/mattvenn/wrapped_frequency_counter/tree/caravel-mpw-two-c)
* Description: Counts pulses on input and displays frequency on 2  seven segment displays

## A5/1 Wishbone

* Author: Jamie Iles
* Github: [https://github.com/jamieiles/a5-1-wb-macro](https://github.com/jamieiles/a5-1-wb-macro)
* Description: A5/1 cryto block connected via wishbone to PicoRV32

## Fibonacci

* Author: Konrad Rzeszutek Wilk
* Github: [https://github.com/konradwilk/fibonacci](https://github.com/konradwilk/fibonacci)
* Description: Fibonacci emitter connected to [37:8] and controlled via wishbone

## Quad PWM FET Drivers

* Author: Chris DePalm
* Github: [https://github.com/ChrisDePalm/wrapped_quad_pwm_fet_drivers.git](https://github.com/ChrisDePalm/wrapped_quad_pwm_fet_drivers.git)
* Description: 4 PWM FET Drivers for Power Applications

## memLCDdriver

* Author: Matt Beach
* Github: [https://github.com/matt-beach/wrapped_memLCDdriver.git](https://github.com/matt-beach/wrapped_memLCDdriver.git)
* Description: SPI to 64-color memory LCD interface

## QARMA-64 Accelerator

* Author: Viktor H. Brange
* Github: [https://github.com/vbrange/verilog_qarma](https://github.com/vbrange/verilog_qarma)
* Description: Implementation of QARMA 64

## ChaCha20 Accelerator

* Author: Richard Petri
* Github: [https://github.com/rpls/wrapped_chacha_wb_accel](https://github.com/rpls/wrapped_chacha_wb_accel)
* Description: A minimal Wishbone connected ChaCha20 accelerator

## Framebufferless Video Core

* Author: Tom Gwozdz
* Github: [https://github.com/tomgwozdz/fbless-graphics-core](https://github.com/tomgwozdz/fbless-graphics-core)
* Description: A framebufferless VGA video generator, under CPU control

## Pong

* Author: Erik van Zijst
* Github: [https://github.com/erikvanzijst/wrapped_pong.git](https://github.com/erikvanzijst/wrapped_pong.git)
* Description: A hardware implementation of Pong

## Hack soc

* Author: Maximo Balestrini
* Github: [https://github.com/mbalestrini/wrapped_hack_soc](https://github.com/mbalestrini/wrapped_hack_soc)
* Description: Hardware implementation of the Hack Computer from the Nand to Tetris courses

## gfxdemo

* Author: Konrad Beckmann
* Github: [https://github.com/kbeckmann/wrapped_gfxdemo](https://github.com/kbeckmann/wrapped_gfxdemo)
* Description: gfxdemo

## Wishbone HyperRAM

* Author: Pawel Sitarz
* Github: [https://github.com/embelon/wrapped_wb_hyperram](https://github.com/embelon/wrapped_wb_hyperram)
* Description: Simple HyperRAM driver accesible on Wishbone bus

## Newmot SoC

* Author: Charles-Henri Mousset
* Github: [https://github.com/chmousset/caravel_multi_newmot](https://github.com/chmousset/caravel_multi_newmot)
* Description: Simple SoC dmonstrating a Stepper Motor step/dir generator, and litex wishbone / uart / pwm

## hoggephase

* Author: David Hulton
* Github: [https://github.com/h1kari/wrapped_hoggephase_project](https://github.com/h1kari/wrapped_hoggephase_project)
* Description: Hogge Phase EMFI/BBI Glitch Detector

## bfloat16_fma

* Author: Author
* Github: [https://github.com/etalian/mensa](https://github.com/etalian/mensa)
* Description: dual bfloat16 fused multiply-add

# Multi project tools

This time around submission was a lot easier and nerve-wracking than [MPW1](/post/asic_submitted). 

Part of that was because I have the whole procedure pretty much automated with the [multi project tools](https://github.com/mattvenn/multi_project_tools).

These tools can run a set of tests including:

* LVS
* GDS size and layers
* Outputs Z when not selected
* Formal connectivity check
* Module tests
* Caravel context tests
* Module interface is correct
* Documentation is available

Then I can run a single command to copy all the GDS, LEF and generate the config file for OpenLANE.

    ./multi_tool.py --create-openlane-config --copy-gds  --force-delete

Routing all the macros takes about 15 minutes, and running all the tests of all the designs takes about 60 minutes.

It wasn't all smooth sailing, we had a few last minute changes including adding IRQs, a new user clock, and dealing with unwanted buffered outputs.

I put together a video to describe the process:

{{< youtube DdKgbq5KGqw >}}

# Awesome blender renders!

Course participant Maximo put together some lovely images here by converting the GDS to STL and then rendering inside blender.

{{< tweet user="maxiborga" id="1408126991459553284" >}}

{{< tweet user="maxiborga" id="1412801867302805504" >}}
