---
title: "Floorplan"
date: 2020-11-13T18:20:59+01:00
images: ["floorplan.png"]
featured_image: "floorplan.png"
description: Floorplanning is the ASIC design step where the die area is determined, standard cells are initially gathered, and tap cells and decoupling capacitors are placed to prepare for place and route.
faq:
  - q: What happens during the floorplanning stage of ASIC design?
    a: During floorplanning, LibreLane decides how large an area is needed to fit everything in. All the required standard cells are placed in the bottom left corner, ready for the place and route stage.
  - q: What are tap cells in a floorplan?
    a: Tap cells are the small rectangles placed across the floorplan. They make sure MOSFETs work correctly by connecting the P-doped substrate to ground and the N-wells (which insulate the P-type MOSFETs) to power.
  - q: What are the larger rectangles at the edges of the floorplan?
    a: The slightly bigger rectangles at the edges are decoupling capacitors. After routing is finished, any spare space is also filled with decoupling capacitors, whose job is to ensure all cells receive a smooth power supply.
---

The floorplanning stage is where [LibreLane](/terminology/librelane) decides how big an area we need to fit everything in.
All the required [standard cells](/terminology/standardcell) are placed in the bottom left corner, ready for the [place and route](/terminology/place_and_route) stage.

![floorplan](/floorplan.png)

All the little rectangles in the centre are called tap cells. They make sure the [MOSFETs](/terminology/mosfet) work correctly by connecting the [P doped](/terminology/doping) [substrate](/terminology/wafer) to ground and the N-wells (that insulate the P-type MOSFETS) to power.

The slightly bigger rectangles at the edges are decoupling capacitors. After the [routing](/terminology/place_and_route) is finished, any spare space is filled up with decoupling capacitors. The job of these capacitors is to make sure that all the cells get a nice smooth power supply.
