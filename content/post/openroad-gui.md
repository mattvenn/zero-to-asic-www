---
title: "OpenROAD GUI"
date: 2023-04-26T11:55:07+02:00
tags: ["videos","tools"]
images: ["clocktree.png"]
featured_image: "clocktree.png"
---

The OpenROAD GUI is a great way to explore your ASIC design. You can:

* View various types of heatmaps, including
    * Placement density 
    * Power density 
    * Routing congestion 
    * IR drop
* Trace nets,
* View the clock tree,
* Inspect timing and more.

I recently spoke with Matt Liberty, and OpenROAD maintainer, and he showed me how to inspect a simple design.

{{< youtube NuFJLy9ywVg >}}

## OpenLane

If you're using OpenLane to harden your ASIC designs, and you want to use the GUI, you might [hit a segfault](https://github.com/The-OpenROAD-Project/OpenLane/issues/1772). If so, you'll need to modify the OpenLane top level Makefile.

Find the line that starts with `DOCKER_OPTIONS` and on the next line, add this:

    DOCKER_OPTIONS += --privileged

Then here are the instructions to first harden a design, and then inspect it:

    # mount the docker image
    make mount                              

    # harden the spm example, and tag it 'gui'
    ./flow.tcl -design spm -tag gui         

    # start the OpenROAD GUI on the spm design tagged 'gui'
    ./flow.tcl -design spm -tag gui -gui    
    
If you don't tag the design as your harden it, it will be given an automatic tag based on the time and date. Then you'll need to 
provide that tag when you start the GUI.

If you want to learn more about OpenLane & OpenROAD, [you can read this article](/terminology/openlane).

