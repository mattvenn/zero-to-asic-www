---
title: "OpenLANE Output Files"
date: 2021-04-16T13:06:58+02:00
featured_image: "/openlane-flow.png"
---

[OpenLANE](/terminology/openlane) makes a lot of output files! This can be quite confusing when you're getting started.

Here's a [useful spreadsheet](https://docs.google.com/spreadsheets/d/1YI5u9izOAu-M98WH2ftB0fTlnlqDJJyd2DKChN_Zku4/edit?usp=sharing) I made to show:

* the path of the files
* most important files and what they mean
* which tool creates which file

Thanks Amr and Ahmed for helping me with this!

Note that newer versions of OpenLANE have started numbering the filenames so I will update the spreadsheet in the future to reflect this.

# OpenLANE summary tool

I've also made a summary tool: https://github.com/mattvenn/openlane_summary

This allows you to easily:

* browse and pick a specific results directory
* get a summary of violations
* get a summary of antenna issues
* show usage of standard cells
* easily view the various stages of the OpenLANE ASIC flow: floorplanning, power distribution, placement and the final GDS.

{{< youtube 2wBbYU_8dZI>}}
