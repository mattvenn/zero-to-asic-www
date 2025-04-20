---
title: "Sky130 Inverter Instructions"
tags: ["3D printing","GDS"]
date: 2025-01-24T12:48:53+01:00
images: ["3Dcell/parts.jpg"]
featured_image: "3Dcell/parts.jpg"
custom_summary: |
    Instructions for building the Sky130 30000:1 scale inverter. Kits available or print your own!
---

## Parts

Open the bag carefully and pour out the parts. You should have 11 pieces and a sticker.

The parts are made to push fit together. They will wear out if you take it apart and rebuild it more than a couple of times. 

![parts](/3Dcell/parts.jpg)

## Diffusion

This model is of a [CMOS](/terminology/cmos) inverter. The C stands for complementary, and it means we use both N and P type MOSFETS in a complementary pair.

Start by inserting the [N and P doped diffusion](/terminology/doping) into the substrate. Make sure the dots line up.

The P diffusion is larger because the positive charge carriers are slower than the negative charge carriers.

Around the P diffusion you can see a slight depression in the substrate. This normally invisible "well" of N diffusion surrounds the P diffusion and insulates it from the substrate.

![diffusion](/3Dcell/diffusion.jpg)

## Poly silicon gate and A input

The poly silicon gate is what controls the P [MOSFET](/terminology/mosfet) on the top and the N MOSFET below. 

The gate is 150nm wide, or at 30000:1, 4.5mm.

The input to the inverter is the **A** port, on the local interconnect layer. When the input is high, the top P MOSFET is off and the botton N MOSFET is on.

![poly](/3Dcell/poly_li_a.jpg)

## Y Output

The Y output connects the outputs of the N and P MOSFETS together.

![li](/3Dcell/li_y.jpg)

## Assemble Power and Ground rails

It's easier to assemble these parts separately and then add to the model afterwards.

Power is supplied through the top and bottom rails. Every [standard cell](/terminology/standardcell) has the same power supply spacing, so they can fit together easily.

![pwr_gnd](/3Dcell/pwr_gnd.jpg)

## Fit Power and Ground rails

Power flows down through the metal, local interconnect and then into the source of both MOSFETS. On Sky130 this power supply is normally 1.8v. There are other families of standard cell that can tolerate high voltages.

![fit_pwr_gnd](/3Dcell/fit_pwr_gnd.jpg)

## Add the stand

If you want to have the model standing at an angle, add the stand.

![stand](/3Dcell/stand.jpg)

## Congratulations!

You now have your own 30000:1 scale Sky130 inverter! 

If you want to see it in action, check out the [simulation in SiliWiz](https://app.siliwiz.com/). As the input goes high, the output goes low.

![completed](/3Dcell/complete.jpg)

While the inverter is to scale in X and Y dimensions, it's been shrunk in the Z dimension. This is because otherwise it would be too tall and fragile. From the [Sky130 cross section](/terminology/pdk), the local interconnect via is 0.9 microns, so at 30000:1 it would be 30mm tall.


# Resources

* [Buy a kit and support my work!](https://store.tinytapeout.com/products/Sky130-Inverter-Model-Kit-p727081769)
* [Try the SiliWiz lessons to draw and simulate your own inverter](https://tinytapeout.com/siliwiz/)
* [Download the STLs and .3mf file](/3Dcell/sky130_inverter.zip)
* [View and fork the CAD](https://cad.onshape.com/documents/0028930fc0a28cbd8d0bc42b/w/654e56b5a01f78bba7a65678/e/1e7773b38bc6e65d94707c96)
* [Design your own printable cell](/post/3dcells)

