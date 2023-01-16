---
title: "Submit TinyTapeout Projects to an MPW"
date: 2023-01-07T10:00:00+01:00
tags: ["ASIC", "MPW", "TinyTapeout", "course"]
images: ["tinyuserproject.png"]
featured_image: "tinyuserproject.png"
---

Using the *Tiny User Project* tool, people can quickly submit a [Tiny Tapeout](https://tinytapeout.com) design to the MPW lottery. The low barrier to entry makes this a great tool to try variations on a design, test faster I/O speeds on an MPW tapeout, or simply compare tapeout processes using a different submission venue.

[@Proppy](https://twitter.com/proppy) developed the an easy-to-use tool as an extension to the Tiny Tapeout flow. 

[Proppy's template repository](https://github.com/proppy/tiny_user_project) uses GitHub actions to add a design to the [Efabless Caravel User Project](https://github.com/efabless/caravel_user_project). 
The actions automatically perform the steps requried to harden the design, generate the necessary [GDS](\terminology/gds/) files, and even generate a convenient GDS viewer.
Additionally, the actions output useful reports on cell resource utilization, manufacturability errors, and the precheck results.

The GitHub template contains clear instructions for submitting a TinyTapeout design, but as long as you follow the info.yaml semantics, you can submit anything. 
It supports both [Wokwi graphical designs](https://wokwi.com/projects/339800239192932947) as well as [HDL](terminology/HDL) designs.

To see an example submission, take a look at Thorsten Knoll's [(ThorKn on GitHub)](https://github.com/ThorKn/tiny_user_project_vgaclock_mpw8) MPW8 design. Using *Tiny User Project*, Thorsten created a clock that is output to a monitor over VGA. 

The [info.yaml](https://github.com/ThorKn/tiny_user_project_vgaclock_mpw8/blob/main/info.yaml) configures the GitHub action, which then [produces this summary](https://github.com/ThorKn/tiny_user_project_vgaclock_mpw8/actions/runs/3814053720).

For an example on using the tool to submit to the recent GF180 shuttle, take a look at this video.

{{< youtube h3DS4wM3rdY >}}

