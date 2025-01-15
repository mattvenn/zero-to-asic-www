---
title: "Review of 2024 and aims for 2025"
date: 2025-01-14T10:47:24+01:00
tags: ["ASIC", "course" ]
images: ["year_update_2024.png"]
featured_image: "year_update_2024.png"
image_pos: 0% +10%
custom_summary: |
    Wow what a year! In this post I’m going to look back over 2024 and share some of my highlights and the goals I met and those that I failed. Then I’ll share my ambitions and predictions for 2025.

    With all the open source tapeouts, events, workshops and news, there’s a ton to cover - so let’s jump in!

    I aimed for 2000 new people to get started with open source silicon via my courses and tiny tapeout.
---

Wow what a year! In this post I’m going to look back over 2024 and share some of my highlights and the goals I met and those that I failed. Then I’ll share my ambitions and predictions for 2025.

With all the open source tapeouts, events, workshops and news, there’s a ton to cover - so let’s jump in!

{{< youtube iNPxTtRB-Hg >}}

## 2024 Goals

### More people

I aimed for 2000 new people to get started with open source silicon via my courses and tiny tapeout.

* We had 600 new people tape out on tiny tapeout 6 to 9,
* 171 people joined my courses,
* and 250 people joined tiny tapeout workshops.

So that’s about 1000 people, not bad but not 2000. I did get 93 thousand new youtube viewers though!

### Universities

Last year I said I wanted to grow from working with 10 universities to 100, but that didn’t happen. We grew to 21 universities, mostly American, but we also added some from Latin America, Europe, India, Sri lanka and the Philippines. These are the universities that are making big or repeated orders.

If you count just making a few tapeouts, then we’ve had around 50 orders made from .edu addresses.

Still quite a long way to go!

### Enable mixed signal

I wanted to enable more people to try analog and mixed signal, and this is one I’ve definitely achieved. We added mixed signal support to Tiny Tapeout and enabled nearly a hundred analog projects. It was such a highlight I’ll come back to this later.

### Open source silicon product

I also wanted to create an open source silicon project and sell it in support of [OSHWA](https://oshwa.org/). To be honest I’ve had this goal right from the start. But I never got enough working chips with a good enough design on them. That changed with our experimental Tiny tapeout 3.5 shuttle. I put my vga clock on it and we had quite a few chips left over. The kit is now available in the [Tiny Tapeout store](https://store.tinytapeout.com/) and I’ve already donated $500 to OSHWA from sales. There are 6 kits left, and we also have hats and some rare Google MPW dies mounted in epoxy cubes if you want to support my mission.

## 2024 highlights

* Getting into analog and mixed signal was a really satisfying experience. As well as learning a lot myself and taping out my first designs, we also enabled a lot more people to get involved.
* The first analog design on Tiny Tapeout was on TT05 with a ring oscillator and a DAC from Harald Pretl. I want to say a big thanks to Harald for being our analog adviser and also for helping me out with my new course. I put a [simple voltage divider](https://tinytapeout.com/runs/tt05/tt_um_matt_divider_test) and the biggest capacitor I could fit, which was a princely 10pF. We enabled analog support officially on Tiny Tapeout 6 and 92 analog slots have been used over the 4 tapeouts in 2024. I taped out a DAC, a couple of different oscillators, a band gap reference, and at last my first GDS art!
* I also created the [new Zero to Asic analog course](https://zerotoasiccourse.com/analog/), which already has 50 members. The first designs were taped out on tiny tapeout 6 by my awesome beta testers and we’re just starting to get results as people receive their boards. I’m really looking forward to seeing what people come up with in 2025.
* Harald also created a [new analog circuit design course](https://iic-jku.github.io/analog-circuit-design/), and all the materials are published and open source. Definitely check that out if you’re interested in analog circuit design.
* I wrote and published my[ first paper for the IEEE solid state circuits magazine](https://www.zerotoasiccourse.com/post/ieee_tinytapeout_paper/) and It was way more work than I imagined! but it’s quite a nice milestone and great to have something that people can cite in their publications. Thanks to everyone who helped out with that, especially Gareth Halfacree for the technical editing. 
* Last year We did 4 Tiny Tapeout workshops with about 250 people attending in total. Every time we run them they get a bit better. The ones in the US were the biggest yet, and they were also the debut of my semiconductor based music! Thanks to all the teaching assistants and organisers for making them run so smoothly.
* There were also the conference events, including FOSSi latch up and ORConf, and the Free silicon conference. I was able to attend and speak at [ORConf](https://www.youtube.com/watch?v=DoFL6PPlErw) and the [free silicon conference](https://www.youtube.com/watch?v=O6-3Dfwfp5Q) and they were as good as always. Definitely try to attend one of these events if you can, and even better apply to present your own work! I also really enjoyed attending the ETH Zurich summer school and learnt a lot from the keynote speakers.
* If you’re unable to attend these conferences, then there’s also things happening online, like the [YosysHQ user groups](https://blog.yosyshq.com/yug/). We ran 5 last year covering System Verilog, hardware security, fpgas and more. Join the YosysHQ mailing list for news of upcoming events.
* Another big highlight from FOSSi was publishing an open letter on the [Importance of Open-Source EDA Tools for Academia](https://open-source-eda-letter.eu/ ). It was signed by over 500 academics and shows the strong demand for using open source EDA in education. 
* FOSSi was also a major contributor to the [Recommendations and Roadmap for Open-Source EDA in Europe](https://fossi-foundation.org/resources/eu-roadmap), published in November. The document will be used by the EU to allocate around 40 Million euros of funding to develop open source EDA tooling and tapeouts. A lot of people contributed to that, and I want to say a special thanks to Stefan Wallentowitz for leading the project.
* FOSSi director Olof Kindgren also reached a major milestone when his “LED to believe project” [hit 100 boards](https://fossi-foundation.org/blog/2024-02-13-ecl71#project-led-to-believe-breaks-through-the-100-fpga-board-milestone). The project aims to provide LED blinking examples for every FPGA dev board. It’s just a shame it hasn’t won any awards yet!
* Over on Youtube I saw more people publishing great semiconductor content. In particular Breaking taps made a video on [speed running the last 30 years of lithography](https://www.youtube.com/watch?v=RuVS7MsQk4Y), Projects in Flight released a [whole series of videos about DIY semiconductors](https://www.youtube.com/@projectsinflight/videos), and Pat Deegan was interviewed by Robert Ferenac about the [open source analog microelectronics flow.](https://www.youtube.com/watch?v=caXwuuXSB-A)
* Talking of DIY semiconductors, this year has seen a lot of progress by hackerfabs. [Hackerfabs](https://docs.hackerfab.org/hacker-fab-space) aim to Make integrated circuit prototyping as fast as 3D printing with open source hardware. I was lucky to meet some of the people involved at the Stanford Tiny Tapeout workshop. And if you want to try making your own transistor, Check out their website and see if you have one nearby to visit.
* Moving up to slightly bigger fabs, we saw another round of the minimal fab competition. The minimal fab aims to very rapidly prototype on very small wafers. I [spoke about it with Leo Moser](https://www.youtube.com/watch?v=JHnb7GbcRW0) who won one of the prizes earlier this year. 

{{< youtube JHnb7GbcRW0 >}}

* Taking Another step up in fab size and we get to iHP. This is the foundry I visited to make my tour video in 2023. In 2024 they ran their first open source tapeouts. One design I want to call out in particular is a Linux capable SoC called Basilisk by the Pulp team at ETH Zurich. They were able to achieve competitive performance with OpenROAD and [published their results](https://arxiv.org/html/2405.03523v1).
* Tiny Tapeout also did 2 experimental tapeouts in partnership with Swiss Chips and iHP. The first one was just taking our first steps with a new process. It was the first time we created our own padframe, which feels like an important step in being a semiconductor company.  For the [2nd experiment](https://tinytapeout.com/runs/ttihp0p2/) we ported the tiny tapeout infrastructure and then filled it with designs from the community. Thanks to Sylvain, Tamas, ETH Zurich and the team at iHP for helping make that happen.
* Moving on to Skywater tapeouts, we did another 4 Tiny Tapeouts this year, all made possible by [Efabless](https://efabless.com). Big thanks to the team at Efabless for the tools, the support and the tapeouts! tiny tapeout 6 was our best shuttle to date, with almost all the area used, and then we smashed a new record with tiny tapeout 9 - selling the most devkits of any shuttle we’ve run so far. 
* There’s always so many awesome projects it’s hard to choose, but here’s just a few of my favourites:
    * We saw at least 13 RISC-V CPUs taped out last year including an incredible effort by Hirosh with his [micro Linux capable SoC on Tiny Tapeout 5 and 6](https://tinytapeout.com/runs/tt06/tt_um_kianV_rv32ima_uLinux_SoC). I was able to boot linux and run some commands on custom silicon! Amazing!
    * As an aside, It’s been a very interesting year for RISCV with the Raspberry Pi 2350 chip including 2 RISCV cores and the ten cent CH32V003 microcontroller growing in popularity.
    * Last year it was sad to see the classic Z80 discontinued, but ReJ saved the day with an [open source version using 4 tiles on TT 07](https://tinytapeout.com/runs/tt07/tt_um_rejunity_z80). I interviewed Rej about it [on the channel](https://www.youtube.com/watch?v=GI1e22A2J3U). He’s a fan of classic computers, and has just put an [Atari 2600 with games on TT09](https://tinytapeout.com/runs/tt09/tt_um_rejunity_atari2600).
    * Among some excellent analog designs we had a [SAR ADC](https://tinytapeout.com/runs/tt06/tt_um_TT06_SAR_wulffern) from Carsten Wulff, university professor and principal IC scientist at Nordic Semi. We [talked about it on the channel](https://www.youtube.com/watch?v=ypXynGz8Heo) and he’s just received his board for testing.
    * Vincent Fusco taped out a [555 timer on TT06](https://tinytapeout.com/runs/tt06/tt_um_vaf_555_timer), and we’ve just seen it working - what a beauty!
    * Sylvain Munault finally got some timeout from developing TT infrastructure to try out his ideas for small ROMS. You can follow his progress [on his own channel](https://www.youtube.com/watch?v=MlqDm_Kg0u8).
    * TT08 featured the first [demoscene](https://tinytapeout.com/competitions/demoscene/) competition, with about 30 entrants. A lot of the entries really blew my mind! I remember faking up the invitro, and thinking even doing something like that would be pretty hard. Then we saw some absolute amazing entries from the contestants. We expect TT08 back in March, so stay tuned for the judging!
    * Finally, I loved this cellular automata design by Alexander Mordvintsev. Not just because I’m a cellular automata fan, but because he put together this [amazing online simulation](https://znah.net/tt09/) you can play with. It’s so cool to see how the design is working when you slow it down. And when you speed it right up you can see the graphics being built up line by line.
* Ever since I started thinking about how to make ICs more transparent in their operation, I thought it would be cool to do a chip on board with a clear epoxy. It took a lot longer than I expected but finally we got some Zero to ASIC course chips [mounted and wirebonded in Shenzhen](https://www.zerotoasiccourse.com/post/cob/) and they work!
* Transparent epoxy is great but you still can’t see inside the chip, and that’s another thing I’ve wanted to include in the Tiny Tapeout datasheets. So I’m very happy to announce that we have now partnered with [Texplained](https://www.texplained.com/) to do our decapping and imaging. These images are from TT06 and TT07 and they’ll be slicing up all our future chips too!

{{< youtube GI1e22A2J3U >}}

## 2025 goals

*  Well I want to work with 100 universities. OK, so this is the same number I said last year, but now I just need another 80! I have to admit this remains a very ambitious goal, but I am seeing more and more universities revitalise their microelectronics programs, and an undergraduate tapeout is very compelling!
* I want to get 2000 more people involved in open source silicon. Again, the same number as last year. I think I can make up the numbers if I start running more, larger workshops.
* Talking of workshops, I’d like to build up to one a month. I already have 4 booked for 2025 and I’m looking for partners who want to try running some hybrid events. I want to find a way to keep the same level of fun and engagement but without all the travel. 
* I want to continue to make it even easier to tapeout for beginners like high school students. One of the projects we’re working on with Efabless is a way to test Wokwi designs on an FPGA. Once that’s ready, the next step will be a single button to create the GDS ready for submission.
* Now that access to silicon is so much easier, I really want to see more people doing GDS art. We’ve all seen silicon doodles by the chip’s designers, but what if artists got involved? We’ve seen some amazing work from the Pulp team, but I want to push this further by funding some silicon art this year. Stay tuned for an imminent announcement on that front!
* 2025 is the year we’re finally going to see radio on Tiny Tapeout. I’m pretty sure we already have a few unintentional transmitters, but it’s going to need a bit more effort to make a receiver.  To count this as a win I’d want a pair of projects that can send and receive data with just a couple of short wire antennas.

---

So, thanks for reading, and for all your support over the last year. I may be the beautiful face, but this is truly a team effort - from the people developing the tools to the people making their first tapeouts!

If you want to stay up to date with all things open source silicon, sign up to my [newsletter](https://www.zerotoasiccourse.com/newsletter/)!

