---
title: "Antenna Report"
date: 2021-03-30T12:31:35+02:00
featured_image: '/antenna-rule.png'
---

Antenna rules are part of the [DRC](/terminology/drc).

![antenna rule](/antenna-rule.png)

When the ASIC is being built up layer by layer, we have the gates of the MOSFETS built first. Then we use the metal layers to connect them into bigger blocks.
Between layers, the [wafer](/terminology/wafer) is often flattened. This process can induce enough electrical charge to destroy the connected gate.

After OpenLANE finishes, we have an antenna report in this file: ./reports/routing/antenna.rpt

The antenna report is a long collection of smaller reports like this:

    Net - active
      _1235_  (sky130_fd_sc_hd__inv_2)  A
    [1]  met2:
      PAR:    2.49  Ratio:    0.00       (Area)
      PAR:   12.66  Ratio:  400.00       (S.Area)
      CAR:    2.82  Ratio:    0.00       (C.Area)
      CAR:   14.39  Ratio:    0.00       (C.S.Area)

    [1]  met1:
      PAR:    0.30  Ratio:    0.00       (Area)
      PAR:    1.70  Ratio:  400.00       (S.Area)
      CAR:    0.33  Ratio:    0.00       (C.Area)
      CAR:    1.73  Ratio:    0.00       (C.S.Area)

    [1]  li1:
      PAR:    0.03  Ratio:    0.00       (Area)
      PAR:    0.03  Ratio:   75.00       (S.Area)
      CAR:    0.03  Ratio:    0.00       (C.Area)
      CAR:    0.03  Ratio:    0.00       (C.S.Area)

    [1]  M1M2_PR:
      PAR:    0.05  Ratio:    6.00       (Area)
      CAR:    0.10  Ratio:    0.00       (C.Area)

    [1]  L1M1_PR_MR:
      PAR:    0.06  Ratio:    3.00       (Area)
      CAR:    0.06  Ratio:    0.00       (C.Area)

We have the name of the net, in this case 'active'. 
Then 5 subsections related to the layers of the chips that each have a PAR or CAR value on the left and a ratio on the right.
PAR and CAR refer to Partial or Cumulative Antenna Ratio. 

From [this reference](http://free-online-ebooks.appspot.com/enc/14.17/lefdefref/PAE.html):

* A PAR tells you if any single metallization step is likely to inflict damage to a gate.
* A CAR adds the damages on successive layers together to accumulate them as the layers are built up.

If the value exceeds the ratio then it's a violation. However, most violations are not worth fixing unless they exceed the ratio by 2x.
For small runs we don't care too much if we have antenna rule violations because the failures caused by antennas is statistical. Maybe a few
chips of the 100 we get from the shuttle would be affected.
We can improve yield by making sure the antenna ratios are lower than the threshold given by the foundry.

Violating values are marked with *. So you can search for that in the report to find the violating values and nets.

OpenLANE automatically inserts antenna diode cells to protect nets.
One way to try to reduce antenna violations is to try a different insertion strategy. This configuration variable is called 

    DIODE_INSERTION_STRATEGY

You can find the definition here in the [OpenLANE docs](https://openlane-docs.readthedocs.io/en/rtd-develop/configuration/README.html).
