---
title: "Photolithography"
date: 2020-11-13T10:57:47+01:00
featured_image: '/die.jpg'
---

Sam Zeloof did a great talk about his home [IC](/terminology) [foundry](/terminology/foundry) at the Hackaday Supercon 2019.

{{< youtube 23fTB3hG5cA >}}

This slide shows an overview of the process:

![photolithography](/photolithography.png)

A series of [masks](/terminology/maskset) is used to build up a 3 dimensional structure on the [wafer](/terminology/wafer).

Each step is fundamentally the same:

* coat the wafer in photo resist
* bake it
* use a mask to cover certain areas and use light (often UV) to illuminate the areas not covered
* develop the mask, which will wash out the areas exposed. This leaves holes through to the previous layer.
* now we can apply a process to the exposed areas. This includes things like:
    * growing a layer of silicon dioxide
    * growing a layer of polysilicon
    * metalising the area
    * [implanting](/terminology/doping) impurities that change the electrochemical properties

Photolithography is the key that allows us to take the patterns we create in a tool like [Magic](/terminology/magic) or [OpenLane](/terminology/openlane) and miniaturise them down to the nanometer scale. It also lets us easily tile the same design over the [wafer](/terminology/wafer) to make the individual [dies](/terminology/die)
