---
title: 'Chip On Board'
date: 2024-12-12T14:36:11+01:00
tags: ['ASIC', 'MPW']
images: ['cob.jpg']
featured_image: 'cob.jpg'
custom_summary: |
    Our first COB (chip on board) chips are working! This has been a dream of mine for a few years, and it’s finally a reality!

    We're used to seeing chips as little black boxes on a circuit board, but what's inside?

    The first part of the journey started with Tamas creating this cool circuit board.
---

Our first COB (chip on board) chips are working! This has been a dream of mine for a few years, and it’s finally a reality!

We're used to seeing chips as little black boxes on a circuit board, but what's inside?

![COB](/cob.jpg)

The first part of the journey started with Tamas creating this cool circuit board.

![layout](/cob_layout.jpg)

Then Stuart visited a wire bonding ‘factory’ while he was in Shenzhen. It’s nothing like you might imagine. The machines are old and dusty and practically no effort was made on keeping the room clean. The dies are actually pretty hardy, as they’re covered in a thin layer of glass to protect them. There are little holes in this passivation layer that expose the bond pads.

![cob setup](/cob_setup.jpg)

After the dies are glued onto the circuit boards and the machines are set up, the bonding happens automatically. 

![bonding](/cob_bond.jpg)

After the wires have been bonded, they’re protected with a blob of epoxy, or ‘glob top’. Normally this is black, but we asked for transparent. I’ve always liked the idea of having the chip exposed and visible, I think that helps people to understand what’s inside the little black boxes we’re used to seeing on circuit boards.

The chip we used was one we submitted to the [Google MPW 7 lottery back in 2022](https://www.zerotoasiccourse.com/post/mpw7_submitted/). It was one of the few times we received both QFN packaged chips and bare dies. It contains 7 designs from members of the Zero to ASIC digital course.

![mpw7](/mpw7_multi_macro.png)

After plugging it into a tester board, and loading a ‘blink’ program I can see the chip is working!

![cob working](/cob_working.jpg)

I would love to have this as an option for [Tiny Tapeout](https://tinytapeout.com), but it required getting hold of bare dies, which isn’t an option for us at the moment. The long wires also affect the performance of the chip, because they add unwanted inductance.

Although the chips work, I don't have plans to provide them with a demoboard needed to power them up and get a design working. They're more intended as nice gifts or prizes for people. 

For the rest of the photos and lots of videos, check out [Stuart’s album](https://photos.google.com/share/AF1QipPvHwLy1QsDnQShTJTSbDiQ6kdWi2avBRBA2i7dXp9sm7P3BI3qjYkOHsiN2lh8zg?key=TFBDZ09Kd18zS1VURjRadEc1UUFQRDExSWxpakJ3).