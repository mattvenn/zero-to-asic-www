---
title: "MOSFET"
date: 2020-11-12T17:39:16+01:00
images: ["Construction-of-MOSFET.png"]
featured_image: "Construction-of-MOSFET.png"
---

A MOSFET is a type of transistor we can use as a digital switch.
The name stands for Metal Oxide Silicon Field Effect Transistor.
The first MOSFET was made in 1959 by Mohamed M. Atalla & Dawon Kahng.

The MOSFET eventually dominiated [VLSI](/terminology/vlsi) chips 
due to it being easy to manufacture in volume and easy to miniaturise - at least to start with.

It has become the basic building block of modern electronics.

They are the most manufactured object in the world: 1.3×10^22 of them have been made between 1960 and 2018 - [Wikipedia](https://en.wikipedia.org/wiki/MOSFET)

# Simplified operation

![MOSFET Construction](/Construction-of-MOSFET.png)
Image is from [components101](https://components101.com/articles/mosfet-symbol-working-operation-types-and-applications)

When a voltage is applied across the gate and body an electric field is formed in the channel.
This field attacts the charge carriers to the channel region where they can then work to conduct electricity.

In an N type MOSFET built on a P type substrate, the majority charge carriers are holes, and it's the minority carriers (the electrons) that get attacted to the gate and form the conductive channel between the drain and source. 

For a P type MOSFET, it's all reversed. The substrate is N, the majority carriers are electrons and the minority carriers doing the work are holes. 

The holes have less mobility than electrons, so you will typically see that for two matching N and P MOSFETs, the P type will have a larger channel.

To get the right ratios of charge carriers, the silicon needs to be [doped](/terminology/doping).

This is quite a good video on the operating principles of a MOSFET:

{{< youtube Bfvyj88Hs_o >}}

# Making a MOSFET

MOSFETs are made by using a [photolithograhic](/terminology/photolithography) process.
It is possible to make them in your garage, if it's well equipped!

{{< youtube s1MCi7FliVY >}}
