---
title: "SPICE"
date: 2020-11-12T17:39:43+01:00
images: ["inverter-current.png"]
featured_image: "inverter-current.png"
description: "Simulation Program with Integrated Circuit Emphasis"
---

SPICE general-purpose, open-source analog electronic circuit simulator. It stands for Simulation Program with Integrated Circuit Emphasis.
ngspice is a successor, and is easily installable on Linux. It's the simulator I've used to explore the Skywater 130 [PDK](/terminology/pdk).

Here's an example spice simulation file that I used to [simulate the inverter I drew](/post/inverter).

    Inverter Simulation
    * this file edited to remove everything not in tt lib
    .lib "./sky130_fd_pr/models/sky130.lib.spice" tt

    * instantiate the inverter
    Xinv Y A VPWR VGND VGND VPWR inverter

    .subckt inverter Y A NWELL VSUBS VGND VPWR
    * NGSPICE file created from inverter.ext - technology: sky130A


    * Top level circuit inverter

    X0 Y A VPWR NWELL sky130_fd_pr__pfet_01v8 w=1e+06u l=150000u
    X1 Y A VGND VSUBS sky130_fd_pr__nfet_01v8 w=650000u l=150000u
    C0 VGND A 0.06fF
    C1 NWELL VPWR 0.05fF
    C2 VPWR Y 0.16fF
    C3 NWELL Y 0.00fF
    C4 VGND VPWR 0.01fF
    C5 VGND Y 0.06fF
    C6 A VPWR 0.05fF
    C7 A Y 0.03fF
    C8 VGND VSUBS 0.62fF
    C9 Y VSUBS 0.22fF
    C10 VPWR VSUBS 0.55fF
    C11 A VSUBS 0.32fF
    C12 NWELL VSUBS 0.63fF


    .ends

    * set gnd and power
    Vgnd VGND 0 0
    Vdd VPWR VGND 1.8

    * create pulse
    Vin A VGND pulse(0 1.8 1p 10p 10p 1n 2n)
    .tran 10e-12 2e-09 0e-00

    .control
    run
    set color0 = white
    set color1 = black
    plot A Y
    plot i(Vdd)
    .endc

    .end
