---
title: "Maskset"
date: 2020-11-12T17:42:33+01:00
images: ["photomask.jpg"]
featured_image: "photomask.jpg"
description: A mask set is the complete collection of photomasks used in chip fabrication — one per layer — where each opaque plate with transparent patterns is used in a photolithographic step to build up the IC.
faq:
  - q: What is a photomask and what is a mask set?
    a: A photomask is an opaque plate with holes or transparencies that allow light to shine through in a defined pattern. Several masks are used in turn during chip fabrication, each reproducing one layer of the design, and together they are called a mask set.
  - q: How is a photomask physically made?
    a: Masks are made from fused quartz with a chrome pattern deposited on the surface and then removed using lasers or ion beams. The pattern on the mask is typically 4 times larger than the image projected onto the wafer, so that the optical reduction makes the mask cheaper and dust less significant.
  - q: How many masks are needed for the Skywater PDK?
    a: The Skywater PDK has 33 different layers, so 33 different masks are needed. The masks must be extremely precisely made, which is why the whole set is so expensive.
---

From [Wikipedia](https://en.wikipedia.org/wiki/Photomask):

> A photomask is an opaque plate with holes or transparencies that allow light to shine through in a defined pattern. They are commonly used in photolithography and the production of integrated circuits (ICs or "chips") in particular. Masks are used to produce a pattern on a substrate, normally a thin slice of silicon known as a [wafer](/terminology/wafer) in the case of chip manufacturing. Several masks are used in turn, each one reproducing a layer of the completed design, and together they are known as a mask set. 

![mask](/photomask.jpg)

This mask shows 20 copies of the same design, so a single exposure (in the stepper) will create the pattern for 20 chips. The mask is made from fused quartz (instead of glass) and the pattern is made by depositing chrome evenly on the surface of the quartz and removing it using lasers or ion beams. The pattern on the mask is typically 5 times larger than the image projected onto the wafer, this optical reduction allows the mask to be cheaper to produce and makes dust on the mask less significant (because its shadow will also be shrunk by a factor of 5. The whole maximum exposed area on the wafer on a given step is typically 25mm across, the pattern on the mask is thus 125mm across. 

In the case of the [Skywater PDK](/terminology/pdk), we have 33 different layers and so 33 different masks are needed. The masks have to be extremely precisely made, which is why the whole set of masks ends up being so expensive. You can see a list of all the layers and what they are used for on this [spreadsheet](https://docs.google.com/spreadsheets/d/1y6cjte_stJ96g2f_fNWIj1oU6yipX5GKY3nb_1dL-XE/edit#gid=0).

For experimentation, a [Multi Project Wafer](/terminology/mpw) is often used to lower the costs.

The process of using the masks to create the patterns on the [silicon wafer](/terminology/wafer) is called [photolithography](/terminology/photolithography).
