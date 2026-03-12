---
title: "Die"
date: 2020-11-13T10:31:34+01:00
images: ["wafermap.svg"]
featured_image: "wafermap.svg"
description: A die is an individual IC cut from a silicon wafer after fabrication; each wafer yields hundreds or thousands of dies that are then packaged for use.
faq:
  - q: What is a semiconductor die?
    a: A die is a single IC cut out of a silicon wafer using a diamond-edged saw. Each wafer is patterned with the same mask set to produce hundreds or thousands of copies, and these individual pieces are called dies (or dice).
  - q: How is a die packaged after being cut from the wafer?
    a: The die is often mounted to a leadframe with epoxy, then bondwires attach the die pads to the leadframe leads, and the whole assembly is encapsulated in injection-moulded plastic to make it larger and easier to handle.
  - q: What happens to faulty dies after wafer slicing?
    a: After separation, the dies are tested and the faulty ones are marked. Only non-faulty dies are then assembled into packages.
---

The silicon [wafer](/terminology/wafer) is usually patterned with the [mask set](/terminology/maskset) to make hundreds or thousands of the same [IC](/terminology/ic). The circle below represents the wafer, the squares represent the copies of the maskset pattern exposed onto the wafer by the stepper. The light squares are completely within the wafer and thus may be functional chips, the others are only partial and so cannot be functional chips.

![wafermap](/wafermap.svg)

Each of these ICs are then cut out of the wafer using a diamond edged saw and are called dies (or die, or dice).

![slicing the die](/die-slicing.jpg)

The die is then somehow packaged. Often they are mounted to a leadframe and then moulded into a plastic packaging to make them larger and easier to handle.

Typically, the separated die are tested at this stage, and the faulty ones marked. Only non-faulty ones would then be assembled into packages.

## Leadframe 

The chip or die would be attached to the central square area of the lead frame with an epoxy glue, then bondwires would attach the pads of the die to the corresponding lead of the frame. The whole leadframe then goes into an injection moulding machine to encapsulate the individual die, four sections of black plastic for this case, then the leadframe is chopped and the leads formed into legs for the finished product.

![leadframe](/leadframe.jpg)

Image from [Sergei Frolov](https://commons.wikimedia.org/wiki/File:DIP_zagotovka.jpg)

Read more about how the dual in line package was created (DIP) in this [Hackaday article](https://hackaday.com/2018/11/08/the-dual-in-line-package-and-how-it-got-that-way/)

The Google [shuttle](/terminology/shuttle) will provide a type of packaging called [Wafer Level Chip Scale Packaging](/terminology/wlcsp).
