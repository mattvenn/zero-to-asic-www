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

The report below is extracted from reports/synthesis/1-opensta.min.rpt which is created right after the synthesis step.

The report shows the shortest data path and sums the data arrival time (0.38ns). The data arrival time has to be more than the data required time (0.24ns). As 0.32ns > 0.24ns we pass the hold requirements.

    Startpoint: _1786_ (rising edge-triggered flip-flop clocked by wb_clk_i)
    Endpoint: _1787_ (rising edge-triggered flip-flop clocked by wb_clk_i)
    Path Group: wb_clk_i
    Path Type: min

    Fanout     Cap    Slew   Delay    Time   Description
    -----------------------------------------------------------------------------
                      0.15    0.00    0.00   clock wb_clk_i (rise edge)
                              0.00    0.00   clock network delay (ideal)
                      0.15    0.00    0.00 ^ _1786_/CLK (sky130_fd_sc_hd__dfxtp_2)
                      0.03    0.31    0.31 v _1786_/Q (sky130_fd_sc_hd__dfxtp_2)
         1    0.00                           rgb_mixer0.debounce2_b.button_hist[0] (net)
                      0.03    0.00    0.31 v _0894_/A (sky130_fd_sc_hd__inv_2)
                      0.04    0.04    0.35 ^ _0894_/Y (sky130_fd_sc_hd__inv_2)
         3    0.01                           _0216_ (net)
                      0.04    0.00    0.35 ^ _1177_/B (sky130_fd_sc_hd__nor2_2)
                      0.01    0.02    0.38 v _1177_/Y (sky130_fd_sc_hd__nor2_2)
         1    0.00                           _0030_ (net)
                      0.01    0.00    0.38 v _1787_/D (sky130_fd_sc_hd__dfxtp_2)
                                      0.38   data arrival time

                      0.15    0.00    0.00   clock wb_clk_i (rise edge)
                              0.00    0.00   clock network delay (ideal)
                              0.25    0.25   clock uncertainty
                              0.00    0.25   clock reconvergence pessimism
                                      0.25 ^ _1787_/CLK (sky130_fd_sc_hd__dfxtp_2)
                             -0.01    0.24   library hold time
                                      0.24   data required time
    -----------------------------------------------------------------------------
                                      0.24   data required time
                                     -0.38   data arrival time
    -----------------------------------------------------------------------------
                                      0.14   slack (MET)

# Max report - validating setup timing

To validate setup timing, OpenSTA does a 'max' timing analysis. This uses the most pessimistic timing to check how long it takes the data to arrive at the flip-flop. It is measured against the next clock edge and verifies that the data will arrive in time.

For the max report, the longest path is found (4.64ns). This must be shorter than the data required time (7.75ns).

    Startpoint: la1_data_in[0] (input port clocked by wb_clk_i)
    Endpoint: io_out[15] (output port clocked by wb_clk_i)
    Path Group: wb_clk_i
    Path Type: max

    Fanout     Cap    Slew   Delay    Time   Description
    -----------------------------------------------------------------------------
                      0.15    0.00    0.00   clock wb_clk_i (rise edge)
                              0.00    0.00   clock network delay (ideal)
                              2.00    2.00 ^ input external delay
                      2.45    1.89    3.89 ^ la1_data_in[0] (in)
        66    0.30                           la1_data_in[0] (net)
                      2.45    0.00    3.89 ^ _0863_/A (sky130_fd_sc_hd__inv_2)
                      0.24    0.02    3.90 v _0863_/Y (sky130_fd_sc_hd__inv_2)
         2    0.00                           _0191_ (net)
                      0.24    0.00    3.90 v _0864_/A (sky130_fd_sc_hd__buf_1)
                      0.06    0.21    4.11 v _0864_/X (sky130_fd_sc_hd__buf_1)
         5    0.01                           _0192_ (net)
                      0.06    0.00    4.11 v _0865_/A (sky130_fd_sc_hd__buf_1)
                      0.07    0.15    4.26 v _0865_/X (sky130_fd_sc_hd__buf_1)
         5    0.01                           _0193_ (net)
                      0.07    0.00    4.26 v _1527_/C1 (sky130_fd_sc_hd__o221a_2)
                      0.04    0.14    4.40 v _1527_/X (sky130_fd_sc_hd__o221a_2)
         1    0.00                           rgb_mixer0.pwm1.out (net)
                      0.04    0.00    4.40 v _1696_/A (sky130_fd_sc_hd__ebufn_2)
                      0.15    0.25    4.64 v _1696_/Z (sky130_fd_sc_hd__ebufn_2)
         1    0.04                           io_out[15] (net)
                      0.15    0.00    4.64 v io_out[15] (out)
                                      4.64   data arrival time

                      0.15   10.00   10.00   clock wb_clk_i (rise edge)
                              0.00   10.00   clock network delay (ideal)
                             -0.25    9.75   clock uncertainty
                              0.00    9.75   clock reconvergence pessimism
                             -2.00    7.75   output external delay
                                      7.75   data required time
    -----------------------------------------------------------------------------
                                      7.75   data required time
                                     -4.64   data arrival time
    -----------------------------------------------------------------------------
                                      3.11   slack (MET)

# Different reports

The reports are split into min and max files.

There are currently 5 calls to OpenSTA during a typical OpenLane including:

* In the synthesis exploration loop. Here the results can be used to iterate over different synthesis options to help meet timing requirements.
* After resizing cells (to get better timing performance - [see this video](https://www.youtube.com/watch?v=ajwZVAVo3yk))
* After extraction. This is the most accurate timing report as it is done on the finished layout. These files are called:
    * 23-spef_extraction_sta.min.rpt (numbering can change depending on OpenLane setup).
    * 23-spef_extraction_sta.max.rpt

# MPW1 issues

[MPW1 silicon was faulty](/post/mpw1_silicon) because a hold time violation wasn't detected. This was due to the tools being setup incorrectly. In fact you can see in the above timing charts that the clock network delay for both setup and hold timing reports was 0. This is a clue that the tool wasn't working correctly, as there should always be some small delay in the clock network.
