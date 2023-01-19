---
title: "PDK"
date: 2020-11-12T17:38:48+01:00
description: "Process Design Kit"
images: ["stackup.png"]
featured_image: "stackup.png"
---

The Process Design Kit is a library of all the specifications that describe a particular factories' particular chip fabrication process. This often includes representations of the design rules and devices which can be used by particular implementation and verification tools that have been checked and approved by the fab. This may include software representations of items such as transistors which will be automatically layed out with the dimensions that meet the rules for the process (often called pcells for 'parameterized cells' - the designed says what size is wanted, the pcell does the rest).

In our case we have access to the Skywater factories 130 nanometer [process](/terminology/node), usually called sky130. 

Tim Edwards:

> Note that this process is advertised as a "hybrid 180nm / 130nm".  
A number of aspects are either very close to a 180nm process or somewhere between 180 and 130.  
The typical minimum length low-voltage transistor is 150nm. 

For more information about process sizes see this about the [node](/terminology/node).

This picture shows how the layers of the chip stack up to form the complete ASIC.

![stackup](/stackup.png)

This table shows all the layers defined in the PDK that can be used in a design tool like [Magic](/terminology/magic).

![layers](/sky130-layers.png)

For the raw data, check the [mask definitions](https://skywater-pdk.readthedocs.io/en/main/rules/masks.html)

You can get all the information here: https://skywater-pdk.readthedocs.io/en/main

The following is adapted from one of Tim Ansell's [slides](https://docs.google.com/presentation/d/e/2PACX-1vRtwZPc8ykkkgtUkHkoJZrP9jKOo3FYdKqbg-So0ic6_kx7ha1vHnxrWmuxWkTc9GfC8xl0TfEpMLwK/pub?start=false&loop=false&delayms=3000#slide=id.g8a122ff1a1_6_2113) in his [Fossi presentation](https://www.youtube.com/watch?v=EczW2IWdnOM&list=PLUg3wIOWD8yoZCg9XpFSgEgljx6MSdm9L)

# Design Rules

* [DRC](/terminology/drc)
* [LVS](/terminology/lvs)

# Behavioural models

This allows us to model analogue and digital components, for example different sizes of [MOSFET](/terminology/mosfet).

# Support IP

* Input Output libraries

# Analogue design

* [Spice](/terminology/spice) models

# Digital design

* [Standard cells](/terminology/standardcell)
* Timing models - allow us to know how fast we can run our designs


