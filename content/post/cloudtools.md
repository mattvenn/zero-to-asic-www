---
title: "Cloud Tools for ASIC Development"
date: 2023-01-15T10:00:00+01:00
tags: ["ASIC", "MPW", "course"]
images: ["inverterjupyter.png"]
featured_image: "inverterjupyter.png"
---

ASIC development tools have often been inaccessible due to cost and complexity. Even as free, open-source tools have become available, the complexity of building and installing the tools has slowed their use by would-be designers.

A challenge in making ASIC development more accessible has been to provide free, easy-to-use development tools. Thankfully development of cloud-based tools using open-source software are making chip design easier than ever. 

In June 2022, I had the chance to talk with [@Proppy](https://twitter.com/proppy), a Tokyo-based Google engineer who's enabling people to collaborative ASIC in the cloud with [Jupyter and Colab notebooks](https://github.com/chipsalliance/silicon-notebooks).

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
* Visualizing the optimization results 

{{< youtube yCyOVq5ZHYg >}}

Proppy has further helped lower the bar to ASIC design with [TinyUser Project](/post/tinyuserproject), enabling quick and easy submissions to the Open MPW shuttles.

Other cloud tools exist as well that simplify the ASIC design flow. For the Zero to ASIC course, GitHub's cloud-based *Actions* are an essential part of the flow. They help to continuously build the tools to verify their functionality, as well as to build the final [GDS](/terminology/gds) files and extract their key parameters. 

You can read more about my experiences with GitHub actions [here](/post/github_actions)

