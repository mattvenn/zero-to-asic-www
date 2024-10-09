---
title: "Tiny Tapeout Goes Analog!"
date: 2024-04-20T13:34:51+02:00
tags: ["Tiny Tapeout", "analog"]
images: ["tt_paper.png"]
featured_image: "555_timer.jpeg"
---

[Tiny Tapeout 6](https://tinytapeout.com/runs/tt06/) marked a significant milestone by introducing support for analog and mixed-signal ASIC designs. This innovation opened up a world of possibilities for open-source chip development, building on the project’s success in the digital realm.

Prior to Tiny Tapeout 6, only digital designs were supported. However, the demand for analog and mixed-signal capabilities was evident. In an [interview](/post/carsten_wulff_interview), Carsten Wulff, Principal IC Scientist at Nordic Semiconductor, expressed his enthusiasm for the open-source ASIC movement, noting that a key strength of this approach lies in the mixed-signal domain. FPGAs and microcontrollers excel in digital applications, but mixed-signal designs on ASICs offer unique advantages and capabilities.

[Tiny Tapeout 5](https://tinytapeout.com/runs/tt05/) took the first step by including an experimental analog design submission, a ring oscillator and digital-to-analog converter (DAC) automatically placed and routed using experimental analog place and route tools. Building on this, Tiny Tapeout 6 embraced analog designs, as evidenced by the all-green analog tiles on the chip map.

![tt06 layout](/tt06_layout.png)

The shift to analog required significant infrastructure changes. Recognizing the risks associated with analog designs, such as potential short circuits, Tiny Tapeout 6 incorporated power gating for every design, enhancing safety and enabling more experimental submissions. To facilitate this, a robust power gate was implemented, leveraging a large, multi-fingered transistor design. 

{{< youtube _m_jK7twymM >}}

This move to analog wasn't just about expanding functionality; it also provided an opportunity to enhance existing features. While the power gating primarily aimed to mitigate risks associated with analog designs, it also benefited all projects on the chip by improving noise performance and signal integrity.

This development attracted a diverse range of analog projects. Impressive submissions included an [8-bit SAR ADC](https://tinytapeout.com/runs/tt06/tt_um_TT06_SAR_wulffern)  by Carsten Wulff and a [classic 555 timer](https://tinytapeout.com/runs/tt06/tt_um_vaf_555_timer) by Vincent Fusco. 

> It’s a really nice flow - I can’t tell you how excited I am about the fact that I can tape out some analog circuits for less than $1k now.
>
> Vincent Fusco.

The introduction of analog capabilities in Tiny Tapeout 6 represented a big step towards a more versatile and accessible open-source ASIC design ecosystem. As the project continues to evolve, I expect even more exciting analog and mixed-signal innovations to emerge from the Tiny Tapeout community. 

