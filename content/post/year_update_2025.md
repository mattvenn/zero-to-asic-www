---
title: "Review of 2025 and goals for 2026"
date: 2026-01-04T14:24:44+01:00
tags: ["ASIC", "course" ]
images: ["keepcalmandmakeasics.jpeg"]
featured_image: "keepcalmandmakeasics.jpeg"
image_pos: 0% +50%
description: ""
---

For the first time, open silicon wasn’t just a niche experiment in 2025 - it was a real ecosystem spanning three fabs and thousands of designs. And then one company collapsed and hundreds of chips effectively disappeared overnight.

Efabless [going out of business](https://www.linkedin.com/posts/tinytapeout_were-very-sad-to-hear-that-efabless-corporation-activity-7301638170297720832-n7Ru) at the end of February hit the community like a hammer. They weren’t just an MPW provider - they offered hundreds of packaged parts with no NDAs, great pricing, and a level of openness that was rare in silicon. Losing them left hundreds of designs, including 500 Tiny Tapeout projects from [TT08](https://tinytapeout.com/chips/tt08/) and [TT09](https://tinytapeout.com/chips/tt09), seemingly stuck in fabrication limbo.

![keep calm and make asics](/keepcalmandmakeasics.jpeg)

The vacuum left by Efabless didn’t last long. Within months, new fabs and MPW options appeared - Tim Ansell launched[ wafer.space](http://wafer.space), Jeff and Mohammed (ex-Efabless) started[ ChipFoundry.io](http://ChipFoundry.io), and Cadence kicked off a SKY130 shuttle. At the same time, community infrastructure strengthened: OpenLane became LibreLane under FOSSi stewardship, and[ fossi-chat.org](http://fossi-chat.org) replaced the old Slack. 

Thanks to a combination of foresight and luck, Tiny Tapeout had already started working with IHP as part of the [SwissChips](https://swisschips.ethz.ch/) initiative, so we were able to combine most of the lost designs onto the absolutely packed [TTIHP25a](https://tinytapeout.com/chips/ttihp25a/). 

With the existential crisis out of the way, 2025 quietly turned into a very productive year.

### Best of 2025

#### Funding

Open source ASIC tooling now has serious funding backing it. A 40M euro EU funding opportunity for open source chips was announced in 2024 and the FOSSi foundation helped to create a [roadmap](https://fossi-foundation.org/resources/eu-roadmap) on how best to spend the money. 3 consortia were formed and created plans for analog, digital and workflow. We just heard that all have been approved for funding with work starting in 2026.


#### Zero to ASIC courses and Youtube channel

Teaching and sharing is always a bit of an experiment, and 2025 proved no different. NYU wanted to add practical microelectronics to their course, and I connected them up with the existing Zero to ASIC course curriculum. While updating the digital course, I switched the tools to Harald’s[ OSIC docker](https://github.com/iic-jku/IIC-OSIC-TOOLS), which is now my go-to recommendation: easy, cross-platform, and actively maintained.

I also started a[ weekly stream](https://www.youtube.com/playlist?list=PLyynFETmdQDT0iCaafHSQqluWHgDC6VL0). It was fun, but after 19 episodes I realized the stream was sucking all my energy without producing the depth I wanted. Ending it freed me up for more substantial interviews, tutorials, and site visits, and the channel still grew to[ 23k subscribers](https://www.zerotoasiccourse.com/post/20k-subs/), with highlights like[ Shafin Hossain on 180GHz chips](https://www.youtube.com/watch?v=RFPe4FT126M), the new course trailer and my [collaboration with Branch Education](https://www.youtube.com/watch?v=_Pqfjer8-O4) (2 million views!)

{{< youtube GjEnA3LUDdo >}}

#### Tiny Tapeout

Even with the bumpy start of the year, [Tiny Tapeout](https://tinytapeout.com/chips) sent over a thousand designs across 12 chips to 3 different fabs, including our first test chips for the GF180mcu process. Many of those designs came from high schoolers and students - attendees of my exciting and engaging Tiny Tapeout workshops.

![denmark workshop](/denmark_workshop.jpg)

At the same time those young people were making their first tapeouts, the Tiny Tapeout annual survey showed growing numbers of people from industry taking advantage of cheap, NDA free tapeouts.

![tt survey](/tt_survey_2025_background.png)

Metrics are nice, but designs are where the fun really starts.

### Inspirational designs

Long range radio communication was realised by a [WSPR transmitter](https://www.informatik.uni-wuerzburg.de/en/ce/news/single/news/tinywspr-generating-shortwave-signals-on-open-source-silicon/) - an innovative collaboration between JKU in Austria and JMU Würzburg in Germany.

Analog is crucial for advanced projects, but notoriously hard to teach and learn. Peter Kinget aims to solve that with [MOSBius](https://www.youtube.com/watch?v=abu3u6UX6wE), an analog FPGA aimed at experimentation. We’ve made a smaller version called [Mini MOSBius](https://www.tinytapeout.com/chips/ttsky25b/tt_um_mosbius) to be be included on all future Tiny Tapeout chips.

Designing chips can be overwhelming for beginners, what to make - where to start? That’s why we created the [RISCV peripheral challenge](https://tinytapeout.com/competitions/risc-v-peripheral/). The result was an amazing [RISCV microcontroller](https://www.tinytapeout.com/chips/ttsky25a/tt_um_tt_tinyQV) with [40 highly creative](https://docs.google.com/spreadsheets/d/1ru2YCSY_XCv5kk4FDyfl4eAzEzy9SP3UOAXtZt6OAMY/edit?gid=0#gid=0) peripherals - it was so big we even had to change the Tiny Tapeout chip architecture to fit it in!

We’ve all seen silicon doodles, the art that old school designers squeezed in at the edges of their chips. But what if a professional artist experimented with silicon? This year [Bleeptrack](https://bleeptrack.de/) started her exploration by [creating custom artwork](https://www.tinytapeout.com/chips/ttsky25a/tt_um_bleeptrack_cc2) and making 3 tapeouts. If you can’t wait for some decapped prints, then [grab some of these fantastic postcard sets](https://store.tinytapeout.com/products/Tiny-Tapeout-2025-Postcards-p786116359) showcasing some of the best art already created by the open silicon movement.

![postcard art](/postcard_art.jpeg)

With TT08 chips assumed lost to the silicon graveyard, it was fantastic news when ChipFoundry bought the Efabless IP, finished the packaging of CI2409 and sent us chips. It gave us the chance to judge the demoscene competition, which is close to complete as I write this. There are some mind blowing entries and I’m looking forward to sharing the winners soon. 

One of the lessons we learned through exploring other MPW options was how expensive packaging is. It can easily be the same price as the die itself! A cheaper method is Chip on Board (CoB), which we have continued to explore with this [stunning variant of the TT08 chips](https://store.tinytapeout.com/products/TT08-Development-Kit-Chip-on-Board-edition-p797024321).

![cob](/2025_cob.jpeg)

Apparently, the logical next step after chip-on-board is chip-in-orbit. After a fruitful collaboration with BME University in Hungary and their [HUNITY](https://gnd.bme.hu/hunity) PocketQube satellite platform. It was launched by SpaceX’s transporter 15 on November 28th. 

{{< youtube id=KVwK8GkDfow start=1813 >}}

Just a few days ago I was finally able to pick up the signal from the satellite as it passed overhead. The next step is to enable the experiments and start receiving data!

None of this happens in a vacuum - even when some of it literally leaves the planet, which brings me to the people who make all of this possible.


### Thanks

It would have been easy to lose momentum and wallow in despondency - I had more than one late night wondering whether we’d just watched years of work evaporate.

What stopped that happening was people showing up anyway. So I want to start with a big thanks to the Zero to ASIC, Tiny Tapeout and FOSSi teams and communities.

And then there’s the wider group who quietly made the impossible possible this year:

* [SwissChips](https://swisschips.ethz.ch/) - providing free tapeouts to Swiss students and funding IHP development work.
* [Texplained](https://texplained.com/) - providing high quality [chip imaging](https://tinytapeout.com/decap/tt07) and reverse engineering services.
* [IHP](https://www.ihp-microelectronics.com/) - providing access to open source silicon manufacturing here in Europe, and letting me interview their scientists and film in their cleanroom.
* [ChipFoundry](https://chipfoundry.io/) - providing access to SKY130 and sponsoring the early bird Tiny Tapeout discount.
* [Wafer.Space](https://wafer.space/) and Tim Ansell for access to GF180mcu and sponsoring Tiny Tapeout.
* [Tillitis](https://www.tillitis.se/) and [Wit](https://www.wit.com/) for sponsoring development work to support GF180mcu on Tiny Tapeout.
* [Synopsys](https://www.synopsys.com/) and Patrick Haspell for early access to GF180mcu and sponsoring Tiny Tapeout workshops. 
* A collaboration with [Digilent](https://digilent.com/) allowed me to [subsidize 75% of the cost of the AD3](https://www.zerotoasiccourse.com/post/test-equipment-grant-2025/), an excellent device for people to get started with real world, practical electronics experiments. 

### Goals for 2026

* My focus this year is to see the 1 student 1 chip initiative spread from SwissChips across Europe. If you’re a student then you should be able to get a free tapeout.
* This year we will enable workshop attendees to test their designs on an FPGA. Development boards have already been designed and manufacture is currently under way.
* Demand for Tiny Tapeout workshops is so high, I want find people to lead them and also to try an online version. Expect the first online versions to happen early in 2026, timed to hit the TTSKY26a and TTIHP26a tapeouts.
* My newsletter is due an update, and I’m also going to commit to sending an update at least once a month. If you want to follow along, [sign up here](https://zerotoasiccourse.com/newsletter/).

2026 is going to bring more accessibility, better tools, more first-time designers, and lots of surprises from the community!

