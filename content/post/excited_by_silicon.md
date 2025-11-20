---
title: "Excited by silicon!"
tags: ["essay", "ecosystem"]
images: ["excite/wafer.png"]
featured_image: "excite/wafer.png"
date: 2025-11-20T11:45:52+01:00
---
I was recently asked what excites me most about the exploding open-source silicon ecosystem. Honestly? It depends who's asking.

For one person I might talk about [Basilisk](https://arxiv.org/pdf/2505.10060) - the PULP team's seriously impressive Linux-capable RISC-V core. For another, maybe the new GF180mcu MPW from [Wafer.Space](http://wafer.space), or the millions in funding finally flowing into improving the tools. And then there are the community [events](https://fossi-foundation.org/events) that make the whole thing feel electric.

There's a lot happening at once, so to make sense of it, let me break it down into [Foundries](#foundries), [Funding](#funding), [Tools](#tools), [IP](#ip), [Community](#community-and-events) and the [Future](#looking-to-the-future).

### Foundries

Although open source EDA has a long history, it wasn't until the [opening of Skywater PDK in 2020](https://www.zerotoasiccourse.com/terminology/shuttle/) that we were able to get our designs manufactured. Not only does that make things much more exciting, without being able to test and measure designs, we can't close the learning loop, iterating and improving.

After the Google sponsored Sky130 MPW had run for a couple years, the GF180mcu PDK and shuttle arrived at the end of 2022. Unfortunately when the [Google sponsorship ended](https://opensource.googleblog.com/2023/11/open-source-pdks-joining-linux-foundation-chips-alliance.html), so did access to GF180mcu, with Efabless only supporting SKY130 through their ChipIgnite service.

Only having one supplier makes anyone in manufacturing nervous, and it was certainly something I was concerned about. If we lost access to SKY130, would the ecosystem survive?

[![gf180 wafer](/excite/wafer.png)](https://wafer.space)

So it was a comfort to see [IHP](https://www.ihp-microelectronics.com/services/research-and-prototyping-service/fast-design-enablement/open-source-pdk) open sourcing their 130nm PDK in 2023. As IHP currently holds the record for world's fastest transistors, it's quite an interesting PDK to have access to!

In partnership with [Swiss Chips](https://swisschips.ethz.ch/), Tiny Tapeout was able to start work on porting infrastructure and preparing to run a multi-project chip in late 2024.

When Efabless shut down in March 2025, it felt like an earthquake through the whole ecosystem. We were left with a lot of uncertainty around whether we'd continue to be able to access SKY130, who would support OpenLane, and what would happen to the chips that were halfway through being manufactured.

While the closure left many wondering how the ecosystem would survive, new initiatives soon emerged to restore access. A few months later, Cadence and [ChipFoundry](http://chipfoundry.io) were both offering SKY130 access, and we also heard about a potential new GF180mcu MPW from [Wafer.Space](http://wafer.space).

So now at the end of 2025 we have 3 open source PDKs, and you can order chips from any of them!

### Funding

In Europe we saw the [Importance of Open-Source EDA Tools for Academia](https://open-source-eda-letter.eu/) and the [Open-Source Chips for Europe](https://open-source-chips.eu/) open letters, with thousands of signatories.

These helped to spur the creation of a 20M€ [Horizon funding project](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/HORIZON-JU-CHIPS-2025-IA-EDA-two-stage?isExactMatch=true&status=31094501,31094502,31094503&callIdentifier=HORIZON-JU-CHIPS-2025-IA-EDA-two-stage&order=DESC&pageNumber=1&pageSize=50&sortBy=startDate) that's currently in progress and should result in a range of improvements to the digital and analog tools.

In the US, things have been on shaky ground with the new administration but the NSF have [recommended open source EDA](https://www.zerotoasiccourse.com/post/nsf-report/) for helping with workforce development.

China is in the process of opening a [55nm PDK, with the ICSprout](https://github.com/openecos-projects/icsprout55-pdk) project. Already hundreds of Chinese students are creating RISCV multi-project chips with homegrown open source EDA tools.

Swiss Chips, [Tillitis](https://www.tillitis.se/) and [Wit](https://www.wit.com/) have together funded Tiny Tapeout to port their multi-project chip infrastructure to IHP130 and GF180mcu.

### Tools

OK, we have money and we can spend it on chips, but can we ~~boil them in acid~~ make better chips? Let's take a look at some recent improvements and new tools.

One of the most exciting developments has been the work done to integrate [OpenEMS](https://github.com/VolkerMuehlhaus/openems_ihp_sg13g2) with the IHP130nm process. OpenEMS is a full wave solver, which means the magnetic field is also taken into account. Important for very high frequency work this tool has enabled some [impressive GHz designs to be designed and fabricated](https://youtu.be/RFPe4FT126M?si=t-OT9lIZAYqjBDVq).

* [OpenROAD quality of results](https://theopenroadproject.org/wp-content/uploads/2025/02/OpenROAD-in-2024_-Expanding-adoption-sustaining-ecosystems-improving-PPA.pdf) has continued to improve and is seeing commercially meaningful use cases.
* Mixed signal cosimulation is now available with the [integration between Verilator and NGSpice](https://ngspice.sourceforge.io/docs/others/Verilog-CoSim.pdf).
* The [Surfer](https://surfer-project.org/) wave viewer continues to improve and is growing in adoption.
* [SiliWiz](https://app.siliwiz.com/) has enabled anyone with a web browser to explore physical devices with web based transistor modelling.
* The [Tiny Tapeout 3D viewer](https://gds-viewer.tinytapeout.com/?model=https%3A%2F%2Fshuttle-assets.tinytapeout.com%2Ftt07%2Ftt_um_rnunes2311_12bit_sar_adc%2Ftt_um_rnunes2311_12bit_sar_adc.oas&process=SKY130) has become the standard way to visualise GDS and recently got some new features including cross section views, animated rotation and layer expansion.
* Alex created a [fantastic 3D simulator](https://znah.net/tt09/) that shows digital designs running in the browser.

[![simulation](/excite/simulation.png)](https://znah.net/tt09/)

Open tools allow easier integration of machine learning, and Andrew Kahng has continued to [make improvements with synthesis and routing](https://arxiv.org/pdf/2506.08332?).

It's not only software that has taken steps forward, Andrew ‘Bunnie' Huang also released his [security focussed IRIS setup](https://www.bunniestudios.com/blog/2024/iris-infra-red-in-situ-project-updates/) that allows non destructive in-situ inspection of chips and [the hacker fab](https://docs.hackerfab.org/home) has been building a library of hacker tools for DIY silicon.

[Texplained](https://texplained.com/) have also partnered with Tiny Tapeout to offer [high resolution scans](https://tinytapeout.com/decap/tt06) and electron micrographs of recent chips.


### IP

I'm often asked to predict when we'll see open source silicon in products. My answer is that we won't see open source chips at volume until there's a large enough library of quality, silicon proven IP.

For now, let's ignore the somewhat contradictory ‘open source intellectual property' and consider IP to mean ready to use, open source, modular blocks that are well documented and silicon proven.

Most commercial chips are built by buying ready to use IP like ADC, DAC, PHYs etc. Without them, the job is just too large.

Progress has been slow but steady, and we can expect to see more and higher quality IP as the community grows. One thing we need to ensure is continued, reliable and ideally fast MPW services so that authors can test and refine their projects.

We already have quite a large library from the 1000+ projects taped out over at the [Tiny Tapeout Index](https://github.com/TinyTapeout/tinytapeout-index). There you can search by author, title, description, and poll the [feedback](https://app.tinytapeout.com/api/shuttles/tt08/feedback) to check the design's test status.

Sylvain Munaut has been busy working on ROMs and SRAMs that have been utilised by projects like the [uLinux capable RISC-V](https://tinytapeout.com/chips/ttsky25b/tt_um_kianv_rv32_regfile)  and the [TV-B-Gone](https://tinytapeout.com/chips/ttsky25b/tt_um_tv_b_gone_rom).

We also have a growing collection of analog IP, covering ADC, DAC, bandgap, opamps etc. For a list of all Tiny Tapeout analog designs up to September 2025 check [here](https://gist.github.com/urish/34291f0533671b9de7c19736adb774f4). One notably missing element is non volatile memory.

I [predicted that 2025](https://www.zerotoasiccourse.com/post/year_update_2024/) would be the year when we'd start seeing more radio projects, so it's been satisfying to see Sylvain's [SDR](https://hackaday.com/2025/02/11/a-tiny-tapeout-sdr/) experiment and a [WSPR transmitter](https://tinytapeout.com/chips/ttsky25b/tt_um_TinyWhisper) from a Austrian university collaboration getting taped out.

[![WSPR layout](/excite/wspr.png)](https://tinytapeout.com/chips/ttsky25b/tt_um_TinyWhisper)

Having said that we won't see commercial chips until we have more IP, I think there are some exceptions: security and retro. The [HEP](https://www.ihp-microelectronics.com/news/detail/hep) and [Open Titan](https://www.electronicdesign.com/blogs/the-briefing/article/55038396/electronic-design-open-for-business-open-source-silicon) security implementations and the open source [Z80](https://hackaday.com/2024/04/28/the-z80-is-dead-long-live-the-free-z80/) replacement are all good candidates.

### Community and Events

Open Source doesn't work without community, and we have a solid foundation that's been growing steadily over the years.

Following the Efabless closure, the [FOSSi foundation](https://fossi-foundation.org/) set up [fossi-chat.org](fossi-chat.org), which has become the central place to chat about open source EDA and silicon.

The recent Tiny Tapeout user survey showed not just amateurs and academics, but a growing proportion of industry using the platform. Tiny Tapeout's dedicated [community on Discord](https://tinytapeout.com/discord) now has over 3000 people.

[![survey](/excite/survey.png)](https://docs.google.com/forms/d/e/1FAIpQLSdHB1XBgVXBLGT6KdkQIzfJFvYLMbIrvoG2VuOYp5Dnm3seKw/viewform?usp=preview)

The [demoscene](https://tinytapeout.com/competitions/demoscene/) and [RISCV](https://tinytapeout.com/competitions/risc-v-peripheral/) competitions were a great success in bringing people together and resulted in some very creative and impressive projects.

We saw the first real silicon art from [Bleeptrack](https://bleeptrack.de/), who turned her generative skills to this very unusual [artistic medium](https://gds-viewer.tinytapeout.com/?model=https%3A%2F%2Fshuttle-assets.tinytapeout.com%2Fttihp25b%2Ftt_um_blptrk_weaving01%2Ftt_um_blptrk_weaving01.oas&process=SG13G2).

Just around the corner we have the first [open source silicon in space](https://www.linkedin.com/feed/update/urn:li:activity:7396173179930619904/), with a partnership between BME university in Hungary and participants of Tiny Tapeout 6. The chip will ride on a [pocketqube](https://en.wikipedia.org/wiki/PocketQube) satellite in low earth orbit and run a series of experiments testing the chip.

[![rocket](/excite/rocket.png)](https://nextspaceflight.com/launches/details/7138/)

On social media the most active place at the moment seems to be LinkedIn, with many people posting their projects and showing off working silicon.

Lastly, physical events have been a fantastic way for the community to come together and get to know each other IRL. FOSSi foundation [ORConf (EU) and Latchup (US)](https://fossi-foundation.org/events) as well as the [Free Silicon Conference](https://wiki.f-si.org/index.php/FSiC2025) have all been excellent events with hundreds of talks and presentations.

### Looking to the future

Andrew ‘Bunnie' Huang is a legendary hacker who started in silicon but left the field because the closed, proprietary nature of the industry put him off.  In his recent [presentation](https://www.youtube.com/watch?v=pxQCApAAT0s) for Teardown, he announced that now is the time he'll be returning to his roots and getting involved.

Bunnie argues that open source becomes dominant when modularization increases, costs drop by 10× and the community creates knowledge faster than proprietary institutions. All those conditions are now true in silicon and as a result we can expect a huge shift in the coming years; a growing library of open IP, more niche, custom silicon and hardware as a collaborative platform.

It's now more exciting than ever to get involved in the world of open source silicon!

Thanks for reading! Did I miss anything? Let me know in the [contact form](/contact-form).
