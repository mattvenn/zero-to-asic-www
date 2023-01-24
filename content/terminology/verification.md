---
title: "Verification"
date: 2020-11-12T17:44:17+01:00
images: ["simulation.png"]
featured_image: "simulation.png"
---

Verification covers all areas of checking that a design, at some stage in the design process, is correct. This includes simulation, STA, DRC, LVS, LEC and other checks that are performed. In essence, any step that looks at the design, compares it with some other quantity, and does not alter the design, is part of verification.

[Simulation](/terminology/simulation) offers us a way of checking the design is doing what we expect functionally, but that is almost exactly why simulation on its own isn't enough.
When we simulate we are testing what we _expect to happen_. The problems happen when your design experiences something outside the expected. Simulation relies on stimuli and some model of expected behaviour, whether explicit or in the designer's head. If you don't apply the right stimuli, you won't be able to see a functional error that only occurs for that unique set of stimuli.
Simulation is a form of dynamic verification ie it is stimulus driven. In contrast, STA and LEC are static forms of verification - they only compare against a simple set of rules for how the circuit is meant to behave, or verify one circuit is equivalent to another. All elements are examined, with a focus on finding the most extreme paths, etc.

There are a couple of extra tools we can use to increase our confidence that the design will work as designed.

# Coverage

A coverage tool tests how complete your simulation efforts actually are.
I'm only aware of one free coverage tool we can use for [HDL](/terminology/hdl), and that's [YosysHQ's mcy](https://mcy.readthedocs.io/en/latest/tutorial.html). This is equivalent to coverage in a software environment - it sees whether all parts of a circuit have been exercised (controllability), and potentially that the result of that has some impact visible in the outside world (observability). 

# Formal Verification

Formal verification offers the opportunity to _prove_ various properties of your design. For example, in the [multi project harness](/post/multi-project-harness), I wanted to 
prove that when the design is in reset the outputs are all undefined. LEC is one form of formal verification - it uses logical rules to prove circuits are equivalent. Assertion validation is another form - it allows the designer to state things that always, or never happen, and then attempts to prove if this is true by trying to find ways to setup the circuit to break the assertion.

I can do that by adding an _assertion_ to my design:

    if(&reset)
        assert(gpio_out == 10'bz);

Then I run a tool that uses a solver to prove that this assertion will always hold. If there is any way it can fail it will produce a short trace called a counter example. 
Even though this example is very simple it's good to know that if I do something that accidentally messes up this property the assertion will fail, alerting me.
