---
title: "STA"
date: 2020-11-12T17:43:21+01:00
description: "Static Timing Analysis"
featured_image: "/sta.png"
---

Static Timing Analysis checks that at the desired speed, there are no setup and hold violations.

When the input clock rises, a flip-flop will capture and store the incoming data. If data changes in the setup time, then there is a chance the wrong data will be captured. This is a setup violation. The same thing applies to data changing after the clock, which is called a hold violation.

![setup and hold](/setup_and_hold.png) [Image source](https://www.designnews.com/electronics-test/how-track-down-setup-and-hold-violations-mixed-signal-oscilloscope)

# OpenSTA

[OpenLane](/terminology/openlane) uses a tool called [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA).
Its job is to find the fastest and slowest data paths in the design.

The required timing is set in the OpenLane config file. By default its 10ns, which means we are targetting a clock frequency of 100MHz.

# Min report - validating hold timing

To validate hold timing, OpenSTA does a 'min' timing analysis. Using the most optimisic timing values, how fast can new data arrive at the flip-flop after it receives a clock?

This report below is extracted from reports/synthesis/opensta.min_max.rpt:

The report shows the shortest data path and sums the data arrival time (0.32ns). The data arrival time has to be more than the hold time (-0.02ns - yes hold times can be negative!). As 0.32ns > -0.02ns we pass the hold requirements.

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

# Max report - validating setup timing

To validate setup timing, OpenSTA does a 'max' timing analysis. This uses the most pessimistic timing to check how long it takes the data to arrive at the flip-flop. It is measured against the next clock edge and verifies that the data will arrive in time.

For the max report, the longest path is found (6.48ns). Then the time the data is required to be stable is calculated by subtracting the setup time from the clock period (9.82ns).

We need the data to arrive before the setup time: 6.48ns < 9.82ns. So in this case we pass the setup requirements.

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


