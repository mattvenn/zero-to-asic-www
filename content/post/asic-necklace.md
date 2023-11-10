---
title: "ASIC Necklace"
date: 2023-11-10T14:57:40+01:00
tags: ["ASIC"]
images: ["necklace/asic_necklace_1.JPG"]
featured_image: "necklace/asic_necklace_1.JPG"
---

For the last few years I've worn an old 4 inch [wafer](/terminology/wafer) to conferences or whenever I'm teaching in person. People rarely get to handle a wafer and are always interested to know more.

![old necklace](/necklace/old_necklace.JPG)

While it's a fantastic conversation starter, the problem with this necklace is that it's too hip-hop, and not enough "15 million dollar Nikon [Lithography](/terminology/photolithography) Stepper". To resolve this annoyance, I decided to make the most ridiculous ASIC bling possible - using my own chips of course! The only thing I kept from the old design was the quick release wafer.

A project like this needs a great team - and I got lucky with [Pat Deegan](https://psychogenic.com/) and [Adam Zeloof](https://adam.zeloof.xyz/).

Read on to follow the development story, or go [straight to the photos](#photoshoot).

![chain link](/necklace/chain_link.JPG)

# Concept Design

I started with some concept sketches in August 2023. I always prefer paper and pen for the first sketches, much faster for me than working with a computer.

![design sketches](/necklace/asic_necklace_sketches.png)

The challenging part was making strong, flexible, conductive and most importantly - good looking links.

After a few iterations we decided on gold anodized CNC aluminium links held between sandwiches of PCBs. The top PCB acts as a decorative light diffusor while the bottom holds the LED and passes the signals around the chain.

# 3D design

Adam did the design with [Onshape (account needed to view the design)](https://cad.onshape.com/documents/c94b1292cdd70523373dfc49/w/5a27a2dce2dc4d92de3e72a3/e/d27912885e214c193a7992b3?renderMode=0&uiState=654a3a25f0cd5e4bcf412c07), which certainly made collaboration easier. 

We realised that the edges of the PCB sandwichs wouldn't look great so Adam designed a black 3D printed part that held the top and bottom PCBs apart while covering the sides of the boards. The bottom boards have a [surface mount soldered nut](https://www.adafruit.com/product/4207?gclid=EAIaIQobChMI6KT4h5eMggMVRUxHAR0z6gJoEAQYAiABEgI8WPD_BwE) and the top board is screwed on with some nice [low profile machine head bolts](?).

![cross section side link](/necklace/link_side.png)

The 3D printed spacers are nylon printed with [Multi Jet Fusion](https://www.protolabs.com/services/3d-printing/multi-jet-fusion/), a technique that gives very nice results with hardly any layer lines. Adam used this technique a lot when he worked at Boston Dynamics.


# Decorative pattern

I knew I wanted something that represented a [MOSFET](/terminology/mosfet), as they're fundamental to all my chip design so far. I also thought it would be cool to have the MOSFET connections run around the chain as a metaphorical secondary electronic chain carried by the physical chain.

![mosfet patterns](/necklace/mosfet_patterns.png)

I was really struggling to come up with a design that I was happy with, but finally Adam came up with something that was proportional to the link, looked good and connected a 3 pin device to a 4 symmetric wires. Yes I know MOSFETs are 4 pin devices. No, I couldn't get it to look good in the space we had.

# Diffusion 

LED diffusion is crucial to a high-class blinky. Pat did some testing with the LEDs to see how they'd diffuse through the PCB. We measured the diameter of the light hitting some layers of paper held over the LED and used that for the diameter of the logo.

![led testing](/necklace/Y0-chain-APA102C-exp.jpg)

We blocked the light by covering everything outside the logo with copper, draped the copper with the mattest of matte black soldermask and topped it all off with stunning gold plated traces.

![mosfet final](/necklace/single_link.JPG)

# Electronics

The chips I used were extremely rare, an exclusive vintage we submitted to [Efabless chipIgnite](https://efabless.com/). 

Unfortunately it doesn't contain my WS2812 LED driver [macro](/terminology/macro), so for the LEDs, I went with the easier to drive [APA102s](https://cdn-shop.adafruit.com/product-files/2477/APA102C-iPixelLED.pdf).

I used the chip's on-board RISCV processor to bitbang the LEDs.  I plan to use one of my ring oscillator designs as a crude temperature sensor to change the speed of the animation.

The chip is mounted nicely in the center of the board and sends signals around the chain via flexible cables.

![tip](/necklace/tiptop-floorplan.png)

The schematics are based off of a [minimal viable ASIC board](https://github.com/TinyTapeout/caravel-mvp-pcb) by Pat. It includes all the things we need to get one of my ASICs functioning - 2 power rails, oscillator and flash. We also added a couple of buttons to change modes, and some decorative stripes also serve double duty as capacitive touch sensors.

Pat did some [very nice work on estimating power usage on the LEDs](/necklace/APA102CAnalysis.pdf), and that helped us size the battery. 
The APA102s are meant to require 5v, but we run them direct from the LiPo and they work fine.
We went with a 400mAh LiPo that lasts for a measly 2 hours. Always prepared, I keep some spares in my pocket and swap them over when no-one's looking.


# Ordering

Finally... we started ordering parts.

* Aluminium links from [Runzemetal](https://runzemetal.m.en.alibaba.com/index.html) on the 14th,
* Plastics from [?](?) on the 22nd,
* PCBs from [PCBWay](https://www.pcbway.com/) on the 25th,
* Parts from [Adafruit](https://www.adafruit.com/) and [DigiKey](https://www.digikey.es/) on the 25th.

This was cutting it so close to the deadline it was tighter than 2 MOSFETs in a NAND gate! I wanted to debut the necklace at [Hackaday Supercon](https://hackaday.io/superconference/), and the PCBs needed to land with Pat before his flight on the 31st. 

![fingers crossed](/necklace/fingers_crossed.png)

The PCBs went "out for delivery" on the 30th, but nobody actually showed up. Thankfully they arrived on the 31st and Pat pulled an all-nighter getting high on solder fumes to get it done before leaving for LA.

![tip](/necklace/just-the-tip.jpg)

Aluminium links and plastics arrived on the 31st and fitted well. Thanks Esden and Timon for the CNC factory recommendation!

![plastics and links](/necklace/plastics_link_test.jpg)

We got lucky to have everything in time. Looking back, a bit more project planning would have been helpful. It wasn't clear to us that we wouldn't be able to order the PCBs until we basically had everything else finalised.

# Assembly

Pat and I arrived in LA before Adam, and we tried plugging the links together for the first time and getting a quick firmware to control the lights. Amazingly it all worked, but the update rate of the LEDs was extremely slow. 
I decided to just leave it simple and kept it a solid green. Easy to add animation later.

![led test](/necklace/led_test.JPG)

After my [Tiny Tapeout](https://tinytapeout.com) workshop at the conference Adam arrived and we tried fitting it all together for the first time. Nail biting! 

![assembly](/necklace/assembly.png)

It came together really well, very good for a first assembly and also the first time we'd all worked together as a team. I'd like to pretend I knew it was all going to work first time, but it's still pretty rare.

![team](/necklace/team.jpg)

# Wearing it at the con

At 500 grams, it's a lot heavier than my previous necklace! It took some time to get used to wearing it. It definitely needs to hang down a bit over my back or the links bend too much around my neck. 
You might think I stood out, but the con's blinky game was so strong I blended right in.

![matt con](/necklace/matt_con.jpg)

Over the 3 days we exposed some design flaws:

* The wafer clip was meant to be a "snap fit", but it wasn't quite snappy enough and the wafer fell off a couple of times.
* The clearance between the aluminium and the PCBs was meant to limit the chain to around 15 degrees of movement but it can actually move around 45 degrees.
* The FFC cables are too exposed, fragile and can get pulled out by excessive chain flexing.

We were never convinced by the FFCs so as consummate professionals we had designed in a backup: extra pads on the back of the boards we could just solder wires to. I executed a high pressure fix right before my interview with [Make](https://makezine.com/article/maker-news/hackaday-supercon-2023-lights-up-pasadena/)!

# Photoshoot

Thanks to Bruce and Majenta at Supplyframe for letting me use the [design lab](https://supplyframe.com/designlab)'s CNC machines as the sexy backdrop.

![best of](/necklace/best_of.png)

Now go and enjoy the high resolution [gallery of my favourite photos](https://photos.app.goo.gl/3chxmgiNRyWBmcy26)!

# Resources

* [All the photos](https://photos.app.goo.gl/Urtsa7ztqAidyRfUA)
* The necklace on Adam's [open jewelry](https://open.jewelry/jewelry/7/) site.
* [3D CAD](https://cad.onshape.com/documents/c94b1292cdd70523373dfc49/w/5a27a2dce2dc4d92de3e72a3/e/d27912885e214c193a7992b3?renderMode=0&uiState=654a3a25f0cd5e4bcf412c07)
* [Firmware](https://github.com/mattvenn/asic-necklace-fw)
* [PCBs repository pending]()
* [OSHWA certification pending]()

# Special thanks

* [Adam Zeloof](https://adam.zeloof.xyz/) and [Pat Deegan](https://psychogenic.com/) 
* [Efabless for the chips](https://efabless.com)
