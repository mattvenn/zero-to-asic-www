---
title: "Standard cell"
date: 2020-11-12T17:38:45+01:00
images: ["std-cell-inverter.png"]
featured_image: "std-cell-inverter.png"
---

One of the many things a [PDK](/terminology/pdk) contains is the standard cell library.
This is a collection of all digital building blocks used to build an IC like AND, OR, NOT gates, flip-flops, etc. There will be other libraries for specialised functions such as IO pads, and any analogue blocks or memory macros, and so on.

Standard cell libraries are a set of cells that have common characteristics and physical layout. The most obvious element is that the cells have a common height. Because the cells will be placed side by side with abutting edges, all items that cross these edges need to be at fixed positions and have fixed sizes. These items typically include the power and ground rails and the wells. 
In addition the cells, because they touch, they need to be DRC legal in all combinations. This means that items that do not cross the boundary need to be moved away from it by at least half the minimum spacing rule for that layer.
Because the wells are in common positions, this implies that the P and N transistor sizes will be similar in all cells - and indeed the sizes of these are one of the terms that help define what the standard cell height is. This in turn leads to the logic thresholds for the cells being similar - indeed this is a requirement for STA to work correctly ie that all cells think that the point a 1 becomes a 0 are similar.
Another item that is considered in setting the cell height is the number of wiring pitches across them that are available, both on the layers used in the cells and on those above. It helps for the cells to be an integer multiple of the dominant wiring pitches high, so that we don't waste space.

# Crafting Standard cells with James Stine

For lots of interesting questions and answers about making open source standard cell libraries, this interview with James Stine is really good.

{{< youtube 5J8LJoUxCHk >}}

# Reverse engineering a MUX

If you want to know how these cells are put together, check this video out of me extracting the circuit from a MUX.

{{< youtube NjctnVUxZIk >}}

# SkyWater130 examples

Here are some examples taken from the high density SkyWater 130nm standard cell library.

You can browse them all [here](https://skywater-pdk.readthedocs.io/en/main/index.html)

## Inverter

[Inverter](https://skywater-pdk.readthedocs.io/en/main/contents/libraries/sky130_fd_sc_hd/cells/inv)
![inverter](/std-cell-inverter.png)

## XOR

[XOR](https://skywater-pdk.readthedocs.io/en/main/contents/libraries/sky130_fd_sc_hd/cells/xor2)

![xor](/std-cell-xor2.png)

## D type Flip Flop

[D flop](https://skywater-pdk.readthedocs.io/en/main/contents/libraries/sky130_fd_sc_hd/cells/dfxtp/README.html)

![d flop](/std-cell-dflop.png)

# How a flip flop works

And for a complicated standard cell, see this video about how flip flops work, focussing on the sky130 D type.

{{< youtube 5PRuPVIjEcs >}}
