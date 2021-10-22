---
title: "MPW1 silicon has serious problems"
date: 2021-10-22T15:50:39+02:00
images: ["mpw1_wafer.jpg"]
featured_image: "mpw1_wafer.jpg"
image_pos: 0% 65%
---

[MPW1](/post/asic_submitted) seems an age ago, we submitted in December 2020, but it needed some last minute [DRC fixes in February](/post/last_minute_drc/).

Silicon was received a few weeks ago, and unfortunately we have some serious issues that will prevent most designs from working. This appears to be due to a bad clock tree
in the management section of the chip. Additionally the tool meant to verify the clock tree was also broken.

![Tim Edwards](/tim_edwards_mpw1_fail.png)

The initial announcement is [here](https://groups.google.com/g/skywater-pdk-announce/c/KSRDcyEQEpk).

And I've made a [document trying to collect all the information in one place](https://docs.google.com/document/d/1jRND0EhAWSfLAXHQb2hxlaNhvfcr4skDACXcx0rzDc0/edit).

There's more to find out, and we are still waiting to see how this impacts MPW2 and MPW3.

{{< youtube lw9ucvgQJjk >}}
