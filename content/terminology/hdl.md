---
title: "HDL"
date: 2020-11-13T11:58:32+01:00
images: ["hdl.png"]
featured_image: "hdl.png"
---

A Hardware Description Language is used to... describe hardware!
So instead of drawing out an [inverter](/post/inverter) using a tool like [Magic](/terminology/magic) we can write a line like this:

    output = !input;

Which describes what an inverter does. The ! means invert. This is a description of what the circuit does, similar to a programming language like C (although everything happens at once, not in sequence). This is referred to as a 'register transfer language' or RTL. You can also describe a circuit schematic in an HDL, and then it is referred to as a netlist.

Common HDLs are Verilog and VHDL. There are also higher level languages like [Amaranth](https://amaranth-lang.org/docs/amaranth/latest/index.html), [Chisel](https://www.chisel-lang.org/) & [Spinal](https://github.com/SpinalHDL/SpinalHDL).

The [VexRiscv RISCV](https://github.com/SpinalHDL/VexRiscv) processor in the [harness we use for Efabless submissions](/terminology/shuttle#caravel) is written in Spinal, by Charles Papon.

These are often implemented as a library to a programming language like Python or Scala. Then you can express more complex hardware in fewer lines.

Verilog is the most common HDL and the one most well supported by the Open Source tools. It's well known for the number of 'foot guns' it has!
Be careful, describing hardware with an HDL is nothing like programming a CPU with a sequential language like C or Python.

Circuits operate all at once, parallelism is easy. If you want sequences of things you have to build a sequencer first (like a state machine).

A CPU executes one instruction at a time and if you want parallelism you either 'fake' it by interleaving programs or you have multiple cores on your CPU.

A good short course (targetted at FPGAs) introducing Verilog is [WTFPGA](https://github.com/icebreaker-fpga/icebreaker-workshop).

A good FPGA resource is Will's [Project F](https://projectf.io/).

After writing your design in an HDL, you have to [synthesise](/terminology/synthesis) into a [netlist](/terminology/netlist) so it can be recreated in the actual building blocks you have in the [PDK](/terminology/pdk)
