---
title: "MPW2 Submitted"
date: 2021-06-24T16:51:19+02:00
featured_image: "multi_macro.png"
image_pos: 0px -580px
---

We did it! 14 people from the course got their designs into the group submission, and the project was accepted for fabrication. Silicon here we come!

![MPW2 submission](/multi_macro.png)

You can get all the details on all the projects from the
[Efabless submission](https://efabless.com/projects/66)

This time around it was a lot easier than [MPW1](/post/asic_submitted). 
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

Routing all the macros takes about 15 minutes, and running all the tests of all the designs takes about 60 minutes.

It wasn't all smooth sailing, we had a few last minute changes including adding IRQs, a new user clock, and dealing with unwanted buffered outputs.

I put together a video to describe the process:

{{< youtube DdKgbq5KGqw >}}

# Awesome blender renders!

Course participant Maximo put together some lovely images here by converting the GDS to STL and then rendering inside blender.

{{< tweet 1408126991459553284 >}}
