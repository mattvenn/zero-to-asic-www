---
title: "Verification"
date: 2020-11-12T17:44:17+01:00
---

[Simulation](/terminology/simulation) offers us a way of checking the design is doing what we expect, but that is almost exactly why simulation on its own isn't enough.
When we simulate we are testing what we _expect to happen_. The problems happen when your design experiences something outside the expected.

There are a couple of extra tools we can use to increase our confidence that the design will work as designed.

# Coverage

A coverage tool tests how complete your simulation or verification efforts actually are.
I'm only aware of one free coverage tool we can use for [HDL](/terminology/hdl), and that's [Symbiotic EDA's mcy](https://mcy.readthedocs.io/en/latest/tutorial.html).

# Formal Verification

Formal verification offers the opportunity to _prove_ various properties of your design. For example, in the [multi project harness](/post/multi-project-harness), I wanted to 
prove that when the design is in reset the outputs are all undefined.

I can do that by adding an _assertion_ to my design:

    if(&reset)
        assert(gpio_out == 10'bz);

Then I run a tool that uses a solver to prove that this assertion will always hold. If there is any way it can fail it will produce a short trace called a counter example. 
Even though this example is very simple it's good to know that if I do something that accidentally messes up this property the assertion will fail, alerting me.

I have made a short course on Formal Verification for Symbiotic EDA you can follow here:

{{< youtube _5R35QFsXM4 >}}

