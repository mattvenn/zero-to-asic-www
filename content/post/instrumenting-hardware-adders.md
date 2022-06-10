---
title: "Instrumenting Hardware Adders"
date: 2022-06-10T10:23:33+02:00
images: ["instrumented_adder.png"]
image_pos: 0% 20%
featured_image: "instrumented_adder.png"
---

Following my [interview with Teo](/post/interview-with-teo) on optimising hardware adders, I thought
it would be a great project to tapeout on MPW6.

I wrote about the process on twitter:

{{< twitter user="matthewvenn" id="1526591700122185728" >}}

As usual with ASIC development, it's much faster to say what you want to do than to actually do it!

Teo's Python library makes it very simple to create the adders at an arbitrary width, so the challenge was
to find a way to measure how fast they are.

If you saw the interview series I did with [Andrew Zonenberg](https://www.youtube.com/playlist?list=PLyynFETmdQDQtBEQswy2Io_Kd3FdZkyxG) about characterising OpenRAM, you'll know the results weren't great because the OpenRAM block was just connected straight to the IOs of the ASIC.

This made it quick and easy to tapeout, but created problems in getting accurate measurements. That's because there are [parasitics](/terminology/pex/) and skew in the traces that affected timing and can't be removed from the results because we don't know what they were. 

To avoid this with the adders, we built a measurement circuit around the adder:

![instrumented adder](/instrumented_adder.png)

The top half is a ring oscillator with a few different pathways. We used 31 inverters for a loop frequency of about 250MHz. The different paths through the loop are:

* bypass - just the 31 inverters
* control - adds another 4 inverters
* adder - through any bit of the adder.

We can also set the a and b inputs and get the sum out, which allows us to verify the adder actually works.

The bottom half shows a couple of registers (with adders!) that allow us to program an integration time. While that counter is counter down at the system clock speed (10MHz), the oscillator counter will be counting up. 

When the integration counter finishes we can divide one by the other to get the speed of the loop. By changing swapping in and out the different bits of the adder we'll be able to measure exactly how fast it is, and compare the 5 different adders we put on MPW6:

* Behavioural (default Yosys)
* Ripple-carry
* Sklansky
* Brent-Kung
* Kogge-Stone

The repository we taped out on [MPW6](/post/mpw6_submitted) is here: https://github.com/mattvenn/wrapped_instrumented_adder. There are 5 different branches, one for each type of adder.

Video coming soon!
