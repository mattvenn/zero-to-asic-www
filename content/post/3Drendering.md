---
title: "3D Rendering of GDS Files"
date: 2022-10-13T08:00:00+01:00
tags: ["3D render","Blender","course", "GDS" ]
images: ["blender_inverter.png"]
featured_image: "blender_inverter.png"
---

The 3D structures created within silicon [die](/terminology/die) can be fascinating to see.

More than just aesthetics, being able to explore these 3D structures of an ASIC virtually is an important part of understanding how an analog or digital design is [synthesized](/terminology/synthesis/).

Now thanks to a [video for 3D rendering ASIC designs](https://discord.com/channels/778248761054986292/872889375384555622/1027258297226625084) by Maximo ([@maxiborga](https://twitter.com/maxiborga) on Twitter) and Proppy, anyone can convert their ASIC design into a beautiful 3D rendering. His walkthrough shows how to [convert GDS to STL files](https://github.com/mbalestrini/gdsiistl), enabling you to import the files in image editing software like [Blender](https://www.blender.org/).

We also have a great feature added by Maximo and Proppy that lets you generate 3D interactive viewers with your [GDS](/terminology/gds/) in the cloud via a GitHub action. In the [interactive viewer](https://mattvenn.github.io/wokwi-verilog-gds-test/viewer/tinytapeout.html), you can check out the stats, see what standard cells are used as you hover over them, identify what the cell is, and much more -- all within your browser! Check out the [September 2022 Monthly Update](/post/monthly-update-september/) for a quick run through.

![3Dinverter](/blender_inverter.png)
3D-rendered inverter in Blender

{{< youtube gBjQI3GrBHU >}}

Want a physical 3D model of your design instead? Check out [how to 3D print an ASIC](/post/3dcells/).

In the Zero to ASIC course you will learn how to generate the [GDS](https://www.zerotoasiccourse.com/terminology/gds2/) needed to fabricate your chip and make 3D renderings and prints. No [VLSI](/terminology/vlsi/), [RTL](/terminology/rtl/), or prior [tapeout](/terminology/tapeout/) experience required.

Interested in chip design but hoping to tackle a smaller project first? Check out [Tiny Tapeout](https://tinytapeout.com/). With an easy-to-use a graphical user interface, you can design your own ASIC in less than an evening!

