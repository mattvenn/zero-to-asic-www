---
title: "3D Rendering of GDS Files"
date: 2022-10-13T08:00:00+01:00
tags: ["3D render","Blender","course", "GDS" ]
images: ["maximo_render_4.jpeg"]
featured_image: "maximo_render_5.jpeg"
---

The 3D structures created within a silicon [die](/terminology/die) are spectacular to see.

Thanks to Maximo ([@maxiborga](https://twitter.com/maxiborga) on Twitter), there's now a [video for 3D rendering ASIC designs](https://www.youtube.com/watch?v=gBjQI3GrBHU&feature=youtu.be) enabling  anyone to convert their ASIC design into a beautiful 3D rendering.

![MaximoRender4](/maximo_render_5.jpeg)
3D-rendered chip in Blender

{{< youtube gBjQI3GrBHU >}}

His walkthrough shows how to [convert GDS to STL files](https://github.com/mbalestrini/gdsiistl), enabling you to import the files in image editing software like [Blender](https://www.blender.org/).

![3Dinverter](/blender_inverter.png)
By following along the video, I was able to render my first ever GDS, an [inverter I created back in 2020](https://www.youtube.com/watch?v=IQ_DcWT_cbc)


### Additional Resources

Interested in having a physical 3D model of your design instead? Check out [how to 3D print an ASIC](/post/3dcells/).
![3DprintedAND](/3d_and.jpeg)

We also have a great feature added by Maximo and Proppy that lets you generate 3D interactive viewers with your [GDS](/terminology/gds/) in the cloud via a GitHub action. In the [interactive viewer](https://mattvenn.github.io/wokwi-verilog-gds-test/viewer/tinytapeout.html), you can check out the stats, see what standard cells are used as you hover over them, identify what the cell is, and much more -- all within your browser! Check out the [September 2022 Monthly Update](/post/monthly-update-september/) for a quick run through.

In the Zero to ASIC course you will learn how to generate the [GDS](https://www.zerotoasiccourse.com/terminology/gds2/) needed to fabricate your chip and make 3D renderings and prints. No [VLSI](/terminology/vlsi/), [RTL](/terminology/rtl/), or prior [tapeout](/terminology/tapeout/) experience required.

Interested in chip design but hoping to tackle a smaller project first? Check out [Tiny Tapeout](https://tinytapeout.com/). With an easy-to-use a graphical user interface, you can design your own ASIC in less than an evening!

