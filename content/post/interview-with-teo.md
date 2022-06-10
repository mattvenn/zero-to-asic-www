---
title: "Interview With Teo"
date: 2022-05-10T10:22:31+02:00
tags: ["interviews"]
images: ["adders.png"]
image_pos: 0% 20%
featured_image: "adders.png"
---

Teodor-Dumitru Ene has been doing some interesting work on optimising hardware adders.
Until I spoke with him, I didn't realise how important this basic digital building block really is.
An interesting statistic from his [presentation slides](https://bit.ly/3MYTlCf):

*When a RISC-V processor boots into Linux, 65% to 72% of instructions use addition.*

By default, Yosys will synthesise something like this:

    reg [31:0] a;
    reg [31:0] b;
    wire sum = a + b;

Using a 'middle of the road' adder, that gives medium PPA (power, performance, area) results. 
Teo has made a [Python library and Yosys plugin](https://github.com/tdene/synth_opt_adders) that allows us to choose between 4 other types of adder:

* Ripple-carry
* Sklansky
* Brent-Kung
* Kogge-Stone

These different adders all have different PPA results, and we can choose the one we want for a specific application.

We did a [livestream](https://www.youtube.com/watch?v=P7wjB2DKAIA) presenting his work, but we also made this more consise edited version.

{{< youtube ZvssTXMTRmk >}}

# Development work

Teo did his PPA measurements using [Proppy's Jupyter notebooks](/post/asic-dev-in-the-cloud), which meant he didn't
need to download the [PDK](/terminology/pdk) or [OpenLane tools](/terminology/openlane).

We thought it would be a good experiment to take the adders and put them onto the MPW6 shuttle, with a means to measure how fast they are.
You can [read more about that here](/post/instrumenting-hardware-adders).

# Resources

Teo's main repository - https://github.com/tdene/synth_opt_adders

Keep up to date with Teo's work on [Twitter](https://twitter.com/td_ene).

