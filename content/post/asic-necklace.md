---
title: "ASIC Necklace"
date: 2023-11-10T14:57:40+01:00
tags: ["ASIC"]
images: ["necklace/asic_necklace_1.JPG"]
featured_image: "necklace/asic_necklace_1.JPG"
---

For the last few years I've worn an old 4 inch wafer to conferences or whenever I'm teaching in person. People rarely get to handle a wafer and are always interested to know more.

![old necklace](/necklace/old_necklace.JPG)

The problem with the necklace is that it's too hip-hop, and not enough "15 million dollar Nikon Lithography Stepper". I decided to make a new necklace that:

* looks amazing,
* has animated LEDs,
* LEDs are driven by my own [ASIC](/terminology/asic),
* detachable Wafer.

I teamed up with [Pat Deegan](https://psychogenic.com/) and [Adam Zeloof](https://adam.zeloof.xyz/) to help with the electronics and 3D design.

Here's a preview of what we made! Read on to follow the development story, or go [straight to the photos](#photoshoot).

![chain link](/necklace/chain_link.JPG)

# Concept Design

I started with some concept sketches in August 2023. I always prefer paper and pen for the first sketches, much faster for me than working with a computer.

![design sketches](/necklace/asic_necklace_sketches.png)

Most of the work was on designing the links. They needed to be strong, have some flexibility, carry 4 signal wires and look good. 
We decided on gold anodized CNC aluminium links held between sandwiches of PCBs. 

We wanted the light to diffuse through the PCB so that meant using normal FR4 PCBs. The problem with normal PCBs is that while
you can control the top colour nicely (we went with matte black soldermask and gold coated copper traces), the sides are going to look a light brownish colour.

Adam suggested using a black 3D printed part that held the top and bottom PCBs apart while covering the sides of the boards. The bottom boards have a [surface mount soldered nut](https://www.adafruit.com/product/4207?gclid=EAIaIQobChMI6KT4h5eMggMVRUxHAR0z6gJoEAQYAiABEgI8WPD_BwE) and the top board is screwed on with some nice [low profile machine head bolts](?).

![cross section side link](/necklace/link_side.png)

The 3D printed parts are black nylon printed with [Multi Jet Fusion](https://www.protolabs.com/services/3d-printing/multi-jet-fusion/), a technique that gives very nice results with hardly any layer lines.

# Electronics

Obviously I wanted to use my own chips to drive the LEDs. To make it easier I chose the APA102s as they have a separate clock and data line. That means any issues with precise timings are eliminated. 
The signals run from the centre board around the chain via FFCs - flat flexible cables. This was definitely a mistake and will be fixed in the future with some hardier connectors.

The chip I used is the one we submitted for [MPW6](/post/mpw6_submitted). I used the RISCV processor to bitbang the LEDs and I plan to use one of the ring oscillator tests as a crude temperature sensor to change the speed of the animation.

The schematics are based off of a [minimal viable ASIC board](https://github.com/TinyTapeout/caravel-mvp-pcb) by Pat. It includes all the things we need to get one of my ASICs functioning - 2 power rails, oscillator, flash. We also added a couple of buttons to change modes, and some decorative stripes also serve double duty as capacitive touch strips.

![tip render](/necklace/tiptop-floorplan.png)

We did some basic testing with the LEDs to see how they'd diffuse through the PCB and this then set the size of the decorative patterns around the chain.

![led testing](/necklace/Y0-chain-APA102C-exp.jpg)

Pat did some [pretty nice work on estimating power usage on the LEDs](/necklace/APA102CAnalysis.pdf), and that helped us size the battery. We went with a 400mAh LiPo that lasts for about 2 hours. I keep some spares in my pocket and swap them over when it runs out.

The bottom PCBs were just cheap 2 layer with black solder mask. The top boards were a lot more expensive: matte black with gold coated traces.

# Decorative pattern

I knew I wanted something that represented a [MOSFET](/terminology/mosfet), as they're fundamental to all my chip design so far. I also thought it would be cool to have the MOSFET connections run around the chain as a kind of secondary electronic chain carried by the physical chain.

![mosfet patterns](/necklace/mosfet_patterns.png)

Adam finally came up with something that fit the link, looked good and connected a 3 pin device to a 4 pin chain link.

![mosfet final](/necklace/mosfet_final.png)

# Ordering

Finally, we started ordering parts.

* Aluminium links from [Runzemetal](https://runzemetal.m.en.alibaba.com/index.html) on the 14th,
* Plastics from [?](?) on the 22nd, and
* PCBs from [PCBWay](https://www.pcbway.com/) on the 25th
* Parts from [Adafruit](https://www.adafruit.com/) and [DigiKey](https://www.digikey.es/) on the 25th.

This was cutting it extremely close to the deadline! I wanted to debut the necklace at [Hackaday Supercon](https://hackaday.io/superconference/), and the PCBs needed to land with Pat before his flight on the 31st. 

The PCBs went "out for delivery" on the 30th, but nobody actually showed up. Thankfully PCBs arrived on the 31st and Pat pulled an all-nighter to get the soldering done before leaving for LA.

![plastics and links](/necklace/plastics_link_test.jpg)

Aluminium links and plastics arrived on the 31st and fitted well. Thanks Esden and Timon for the CNC factory recommendation!

We got lucky to have everything in time. Looking back, a bit more project planning would have been helpful. It wasn't clear to us that we wouldn't be able to order the PCBs until we basically had everything else finalised.

# Assembly

Pat and I arrived in LA before Adam, and we tried plugging the links together for the first time and getting a quick firmware to control the lights. Amazingly it all worked, but the update rate of the LEDs was extremely slow. I decided to just leave it on green, as it looked the best when diffused through the PCBs.

![led test](/necklace/led_test.JPG)

After my [Tiny Tapeout workshop](https://tinytapeout.com) Adam arrived and we tried fitting it all together.

![assembly](/necklace/assembly.png)

It really came together well, very good for a first assembly and also the first time we'd all worked together as a team. 

![team](/necklace/team.jpg)

# Wearing it at the con

At 500 grams, it's a lot heavier than my previous necklace! It took some time to get used to wearing it. It definitely needs to hang down a bit over my back or the links bend too much around my neck.

![matt con](/necklace/matt_con.jpg)

Over the 3 days we exposed some design flaws:

* The wafer clip was meant to be a "snap fit", but it wasn't quite snappy enough and the wafer fell off a couple of times.
* The clearance between the aluminium and the PCBs was meant to limit the chain to around a 15 degree movement but it can actually around 45 degrees.
* The FFC cables are too exposed, fragile and can get pulled out by excessive chain flexing.

We weren't sure about the FFC so we designed in a backup: extra pads on the back of the boards we could just solder wires to. I had to fix the chain twice during the con when cables failed. 

# Photoshoot

Thanks to Bruce and Majenta at Supplyframe for letting me use the design lab for the backdrop.

![best of](/necklace/best_of.png)

Here's a high resolution [gallery of my favourite photos](https://photos.app.goo.gl/3chxmgiNRyWBmcy26).

# Resources

* [All the photos](https://photos.app.goo.gl/Urtsa7ztqAidyRfUA)
* The necklace on Adam's [open jewelry](https://open.jewelry/jewelry/7/) site.
* [Firmware](https://github.com/mattvenn/asic-necklace-fw)
* [PCBs repository pending]()
* [OSHWA certification pending]()
