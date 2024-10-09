---
title: "Looking inside an open source ASIC with Zeptobars"
date: 2024-08-03T14:18:07+02:00
tags: ["interviews", "videos"]
images: ["decap_zepto.png"]
featured_image: "decap_zepto.png"
---

In this interview, I met up with Michael from [Zeptobars](https://zeptobars.com/en/) in Zurich, Switzerland, where we use acid to **decapsulate one of my Tiny Tapeout chips.**  This technique involves using acid to remove the protective epoxy layer of a chip, revealing the silicon die underneath.   Decapping is commonly used to analyse the construction of integrated circuits. Michael usually decapsulates chips designed by others, sometimes decades ago, but this time one of the designs is his own.

We used sulphuric acid heated to 250°C to remove the epoxy. Michael mentions that, while there are multiple methods for decapping chips, he finds using acid to be the most effective. Nitric acid is also commonly used, but it is not as readily available in its purest form, as it is a sensitive chemical. Sulphuric acid requires higher temperatures but is safer when cold. 

{{< youtube zUv6sdxOaFE >}}

Once the chip is decapped, we use a microscope to examine the die. While the acid used removed the metal and glass layers, the silicon remained. This allows for a direct comparison between the GDS files used to manufacture the chip and the actual physical layout of the silicon. Check the high resolution images here: https://zeptobars.com/en/read/tt04-tinytapeout-silicon-inside-gds-sky130

The [Tiny Tapeout 4 chip](https://tinytapeout.com/runs/tt04) used in the video was fabricated using the SKY130 process. The video also shows the GDS layout of Michael’s design. The process of dissolving the epoxy took 15 minutes, performed at 60°C. Michael notes that it’s important to monitor the process as, if left too long, the exposed silicon can oxidise and degrade the “picture.” 

The video concludes by highlighting the significance of open-source ASIC design.  The transparency provided by open-source tools and PDKs allows for this level of analysis and comparison, which is rarely possible with proprietary chips and tools. 

Another way to look inside microchips is with xrays, [I visited a synchrotron](/post/inside-my-first-asic/) to find out how!
