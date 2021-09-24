---
title: "Place and Route"
date: 2020-11-12T17:43:12+01:00
images: ["placement-coarse.png"]
featured_image: "placement-coarse.png"
---

Place and Route are 2 steps in the automated process of turning some [HDL](/terminology/hdl) into [GDS2](/terminology/gds2) files.
We will look at how [OpenLane](/terminology/openlane) does these steps using the [seven segment seconds](https://github.com/mattvenn/seven-segment-seconds) example.

I have used my [presentation tools](https://github.com/mattvenn/remoticon-presentation-tools) to generate these images.

# Place

Placement is done in two steps, coarse and fine. The coarse step puts the [standard cells](/terminology/standardcell) in roughly the right place.
The file shown is _replace.def_.

![placement coarse](/placement-coarse.png)

The fine step aligns the cells to the grid and makes sure they don't overlap.
The file shown is _placement.def_.

![placement fine](/placement-fine.png)

# Route

After the cells are in the correct places, the routing of clocks, power and signals can start.

Here is the power distribution, the file shown is _pdn.net_. You can see thick horizontal metal lines carrying power and ground. Then there are the thinner horizontal lines
that connect to the top and bottom of the standard cells. That's why all the standard cells have the power and ground at the top and bottom at a fixed distance.

![pdn](/pdn.png)

And finally, here is a zoomed image of the same design, but showing the routing wires on the metal layers. This file is _routing/design.def_

![routing](/routing.png)

# Clock Tree Synthesis

I don't have a good picture of CTS, but it's worth mentioning here. The clock (and reset) are important and heavily loaded signals. 
The clock especially is probably driving thousands of gates. Each of these gates has a small capacitance that requires some effort to charge or discharge.
For this reason the clock line is treated specially and CTS makes sure the clock drive strength is strong enough by adding special clock buffer standard cells.
