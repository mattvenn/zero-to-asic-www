---
title: "Node"
date: 2020-11-13T16:48:16+01:00
images: ["half-pitch.png"]
featured_image: "half-pitch.png"
description: The process node number (e.g. 130nm, 7nm) originally described the metal half-pitch and gate length of a fabrication process, but since the 1990s the number has been decoupled from physical dimensions and is largely a marketing term.
faq:
  - q: What does the process node number mean in chip manufacturing?
    a: The node number originally referred to both the metal half-pitch (half the minimum center-to-center spacing between Metal 1 lines) and the gate length, which were roughly the same value. By the 1990s these became decoupled — the 130nm node actually has 70nm gates — and by 2000 the number had absolutely no physical meaning.
  - q: Is the process node number accurate today?
    a: No. Since around 2000 the node number has had no physical meaning and is used mainly as a marketing tool. The gate length and metal half-width measurements have become completely uncoupled from the advertised node number.
  - q: How common are older process nodes like 130nm?
    a: Despite being old, the 130nm process and larger/older sizes still account for about 50% of all ASICs made by EuroPractice, showing that older nodes remain commercially important.
---

The metrics for measuring integration density used to be metal half-pitch and gate length. For a while they were about the same number. This number became known as the node or process number.

The half-pitch refers to half the minimum center-to-center distance spacing (or pitch) between Metal 1 lines.

![half pitch](/half-pitch.png)

By 1990s these numbers became uncoupled, and the 130nm node actually has 70nm gates. 
By 2000, the node number "had by then absolutely no meaning" (Paolo Gargini. IEEE article by Samuel  K. Moore: [The node is nonsense](https://ieeexplore.ieee.org/document/9150552).)

It's still used as a marketing tool, but it doesn't really mean anything anymore.

![node sizes](/node-table.png)

The table above shows how the gate length and metal half width measurements have become uncoupled from the node number. The table came from this interesting video about the latest and smallest process sizes.

{{< youtube 1kQUXpZpLXI >}}

Finally, this chart shows how even though the 130nm process is quite old, it and larger/older sizes still account for about 50% of all ASICs made by EuroPractice.

![process pie chart](/process-pie-chart.png)
