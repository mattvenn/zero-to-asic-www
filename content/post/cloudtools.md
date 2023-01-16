---
title: "Cloud Tools for ASIC Development"
date: 2023-01-15T10:00:00+01:00
tags: ["ASIC", "MPW", "course"]
images: ["inverterjupyter.png"]
featured_image: "inverterjupyter.png"
---

For a long time, ASIC development tools have been inaccessible due to cost or complexity. Even as free, open-source tools became available, getting them installed felt like untangling a Gordian Knot, cutting off would-be designers from the start.

A key in opening ASIC development to the masses has thus been to provide free, easy-to-use development tools. Thankfully new efforts in cloud-based tools using open-source software are making ASIC development easier than ever. 

Google is creating collaborative cloud notebooks for ASIC design. In June 2022, I had the chance to talk with [@Proppy](https://twitter.com/proppy), a Tokyo-based Google engineer who's enabling people to collaborative ASIC in the cloud with [Jupyter and Colab notebooks](https://github.com/chipsalliance/silicon-notebooks).

In the interview we discussed:

* Example of [researcher Teodor-Dumitru Ene](/post/interview-with-teo/) using the tools to design optimized hardware adders
* Making ASIC design tools accessible 
* Benefits of an online notebook approach
* Walking through a simple inverter design example
* How to host the notebooks on your own computer or virtual machine
* Package management using Anaconda
* Extracting design metrics 
* More complicated RISC-V SoC example
* Optimizing designs for specific parameters
* Visualization of optimization results 

{{< youtube yCyOVq5ZHYg >}}

For Zero to ASIC, GitHub's cloud-based tool *Actions* is an essential part of the design flow. They help to continuously build the tools to verify their functionality, as well as to build the final [GDS](/terminology/gds) files and extract their key parameters. You can read more about my initial experiences with GitHub actions [here](/posts/github_actions). 


