---
title: "VGA clock"
date: 2020-11-12T19:13:04+01:00
images: ["vga_clock.jpg"]
featured_image: "vga_clock.jpg"
---

This is one of the first projects I [hardened](/terminology/harden) using [OpenLane](/terminology/openlane).

News update: my clock works!

{{< twitter user="matthewvenn" id="1509491474722967553" >}}

It shows the time on an LCD panel. It will be part of my first [tapeout](/terminology/tapeout).

After running the OpenLane ASIC flow, it results in a design that uses 180x180 microns (32000 square microns).
As we have about 10e6 square microns in the user project area of the Google [shuttle](/terminology/shuttle), I could potentially put about 300 of these on the ASIC!

![vga clock](/vga_clock.jpg)

For more information, check the project's [repository](https://github.com/mattvenn/vga-clock)

This project taped out on [MPW1](/post/asic_submitted).
