---
title: "Corner"
date: 2021-03-22T16:59:20+01:00
images: ["corners.png"]
featured_image: "corners.png"
---

[MOSFET](/terminology/mosfet) characteristics can vary across multiple wafers.

If we wanted to make sure a sensitive analogue design worked across all process variations, we would want to simulate these variations and check the results were still within our specification.

Some of the most common variations affect the strength or speed of the MOSFET switching, and we have both P and N type MOSFETS.
The corners represent the most extreme variations of these parameters. By combining them, we get these combinations:

* FF (fast fast)
* SF (slow fast)
* SS (slow slow)
* FS (fast slow)
* TT (typical typical)

We have [SPICE models](/terminology/spice) of the different corners provided in the [Skywater PDK](/terminology/pdk).

![corners included in spice file](/corners.png)

For my basic simulations, I often remove all the corner libraries except TT, to speed up the simulation time. 

For more information, check this Wikipedia page: https://en.wikipedia.org/wiki/Process_corners
