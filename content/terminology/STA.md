---
title: "STA"
date: 2020-11-12T17:43:21+01:00
description: "Static Timing Analysis"
images: ["sta.png"]
featured_image: "sta.png"
---

Static Timing Analysis checks that at the desired speed, there are no setup and hold violations.

When the input clock rises, a flip-flop will capture and store the incoming data. An ideal flip-flop would sample data exactly on the rising clock and immediately have that data available on the output.
Real flip-flops need the data to stay steady (setup time) for some time before the clock edge, and to stay steady for some time after it (hold time).

If we want to know how fast we can run some combinatorial logic in between 2 flops, we need to know that the flop delay + logic delay is less than the clock period - setup time. Setup time relates to 2 adjacent clock edges.

![setup](/sta_setup.png)

Hold time in comparison is related to a single clock edge. If we take the case where we put one flop's output directly into another's input (like in a shift register), then we need to make sure that the flops both receive the clock at the same time.

![hold](/sta_hold.png)

If the 2nd flop's clock is slightly late for any reason, then we risk the data from the 1st flop changing in the hold time of the 2nd flop.

# OpenSTA

[OpenLane](/terminology/openlane) uses a tool called [OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA).
Its job is to find the fastest and slowest data paths in the design and to check that setup and hold timings are met.

The required timing is set in the OpenLane config file. By default its 10ns, which means we are targetting a clock frequency of 100MHz.

# Min report - validating hold timing

To validate hold timing, OpenSTA does a 'min' timing analysis. Using the most optimisic timing values, how fast can new data arrive at the flip-flop after it receives a clock?

The report below is extracted from reports/synthesis/2-opensta.min_max.rpt which is created right after the synthesis step.

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

# Different reports

There are two calls to OpenSTA during a typical OpenLANE run:

* In the synthesis exploration loop. Here the results can be used to iterate over different synthesis options to help meet timing requirements.
* After extraction. This is the most accurate timing report as it is done on the finished layout. This file is called 27-opensta_spef.min_max.rpt (numbering can change depending on OpenLANE setup).

# MPW1 issues

[MPW1 silicon was faulty](/post/mpw1_silicon) because a hold time violation wasn't detected. This was due to the tools being setup incorrectly. In fact you can see in the above timing charts that the clock network delay for both setup and hold timing reports was 0. This is a clue that the tool wasn't working correctly, as there should always be some small delay in the clock network.
