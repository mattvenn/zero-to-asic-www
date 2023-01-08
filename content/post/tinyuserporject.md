---
title: "Submit a TinyTapeout Project to a MPW"
date: 2023-01-07T10:00:00+01:00
tags: ["ASIC", "MPW", "TinyTapeout", "course"]
images: ["tinyuserproject.png"]
featured_image: "tinyuserproject.png"
---

We're excited to highlight an open-source tool enabling people to easily submit [TinyTapeout](https://tinytapeout.com/runs/) projects to the [Efabless MPW ASIC submissions](https://platform.efabless.com/projects/public).

[@Proppy](https://twitter.com/proppy) has developed the easy-to-use tool call *Tiny User Project*. [Proppy's template repository](https://github.com/proppy/tiny_user_project) uses GitHub actions to add a TinyTapeout design to the [Efabless Caravel User Project](https://github.com/efabless/caravel_user_project). The actions automatically perform the steps requried to harden the design, generate the necessary [GDS](\terminology/gds/) files, and even generate a convenient GDS viewer. Additionally, the actions output useful reports on cell resource utilization, manufacturability errors, and the precheck results.

The GitHub template contains clear instructions for submitting your TinyTapeout design. It supports both [Wokwi graphical designs](https://wokwi.com/projects/339800239192932947) as well as [HDL](terminology/HDL) designs.

Using *Tiny User Project*, people can quickly submit a design to the MPW lottery. The low barrier to entry makes this a great tool to try variations on a design, test faster I/O speeds on an MPW tapeout, or simply compare tapeout processes using a different submission venue.

To see an example submission, check out Thorsten Knoll's [(ThorKn on GitHub)](https://github.com/ThorKn/tiny_user_project_vgaclock_mpw8) submission to MPW8. Using *Tiny User Project*, Thorsten created a clock that is output to a monitor over VGA. The summary of his design and GDS image are available [here](https://github.com/ThorKn/tiny_user_project_vgaclock_mpw8/actions/runs/3814053720).
