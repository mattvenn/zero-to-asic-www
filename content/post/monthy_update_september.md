---
title: "Monthly Update - September"
date: 2022-10-13T10:00:00+01:00
tags: ["3D rendering","ASIC", "course" ]
images: ["mouse_chip.jpg"]
featured_image: "mouse_chip.jpg"
---

Welcome to the September 2022 monthly update!

Here are the main topics from last month:
* [MPW7](/post/mpw7_submitted/) submission,
* [MPW2](/post/mpw2_submitted/) updates,
* Job posting at E-Fabless,
* New videos,
* Is it the end for UVM? and
* Rendering GDS files with [Blender](https://www.blender.org/) or in your browser

## MPW7
The deadline for MPW7 was the 14th of September and the Zero to ASIC course submitted another set of projects. Special shout out to Farhad, Peng and James who are all first time tape outs on the project. Well done everyone!

There were 72 projects submitted and that passed tape out. There are about 100 that were submitted overall, and you can see all these different projects on the [E-fabless platform page](https://platform.efabless.com/projects/MPW7/) if you want to take a better look.

I've already picked out some of my favorites:
* A RISC-V processor with a 5 GHz transceiver
* An out-of-order RISC-V Core and
* A CAN controller,
so have a look, pick your favorites, and let me know which authors you'd like me to invite to do an interview.

## E-Fabless Project Browser Tool
Don't forget my [E-fabless project browser tool](https://github.com/mattvenn/efabless_project_tool/) that lets you easily see all the projects and search them to see what people are making. You can also get the links to the projects and the GitHub repositories.

## Job Posting
[E-fabless is looking for a Silicon Validation Engineer](https://www.linkedin.com/jobs/view/3293645910/?refId=BA5W4wSSRYOP%2FlHyVfboBw%3D%3D). It's a full-time job and it's remote, so if you're interested in getting involved with verifying open source silicon, then drop them a line on LinkedIn.

## MPW2 Updates
On the topic of E-Fabless, the [MPW2 update posts](https://groups.google.com/g/skywater-pdk-announce/c/HelusBBUZ20?pli=1) are continuing to arrive. They're doing one a week so check out this latest one about the updated hardware breakout board that has the place to put your MPW2 silicon. The ASIC goes on the top and it plugs into an STM32 development board, which luckily is in stock. They've sent the PCBA order so they're expecting them back within a week and they should be sending them off soon.

## Interview with James Stine
In case you missed it, I did a really interesting [interview with James Stine](/post/interview-with-james-stine/) about making the [standard cells](/terminology/standardcell/) for the open source Global Foundries 180 process. There are loads of good questions answered in there, so definitely worth a watch.

## News from the Fossi Foundation 
The [Correo Libre](https://www.fossi-foundation.org/2022/09/13/ecl54) has been released on the 13th of September, and it has lots of interesting stuff. My picks are Cocotb 1.7 and the information on the US Chips Act. There is lots of money being spent there and we're looking forward to getting some money in the EU, hopefully some of which will go to open source projects.

## Tiny Tapeout
Now a little bit of Tiny Tapeout news. We're continuing to work on this behind the scenes, and we're getting ready for the next submission series, so stay tuned for that! [Don't forget to join the mailing list](https://mailchi.mp/574276e3c9d7/tinytapeout).

## Wokwi Updates
We've got some really great upgrades to Wokwi, so thanks Uri for that. We can now shift and select and drag multiple blocks at once, which is great. We've also got undo and redo, so that's really good news. Try out the [Tiny Tapeout template on Wokwi](https://wokwi.com/projects/339439899388150354)

## Rendering GDS files in your browser or with Blender
We've got a great feature added by Maximo and Proppy that now lets you generate really cool 3D interactive viewers. After your [GDS](/terminology/gds/) is generated, the rendering happens in the cloud via a GitHub action. In the [interactive viewer](https://mattvenn.github.io/wokwi-verilog-gds-test/viewer/tinytapeout.html), you can check out the stats, what standard cells are used as you hover over them, you can see what the cell is, you can turn on and off the fill layer, turn off unused cells and much more, all within your browser! 

And talking of rendering, I finally got around to doing a [how-to video with Maximo](https://www.youtube.com/watch?v=gBjQI3GrBHU&ab_channel=ZeroToASICCourse). We looked at how you can turn your GDS into STL files import them into blender and then make amazing renders. Thanks very much Maximo. For more info check out the [3D rendering blog post](/post/3Drendering/).

{{< youtube gBjQI3GrBHU >}}

## Is it time to say goodbye to UVM?
I want to draw attention to a blog post by [Olof Kindgren](http://olofkindgren.blogspot.com/2022/10/its-time-to-to-thank-uvm-and-say-goodbye.html) who's suggesting maybe it's time to say goodbye to UVM. It's a really interesting blog post, and it sparked quite a lot of discussion on Twitter and Linkedin, so check it out and give your opinion in the comments.

Okay, that's it for this month! During October I'm going to be continuing to prepare for the [Hackday Supercon](https://hackaday.com/tag/2022-hackaday-supercon/) with the Tiny Tapeout face-to-face workshops. I'm looking forward to seeing some of you there, so have a great month!
