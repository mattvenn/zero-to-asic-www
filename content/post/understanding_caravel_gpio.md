---
title: "Understanding Caravel GPIO"
date: 2021-02-15T13:36:29+01:00
featured_image: "/caravel_gpio.png"
---

When I was first testing my designs inside [Caravel](/terminology/shuttle#caravel), I was quite confused about all the GPIO options.

![Caravel GPIO](/caravel_gpio.png)

* Each pin has a range of options that can be configured by firmware running on the RISCV processor.
* Each pin can be driven from the processor or your custom design.
* The outputs have separate output enable lines for bi-directional signalling.

I put together an experiment where I tried the most important options and checked the results in a simulation. You can watch the video here:

{{< youtube pmgeKmqoxTs >}}

* Supporting [documentation](https://docs.google.com/document/d/1l8JvyWgmqLUiq--4obh6iiVnrIt9EOC_Huj9r8eRLk4)
* The github repository is here: https://github.com/mattvenn/caravel_gpio
