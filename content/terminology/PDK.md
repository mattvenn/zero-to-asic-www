---
title: "PDK"
date: 2020-11-12T17:38:48+01:00
description: "A Process Design Kit (PDK) is a collection of files from a chip foundry that defines the fabrication rules, device models, and standard cells needed to design an ASIC for that process."
images: ["stackup.png"]
featured_image: "stackup.png"
faq:
  - q: "What is a PDK?"
    a: "A PDK (Process Design Kit) is a library of files provided by a chip foundry that describes their specific fabrication process. It includes design rules, device models, standard cell libraries, SPICE models for simulation, and verification rule decks — everything a designer needs to create a chip that can be manufactured at that foundry."
  - q: "What does a PDK contain?"
    a: "A PDK typically contains: DRC (Design Rule Check) rules, LVS (Layout vs Schematic) rules, SPICE models for analog simulation, standard cell libraries with timing models, IO pad libraries, parameterized cells (pcells), and layer stack definitions."
  - q: "What PDK is used for open source ASIC design?"
    a: "The most widely used open source PDK is the SkyWater sky130 PDK, which describes SkyWater Technology's 130nm process node. It is freely available and is the PDK used by the Zero to ASIC Course and open source shuttle programs like Tiny Tapeout. More recently IHP130 and GF180 have been published and are now available at Tiny Tapeout."
---

The Process Design Kit is a library of all the specifications that describe a particular factories' particular chip fabrication process. This often includes representations of the design rules and devices which can be used by particular implementation and verification tools that have been checked and approved by the fab. This may include software representations of items such as transistors which will be automatically laid out with the dimensions that meet the rules for the process (often called pcells for 'parameterized cells' - the designer says what size is wanted, the pcell does the rest).

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

This allows us to model analog and digital components, for example different sizes of [MOSFET](/terminology/mosfet).

# Support IP

* Input Output libraries

# Analog design

* [Spice](/terminology/spice) models

# Digital design

* [Standard cells](/terminology/standardcell)
* Timing models - allow us to know how fast we can run our designs
