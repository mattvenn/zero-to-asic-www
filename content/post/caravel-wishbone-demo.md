---
title: "Caravel Wishbone Demo"
date: 2021-05-19T17:25:37+02:00
images: ["wishbone.png"]
featured_image: "wishbone.png"
---

[Caravel](/terminology/shuttle#caravel) is the name of the harness provided by [Efabless](https://efabless.com) to make it
easier to submit a design to the [foundry](/terminology/foundry).

Among other things, it provides:

* The [padring](/terminology/padring)
* 3kB of memory
* A small RISCV processor called PicoRV32
* GPIOs
* A logic analyser
* A Wishbone bus

For the full details, [check the documentation](https://caravel-harness.readthedocs.io/en/latest/?badge=latest)

The simplest way to interface between your project and the PicoRV32 is probably the logic analyser. This gives you 128 ins and outs that you
can use to configure or debug your design.

For anything more complex, it makes sense to switch to a standard bus interface, in this case we are provided a Wishbone bus.

![wishbone](/wishbone.png)

I put together a simple wishbone client here: https://github.com/mattvenn/wishbone-buttons-leds/tree/caravel

And installed it into Caravel here: https://github.com/mattvenn/caravel_user_project/tree/wishbone-demo

Here's a short video giving a brief overview of how wishbone works, how the wishbone client is patched into Caravel, and a demo of it in action.

{{< youtube jEQnLxADgr0 >}}
