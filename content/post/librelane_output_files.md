---
title: "LibreLane Output Files"
date: 2021-04-16T13:06:58+02:00
images: ["openlane-flow.png"]
tags: ["tools"]
featured_image: "openlane-flow.png"
aliases:
    - /post/openlane_output_files
---

[LibreLane](/terminology/librelane) makes a lot of output files! This can be quite confusing when you're getting started.

Here's a [useful spreadsheet](https://docs.google.com/spreadsheets/d/1SePRLd8waVPa1BXPMB2cBOUIXK2lYbP_ace_7pNuEw8/edit#gid=557128491) I made to show:

* the path of the files
* most important files and what they mean
* which tool creates which file

Thanks Amr and Ahmed for helping me with this!

The spreadsheet was updated for LibreLane in 2025.

# LibreLane summary tool

I've also made a summary tool: https://github.com/mattvenn/librelane_summary

This allows you to easily:

* browse and pick a specific results directory
* get a summary of violations
* get a summary of antenna issues
* show usage of standard cells
* easily view the various stages of the LibreLane ASIC flow: floorplanning, power distribution, placement and the final GDS.

{{< youtube 2wBbYU_8dZI>}}
