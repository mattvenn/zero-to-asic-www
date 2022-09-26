---
title: "Standard cell"
date: 2020-11-12T17:38:45+01:00
images: ["std-cell-inverter.png"]
featured_image: "std-cell-inverter.png"
---

One of the many things a [PDK](/terminology/pdk) contains is the standard cell library.
This is a collection of all the analogue and digital building blocks used to build an IC like AND, OR, NOT gates, flip flops, IO pads and so on.

# Crafting Standard cells with James Stine

For lots of interesting questions and answers about making open source standard cell libraries, this interview with James Stine is really good.

{{< youtube 5J8LJoUxCHk >}}

# Reverse engineering a MUX

If you want to know how these cells are put together, check this video out of me extracting the circuit from a MUX.

{{< youtube NjctnVUxZIk >}}

# SkyWater130 examples

Here are some examples taken from the high density SkyWater 130nm standard cell library.

You can browse them all [here](https://antmicro-skywater-pdk-docs.readthedocs.io/en/test-submodules-in-rtd/contents/libraries/sky130_fd_sc_hd/README.html)

## Inverter

![inverter](/std-cell-inverter.png)

## XOR

![inverter](/std-cell-xor2.png)

## D type Flip Flop

![inverter](/std-cell-dflop.png)

# How a flip flop works

And for a complicated standard cell, see this video about how flip flops work, focussing on the sky130 D type.

{{< youtube 5PRuPVIjEcs >}}
