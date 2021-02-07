---
title: "Last minute DRC fixes"
date: 2021-02-07T18:47:01+01:00
tags: ["videos", "updates"]
featured_image: "/m5shorts.png"
---

The story of the first Open Source ASIC shuttle continues! 

A few of the applicants to the first shuttle were recently contacted by efabless - they had discovered some DRC issues that couldn't be waived by the foundry.

In my recent [interview with Tim Edwards](/post/interview-with-tim-edwards), he mentioned that Google are paying for a license of Calibre - another swiss army ASIC tool like Magic. This is to help make sure that the OpenLANE DRC hasn't missed anything.

Well, you guessed it - some problems get through. It turned out that OpenLANE did detect them - but weren't reported in a way that constituted an error.

This screenshot shows metal 5, the top most layer of the [Skywater stackup](/terminology/pdk). It should be reserved for the [Power Delivery Network](/terminology/PDN.md).

Some [macros](/terminology/macro) had wires on metal5, even though the configuration should have prevented that.

![M5 shorts](/m5shorts.png)

The DRC issue was overlapping sections of metal, but this also causes a short between the macros and the PDN - in my case it would have broken the entire chip design! These were fixed pretty easily and in the future OpenLANE will report these DRC errors.
The shorts could have been detected with [LVS](/terminology/lvs), but this is currently only run for the macros, not after they have been added to the Caravel harness.

I made a short video explaining this if you're interested to know more.

{{< youtube 0D8h_5Ei4xs >}}


