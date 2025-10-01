---
title: "Magic"
date: 2020-11-12T17:39:43+01:00
images: ["magic.png"]
featured_image: "magic.png"
---

From its [homepage](http://opencircuitdesign.com/magic/):

> Magic is a venerable VLSI layout tool, written in the 1980's at Berkeley by John Ousterhout, now famous primarily for writing the scripting interpreter language Tcl. Due largely in part to its liberal Berkeley open-source license, magic has remained popular with universities and small companies. The open-source license has allowed VLSI engineers with a bent toward programming to implement clever ideas and help magic stay abreast of fabrication technology. However, it is the well thought-out core algorithms which lend to magic the greatest part of its popularity. Magic is widely cited as being the easiest tool to use for circuit layout, even for people who ultimately rely on commercial tools for their product design flow. 

I asked John Ousterhout (Magic's author) to ask why it got its name. His reply? He liked the sound of it! Ah the good old days of choosing a name without thinking of search engines...
When you're searching for help on how to use Magic, always include VLSI as a search term!

Magic is a very capable tool: 

* draw transistors and build them into [standard cells](/terminology/standardcell)
* extract the [netlist](/terminology/netlist) that can then be used for [simulation](/terminology/spice) or [LVS](/terminology/lvs)
* work with large numbers of designs in hierarchy
* apply and check [DRC](/terminology/drc) rules

It's quite dated in its user interface, which takes a while to get used to.

It has a [fairly decent tutorial here](http://opencircuitdesign.com/magic/magic_docs.html)

I would say it's worth learning how to navigate a design but probably you won't be doing much actual layout with it unless you are doing [analog layout](/analog). A tool like [LibreLane](/terminology/librelane) in combination with the [Skywater PDK](/terminology/pdk) automates a lot of it.

An alternative tool for viewing files associated with chip design is [klayout](https://www.klayout.de/)
