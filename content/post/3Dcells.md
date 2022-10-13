---
title: "3D printed standard cells"
date: 2022-10-08T08:00:00+01:00
tags: ["3D printing","GDS", "course" ]
images: ["3d_and.jpeg"]
featured_image: "3d_and.jpeg"
---

ASICs pack in billions of [transistors](/terminology/mosfet/) per square centimeter, making their construction and functionality impossible to understand with the naked eye.

In fact, the upcoming [2 nanometer technology](https://appuals.com/tsmc-2nm/) will be so small* that the transistor dimensions will only be 20X larger than an individual atom. 

Wouldn't it be great to see how ASICs are built in 3D at a scale that our bulky human hands can appreciate?

Well wait no longer! Thanks to [Thorsten Knoll's guide](https://medium.com/@thorstenknoll/open-source-ic-cells-as-3d-prints-a-rough-how-to-guide-90a8bc8b3b57), you can now 3D print the cells that make up an ASIC using the [GDS](/terminology/gds2/) files. 

![Transistors Shrinking](/timeline.jpg)
Evolution of ASICs, from [Computer History](https://www.computerhistory.org/siliconengine/)

These 3D structures are an excellent way to visualize how the different metal and silicon layers are combined to create a chip. They also make an excellent accent piece for your office or workshop.

![3Dand](/3d_and.jpeg)
3D-printed AND gate, courtesy of Thorsten Knoll

In the Zero to ASIC course you will learn how to generate the [GDS](/terminology/gds2/) needed to not only 3D print your design, but also fabricate your chip in silicon. No [VLSI](/terminology/vlsi/), [RTL](/terminology/rtl/), or prior [tapeout](/terminology/tapeout/) experience required.

Interested in chip design but hoping to tackle a smaller project first? Check out [Tiny Tapeout](https://tinytapeout.com/). With an easy-to-use a graphical user interface, you can design your own ASIC in less than an evening!

*The dimensions implied by a node's name (e.g. 2 nm) aren't entirely truthful. Learn more about [CMOS Node Size](/terminology/node/)
