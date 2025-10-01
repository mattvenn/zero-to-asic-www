---
title: "Photolithography"
date: 2020-11-13T10:57:47+01:00
images: ["die.jpg"]
featured_image: "die.jpg"
---

Sam Zeloof did a great talk about his home [IC](/terminology) [foundry](/terminology/foundry) at the Hackaday Supercon 2019.

{{< youtube 23fTB3hG5cA >}}

This slide shows an overview of the process:

![photolithography](/photolithography.png)

A series of [masks](/terminology/maskset) is used to build up a 3 dimensional structure on the [wafer](/terminology/wafer).

Each step is fundamentally the same:

* Deposit a layer of silicon dioxide (glass) on the surface of the wafer
* Coat the glass with photoresist (which is a light sensitive organic compound, similar to photographic emulsion)
* Bake it
* Use a mask to cover certain areas and use light (often UV) to illuminate the areas not covered
* Develop the photoresist, which will wash out the areas exposed. This leaves holes through to the glass
* Etch the glass through the holes in the resist - this turns the glass into a 'hard mask'
* Strip away the remaining photoresist
* Now use the hard mask to control where the next step can take effect, for instance we could [implant dopants](/terminology/doping) to change the electrochemical properties. The dopant will reach the silicon beneath only where there are holes in the hard mask. Or we can etch away underlying metal (in older aluminimum processes), or in modern copper processes grow metal in the trenches in the glass.
* If no longer need the hard mask, strip it away and repeat the whole process for the next layer up.

Photolithography is the key that allows us to take the patterns we create in a tool like [Magic](/terminology/magic) or [LibreLane](/terminology/librelane) and miniaturise them down to the nanometer scale. It also lets us easily tile the same design over the [wafer](/terminology/wafer) to make the individual [dies](/terminology/die). It allows us to use a prepared image of the chip to make millions of copies reliably and rapidly.

This cross section shows how the layers are used to build up the 3 dimensional structures that make up the IC.

![cross section](/ic-cross-section.jpeg) [Image source](https://twitter.com/reivilo_t/status/1324402794783215616/photo/1)
