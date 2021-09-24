---
title: "Printing my first ASIC's GDS files"
date: 2021-02-24T16:46:34+01:00
images: ["macro_photo.jpg"]
featured_image: "macro_photo.jpg"
---

I've been wanting to try plotting or printing the GDS files from my first ASIC for a while, and finally I've had some time to have a play.
I used KLayout because it's easy to change colours, show and hide layers, and export to a high resolution PNG.

I want to make a poster with 3 pictures inside: 

1. The whole chip,
2. Zoomed into the VGA clock macro,
3. Zoomed into the standard cells.

Here's a photo of the print (I know, how meta) of 1:

![caravel photo](/caravel_photo.jpg)

Number 2:

![macro photo](/macro_photo.jpg)

And number 3:

![macro photo](/standard_cell_photo.jpg)

You can check my layout property files that define colours and layers here: https://github.com/mattvenn/klayout_properties

And I made a video showing how to use KLayout and how to export the PNG files:

{{< youtube 9SZye3jDQTU >}}
