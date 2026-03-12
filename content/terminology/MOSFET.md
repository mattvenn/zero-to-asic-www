---
title: "MOSFET"
date: 2020-11-12T17:39:16+01:00
description: "A MOSFET (Metal Oxide Semiconductor Field Effect Transistor) is the fundamental transistor used in modern chips. Learn how MOSFETs work, the difference between NMOS and PMOS, and how they are manufactured."
images: ["Construction-of-MOSFET.png"]
featured_image: "Construction-of-MOSFET.png"
faq:
  - q: What is a MOSFET?
    a: A MOSFET (Metal Oxide Semiconductor Field Effect Transistor) is a type of transistor used as a digital switch in integrated circuits. It is the basic building block of modern electronics and the most manufactured object in the world, with over 10^22 made since 1960.
  - q: What is the difference between NMOS and PMOS?
    a: In an NMOS transistor, the channel is formed by electrons (negative charge carriers) and the device is built on a P-type substrate. In a PMOS transistor, the channel is formed by holes (positive charge carriers) on an N-type substrate. PMOS transistors are typically 2-3x wider than NMOS to achieve equivalent drive strength because holes have lower mobility than electrons.
  - q: How does a MOSFET work?
    a: When a voltage is applied across the gate and body, an electric field forms in the channel region. This field attracts minority charge carriers to the channel, allowing current to flow between the drain and source. Removing the gate voltage collapses the channel and turns the transistor off.
video_id: IcrBqCFLHIY
---

A MOSFET is a type of transistor we can use as a digital switch.
The name stands for Metal Oxide Semiconductor Field Effect Transistor.
The first MOSFET was made in 1959 by Mohamed M. Atalla & Dawon Kahng.

The MOS part describes the gate structure, so the layering is 'metal' on top of an thin oxide layer, which lies on top of the (silicon) semiconductor channel. In practice the gate is typically polysilicon and not metal.  

The MOSFET eventually dominated [VLSI](/terminology/vlsi) chips 
due to it being easy to manufacture in volume and easy to miniaturise - at least to start with.

It has become the basic building block of modern electronics.

They are the most manufactured object in the world: 1.3×10^22 of them have been made between 1960 and 2018 - [Wikipedia](https://en.wikipedia.org/wiki/MOSFET)

# Simplified operation

![MOSFET Construction](/Construction-of-MOSFET.png)
Image is from [components101](https://components101.com/articles/mosfet-symbol-working-operation-types-and-applications)

When a voltage is applied across the gate and body, an electric field is formed in the channel.
This field attracts the charge carriers to the channel region where they can then work to conduct electricity.

In an N type MOSFET built on a P type substrate, the majority charge carriers are holes, and it's the minority carriers (the electrons) that get attacted to the gate and form the conductive channel between the drain and source. 

For a P type MOSFET, it's all reversed. The substrate is N, the majority carriers are electrons and the minority carriers doing the work are holes. 

The holes have less mobility than electrons, so you will typically see that for two matching N and P MOSFETs, the P type will need to have a larger (wider) channel, typically by a factor of 2 or 3 times. Standard cells often do not try to match P and N strengths because this will make the cell too big.

To get the right ratios of charge carriers, the silicon needs to be [doped](/terminology/doping).

This is a good video on the operating principles of a MOSFET by Veritasium:

{{< youtube IcrBqCFLHIY >}}

# Making a MOSFET

MOSFETs are made by using a [photolithograhic](/terminology/photolithography) process.
It is possible to make them in your garage, if it's well equipped!

{{< youtube s1MCi7FliVY >}}
