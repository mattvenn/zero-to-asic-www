---
title: "STA"
date: 2020-11-12T17:43:21+01:00
description: "Static Timing Analysis"
featured_image: "/sta.png"
---

Static Timing Analysis helps us to understand how fast we can expect our chip to run.

[OpenLane](/terminology/openlane) uses a tool called [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA)
It's job is to analyse the 'critical paths' in the design and then work out how long it will take those paths to propagate a signal.

After OpenLane finishes, we get a report from OpenSTA: reports/synthesis/opensta.min_max.rpt

The required timing is set in the OpenLane config file. By default it's 10ns, which means we are targetting a clock frequency of 100MHz.

The report shows that timing is met, so the design should run fine at 100MHz.

    Startpoint: _357_ (rising edge-triggered flip-flop clocked by clk)
    Endpoint: _357_ (rising edge-triggered flip-flop clocked by clk)
    Path Group: clk
    Path Type: min

      Delay    Time   Description
    ---------------------------------------------------------
       0.00    0.00   clock clk (rise edge)
       0.00    0.00   clock network delay (ideal)
       0.00    0.00 ^ _357_/CLK (sky130_fd_sc_hd__dfxtp_4)
       0.22    0.22 v _357_/Q (sky130_fd_sc_hd__dfxtp_4)
       0.03    0.25 ^ _237_/Y (sky130_fd_sc_hd__inv_8)
       0.07    0.32 ^ _332_/X (sky130_fd_sc_hd__and2_4)
       0.00    0.32 ^ _357_/D (sky130_fd_sc_hd__dfxtp_4)
               0.32   data arrival time

       0.00    0.00   clock clk (rise edge)
       0.00    0.00   clock network delay (ideal)
       0.00    0.00   clock reconvergence pessimism
               0.00 ^ _357_/CLK (sky130_fd_sc_hd__dfxtp_4)
      -0.02   -0.02   library hold time
              -0.02   data required time
    ---------------------------------------------------------
              -0.02   data required time
              -0.32   data arrival time
    ---------------------------------------------------------
               0.33   slack (MET)


    Startpoint: _367_ (rising edge-triggered flip-flop clocked by clk)
    Endpoint: _384_ (rising edge-triggered flip-flop clocked by clk)
    Path Group: clk
    Path Type: max

      Delay    Time   Description
    ---------------------------------------------------------
       0.00    0.00   clock clk (rise edge)
       0.00    0.00   clock network delay (ideal)
       0.00    0.00 ^ _367_/CLK (sky130_fd_sc_hd__dfxtp_4)
       0.70    0.70 ^ _367_/Q (sky130_fd_sc_hd__dfxtp_4)
       0.07    0.77 v _183_/Y (sky130_fd_sc_hd__inv_8)
       0.97    1.74 v _185_/X (sky130_fd_sc_hd__or4_4)
       1.05    2.79 v _192_/X (sky130_fd_sc_hd__or4_4)
       0.83    3.62 v _193_/X (sky130_fd_sc_hd__or4_4)
       0.40    4.02 v _194_/X (sky130_fd_sc_hd__buf_1)
       0.71    4.73 v _195_/X (sky130_fd_sc_hd__or3_4)
       0.35    5.08 v _196_/X (sky130_fd_sc_hd__buf_1)
       0.50    5.58 v _197_/X (sky130_fd_sc_hd__or2_4)
       0.31    5.89 v _198_/X (sky130_fd_sc_hd__buf_1)
       0.44    6.33 v _355_/X (sky130_fd_sc_hd__o22a_4)
       0.15    6.48 ^ _356_/Y (sky130_fd_sc_hd__nor3_4)
       0.00    6.48 ^ _384_/D (sky130_fd_sc_hd__dfxtp_4)
               6.48   data arrival time

      10.00   10.00   clock clk (rise edge)
       0.00   10.00   clock network delay (ideal)
       0.00   10.00   clock reconvergence pessimism
              10.00 ^ _384_/CLK (sky130_fd_sc_hd__dfxtp_4)
      -0.18    9.82   library setup time
               9.82   data required time
    ---------------------------------------------------------
               9.82   data required time
              -6.48   data arrival time
    ---------------------------------------------------------
               3.34   slack (MET)


