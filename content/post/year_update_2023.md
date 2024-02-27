---
title: "Review of 2023 and aims for 2024"
tags: ["ASIC", "course" ]
date: 2024-01-17T10:47:24+01:00
images: ["year_update_2023.jpg"]
image_pos: 0% +5%
featured_image: "year_update_2023.jpg"
---

Hi and happy new year! Welcome to my year in review video of 2023. We’ll revisit the biggest moments of open source semiconductors, the goals I failed and those I met, and set some new ones for 2024!

{{< youtube RBdZX3fBYTM >}}

# So, let’s start with the biggest news of 2023. 

Last year saw the end of the Google sponsored lottery shuttles. We were expecting around another 8 shuttles for sky130, GF180 and the start of sky90. The last shuttle was GFMPW1, which closed late last year and the Sky 130 PDK is now in the safe hands of the [chips alliance](https://opensource.googleblog.com/2023/11/open-source-pdks-joining-linux-foundation-chips-alliance.html).

I think it’s fair to say that the free shuttles made a huge impact on the open source semiconductor community. It enabled hundreds of people to make their first silicon designs. Personally, I wouldn't have been so excited about designing my own ASICs without the possibility of getting them manufactured.

So I want to say thanks to everyone who made it possible!

While it’s sad to see it go, the good news is that we’ve had announcements of new open source PDKs and shuttle opportunities from [IHP](https://github.com/IHP-GmbH/IHP-Open-PDK/tree/dev), [Pragmatic](https://www.pragmaticsemi.com/newsroom/blogs/democratising-ic-design) and the [ICPS](https://github.com/mineda-support/ICPS2023_5) minimal fab. The news has also cemented my commitment to the Tiny Tapeout shuttle service - more on that later.

We also saw huge investments in the semiconductor industry with the EU and US chips act, putting 100B$ funding on the table. A large portion will go to a handful of very expensive factories and equipment, but it’s widely agreed that there will have to be a corresponding investment in training, given that thousands of people will be needed across the industry in the next 10 years.

The US national science foundation workshop report was published that covered a lot of ground, and one of the key recommendations was [making the industry more accessible.](https://www.zerotoasiccourse.com/post/nsf-report/) Open source tools were mentioned throughout as a way of achieving this, as well as a call for free tape outs and training for young people, starting in high school and continuing to university level.

Another great bit of news from 2023 was that the hold violation issues we struggled with in 2022 were resolved and all the Google MPW and Efabless chipIgnite shuttles from MPW6 onwards have been a breeze to bring up and get working.

# What else happened in 2023?

At the start of the year I continued working on the [MPW2](https://www.zerotoasiccourse.com/post/mpw2-submitted/) Zero to ASIC course group submission and also received [MPW3](https://zerotoasiccourse.com/post/mpw3/) chips. It was a mixed bag with some designs seeming to show they were working, but others not responding at all. The [GPIO](https://zerotoasiccourse.com/post/mpw1_silicon/) issue made it very hard to know if there was a problem with the design, or just an inability to get the pins setup correctly. Getting results out of MPW2 and 3 was a goal for 2023, so I think I mostly failed on that one.

![siliwiz](/siliwiz.png)

SiliWiz, the browser based tool I built with Uri Shaked was launched and we released a set of free lesson plans over at [tinytapeout.com](https://tinytapeout.com/siliwiz/). The lessons give a basic introduction to analog microelectronics, with parastics, voltage dividers, nmos, pmos and cmos inverters all covered.

I also did my first simple analog tapeout - a voltage divider made of polysilicon resistors. I had planned to add an analog section to the Zero to ASIC course, but I didn’t manage it. 

I wanted to tapeout on sky 90 and IHP 130, but neither of those happened. Another project that was cut by Google along with the lottery shuttle was development of Sky 90 - now in [archive mode on github](https://github.com/google/skywater-pdk-libs-sky90fd_fd_pr). IHP has done some research tapeouts with their open source PDK, notably [HEP](https://www.ihp-microelectronics.com/news/detail/hep), a security chip, but their public shuttle is not due to open until April 2024.

I also set a goal to help 1000 people tapeout in 2023, but I only managed about half of that. Still, helping 500 people make a tapeout isn’t bad!

More great news was that the issues we saw with MPW1 to 5 were finally put to rest by MPW6, with a [re-engineered Caravel by Efabless](https://www.youtube.com/watch?v=F377UouYr7Y). I received my MPW6 designs as part of their test run and that included the [instrumented adder project](https://www.zerotoasiccourse.com/post/instrumenting-hardware-adders/) I worked on with Teo. These chips were really easy to get working and I managed to measure the performance of the 5 different adder topologies we put on the chip. We’re now working on a paper for the I triple E - finally ending my 20 year streak of writing no papers whatsoever.

![adder](/adders_graph.png)

The open source tools have continued to improve, with hundreds of contributions from the community. To name a few - [OpenROAD](https://theopenroadproject.org/news/2023-has-been-a-year-of-rapid-expansion-and-innovation-for-theopenroad-project/) has continued to develop, [OpenLane2](https://github.com/efabless/openlane2) is in beta, and the [sv2v](https://github.com/zachjs/sv2v) system verilog parser getting a lot of love from the [openhardware group](https://github.com/openhwgroup/programs/blob/master/Project-Descriptions-and-Plans/CORE-V-180-MCU/CORE-V-180-MCU-TWG-20231023.pdf). Additionally, YosysHQ released a new [equivalence](https://yosyshq.readthedocs.io/projects/eqy/en/latest/) checking tool and started an open source [community spotlight](https://blog.yosyshq.com/tags/community-spotlight/) to showcase some of the exciting work going on.

We’ve also seen the continued growth of RISC five, with 8 RISC five CPUs taped out on Tiny Tapeout alone! CPUs are cool, but my favourite design of 2023 was the [very cool digital only mixed signal design](https://github.com/iic-jku/tt03-tempsensor) by Harald Pretl, Manuel Moser, and Michael Herber. It somehow convinced digital standard cells to work as a digital to analog converter to hold a MOSFET in its subthreshold region - I know right? 

We received Tiny Tapeout silicon and it was a huge relief to see it working! Just as well because we did the world’s first public silicon bringup and got some designs working live on stream. We planned to ship the assembled dev boards in 2023, but our PCBA schedule slipped - we expect to be shipping these boards any day now... ish.

{{< youtube psR2ax-LScc >}}

2023 also saw the rise of our new AI overlords, and I’m sorry to say that I’ve helped them invent their own brains by allowing the world’s first chat-gpt designed CPU on Tiny Tapeout. Hammond Pearce and Jason Blocklove also won the Efabless AI competition and I [interviewed them for the channel if you want to find out more](https://www.youtube.com/watch?v=6vC3t_soJok).

{{< youtube 6vC3t_soJok >}}

Tiny Tapeout 1, 2 and 3 all used my slow scanchain design, but we made a big improvement with Tiny Tapeout 4 by swapping it out for a fast multiplexer. We did an experimental test called TT3 point 5, and I’ve just received the chips. We’re measuring about 20ns latency between input and output, about thousand times faster than Tiny Tapeout 1 - turbo button engaged!

Another goal I met was making videos in cool places. It was an amazing experience to visit the Swiss light source and see inside [my first chips with their super powerful xray](https://www.youtube.com/watch?v=kTJZ3uTPhKw). I learnt a lot and it was literally illuminating to compare them to the files we sent for manufacture.

{{< youtube kTJZ3uTPhKw >}}

I also got to make my dream ‘[how chips are made](https://www.youtube.com/watch?v=aBDJQ9NYTEU)’ video by visiting IHP. It took a lot of organisation and work but I’m very proud of the results. As well as getting some amazing footage, I also got to work with an animator to illustrate what happens inside the machines. Thanks to IHP for letting me into your cleanroom - _I’ve never been more terrified of sneezing_!

{{< youtube aBDJQ9NYTEU >}}

There were some inspirational open source silicon events including the [free silicon conference](https://wiki.f-si.org/index.php/FSiC2023) in Paris and [ORConf](https://orconf.org/) in Munich. Both are highly recommended if you get the chance in the future and all the presentations were recorded and are available online. I also visited the US for the Hackaday supercon and we ran a [Tiny Tapeout workshop](https://makezine.com/article/maker-news/hackaday-supercon-2023-lights-up-pasadena/#h-the-workshops) where we had 30 people complete their first tapeout in just 3 hours! 

Open source tools definitely increase accessibility, but last year I also set a goal to make my course more affordable by [introducing a grant](https://www.zerotoasiccourse.com/post/ticket_grant/) that was awarded to 30 people.

Accessibility isn’t just about cost, it’s also about language. I listened to an [episode of the Embedded fm podcast](https://embedded.fm/episodes/465) with [Yanina Bellini Saibene](https://yabellini.netlify.app/), who cited a paper by [Amano](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002184) that found that non native English speakers can take 90% longer to read a scientific paper. This inspired me to renew my efforts on the Spanish translation of Tiny Tapeout, and I’m happy to say that we’ve recently [completed the translation of the SiliWiz](https://tinytapeout.com/es/siliwiz/introduction/) analog microelectronics tutorial. If you can help with translation into other languages, please get in touch.

Finally, on a light hearted note, I upgraded my wafer chain necklace with something a little more serious - a CNC machined necklace with LEDs driven by one of my own chips! [It’s certified open source hardware right down to the ASIC](https://www.zerotoasiccourse.com/post/asic-necklace/) and you can find out how we made it in this [video](https://youtu.be/QxjvktltZ9E). 

{{< youtube QxjvktltZ9E >}}

# 2024

So let’s move on to 2024, what’s going to happen and what are my new goals?

We’ll continue to see the tools improve and new shuttles supporting the open PDKs. I hope to see more mixed signal designs including some faster interfaces and maybe radio. 

We’re seeing a continued take up of open source tools in academia and I hope to see that extend to younger students as well.

It would be great to get a more solid and tested open source IP library that will make complex designs easier and faster to tapeout. I also think we’ll see more EDA tools available online from jupyter notebooks, github actions and web assembly like the [new fully online FPGA toolchain from Catherine “Whitequark](https://twitter.com/whitequark/status/1738722422646292688)”.

{{< twitter 1738722422646292688 >}}

As for my goals, even though I failed to get 1000 new people involved last year, this year I’m aiming for 2000! It’s going to be tough to reach, but if we fill every Tiny Tapeout shuttle, it’s possible.

We’re already [working with 10 universities](https://tinytapeout.com/#our-customers), but I want to grow this to 100 in 2024. If you’re in a university and you’re interested in easy and affordable silicon, then please get in touch!

I want to enable more mixed signal designs this year, as it’s a key advantage ASICs have over FPGAs. We plan to add analog support to [Tiny Tapeout](https://tinytapeout.com/) for the next shuttle in April, and I think that’s going to lead to a lot more people trying it out. Maybe I’ll finally add that section to the Zero to ASIC course - if doesn’t happen I’ll eat my hat!

I hope to re-visit [IHP](https://www.ihp-microelectronics.com/) while they’re manufacturing an open source design so I can see and share some of the metrology and inspection steps. I really enjoyed the on-site videos I made last year - if anyone’s out there working on something interesting and wants to invite me - please reach out!

![vga clock](/vga_clock.jpg)

Way back in 2021 I hoped to make my [VGA clock design into a product](https://www.zerotoasiccourse.com/post/vga_clock_pcb/) and donate the proceeds to the open source hardware association. This didn’t happen because the MPW1 chips needed so much infrastructure to get working. Now with the Tiny Tapeout 3 point 5 test chips, I have a few hundred chips that all run the clock perfectly and are easy to [mount onto boards](https://www.zerotoasiccourse.com/post/vga_clock_pcb_v2/). If you want to buy one of these unique, limited edition boards and support the open source hardware association, [sign up to the waitlist](https://docs.google.com/forms/d/1T6BmjGyFQyqTNji1qao1T61LZW5fL_B2eHlydXzalR4/edit).

# Thanks

And saving the most important thing till last, none of this would have been possible without help from people all around the world. 

Thanks to everyone who’s answered my questions or directed me to new tools or resources. 

Thanks to everyone who wrote documentation, opened issues or contributed to the open source tools. 

Thanks to everyone who helped me run a workshop. 

And thanks to everyone who bought a ticket to my course or did a tapeout with Tiny Tapeout.

In short, thanks to all involved - without you, the community, we wouldn’t be doing all of this cool stuff.

Have a great 2024!

