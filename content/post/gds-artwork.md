---
title: "GDS Artwork"
date: 2020-11-20T17:58:11+01:00
description: "artwork on the top metal layer"
images: ["chip-artwork.jpeg"]
featured_image: "chip-artwork.jpeg"
---

I've always thought the artwork people put in the top layer of their chips was cool.
Do a google image search for [chip artwork](https://www.google.com/search?q=chip+artwork) to see some more fun examples.

![chip artwork](/chip-artwork.jpeg)

While waiting for some toolchain bugs to get ironed out I've made a tool to help me make logos. It can take SVG or PNG input and
makes a [GDS2](/terminology/gds2) file output. These files can then be merged together to create the final layout for the [ASIC](/terminology/asic).

Code is [here](https://github.com/mattvenn/logo-to-gds2)
