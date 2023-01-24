---
title: "ASIC"
date: 2020-11-12T17:38:37+01:00
images: ["asic-zoom.png"]
featured_image: "asic-zoom.png"
---

Application Specific Integrated Circuit. An ASIC is a custom [IC](/terminology/ic), which means it is not a standard product such as a microprocessor, memory, standard logic chip or generic component which might be available from several or many different manufacturers. It will often add functionality not available from a standard product, or combine the functions of many standard products at a lower total price.

You might make an ASIC because:

* You need a chip that isn't available off-the-shelf,
* You can save money by merging a lot of components into one,
* Recently, for fun!

If your design only needs digital logic, you might be able to use an [FPGA](/terminology/fpga). An advantage of ASICs is that they can combine digital and analogue circuits together in one chip. A disadvantage is that errors often cannot be fixed afterwards, hence the heavy use of [verification](/terminology/verification).

Big semiconductor companies produce millions of chips, which can offset the large costs related to the [masks](/terminology/maskset). For example, a full maskset for the 130nm process at the Skywater [foundry](/terminology/foundry) costs about $200k.

Until recently, an additional cost was the license fee for the ASIC software tools. Now we have the open source tools like [OpenLane](/terminology/openlane) that have opened the door to experimentation and learning.

Here's a picture from [magic](/terminology/magic) showing a layout of my [VGA clock](/post/vga_clock)

![vga clock asic](/asic-full.png)

And a zoom, more clearly showing the [standard cells](/terminology/standardcell)

![vga clock asic zoom](/asic-zoom.png)
