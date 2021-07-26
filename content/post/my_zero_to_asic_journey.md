---
title: "My Zero to ASIC journey"
date: 2021-03-10T11:36:30+01:00
featured_image: /matt_photo.jpg
---

Almost exactly a year ago in March 2020 I started getting interested in Open Source ASIC tooling. I don't remember exactly what sparked my interest, but I remember this talk by Tim Edwards at WOSH: [Bootstrapping a real working design flow](https://www.youtube.com/watch?v=ztcAbszOBs8) and sometime after seeing [Adam Zeloof posting a picture of an ASIC implementation of pong](https://twitter.com/azzeloof/status/1180877525372882944).

I began by investigating [QFlow](http://opencircuitdesign.com/qflow/). The [standard cells](/terminology/standardcell) used by QFlow were from Oklahoma State University (OSU).

By May I was getting a few results out of QFlow and I was curious to discover how digital logic actually works on silicon. I experimented with [Magic](/terminology/magic) and managed to draw and simulate an inverter after taking one of [Kunal Ghosh's VLSI courses](https://www.vlsisystemdesign.com/basic_courses/). 

{{< twitter 1274728518216306690 >}}

Seeing such interest in this topic gave me a bit of an energy boost and I began wondering if I could find enough people to share the cost of producing an ASIC. I worked up a quick course structure and started getting feedback from people in the industry. It looked like if there 10 people all willing to put in $1000 we could do it.

This was when I first met Mohammed Kassem and Tim Edwards from [Efabless](https://efabless.com/) who have continued to be extremely helpful. I also spoke to Olof Kindgren who I'd met at WOSH. He said I should talk to Tim Ansell because there was something in the pipeline that might change how I was planning to make an ASIC!

Then in late June 2020 we had the [announcement from Tim](https://www.youtube.com/watch?v=EczW2IWdnOM) about the Open Source PDK and the Google sponsored shuttle. 
This of course changed everything! We now had an Open Source, production ready [PDK](/terminology/pdk) along with a new set of tools called [OpenLANE](/terminology/openlane) that aimed to turn your [HDL](/terminology/hdl) into the files needed for ASIC manufacture. 
I was quickly able to use OpenLANE to turn my [FPGA VGA clock design](/post/vga_clock/) into [GDS2 files](/terminology/gds2).

In August Hackaday put a call out for talks to their #remoticon conference. I asked on Twitter to gauge interest and subsequently began working on a presentation.
I just couldn't get it short enough to fit but they kindly gave me a bigger slot - it was still a tight squeeze covering everything in 1 hour! I think I practiced that presentation 4 times, and even did it in Spanish for my local hackerspace.

{{< twitter 1298282514495213574 >}}

My work situation had just changed and I was thinking that instead of looking for another electronics contracting job I could try creating a paid course. I decided to add a link to the end of the talk and find out how many people would be interested in paying for a course.

October came and although it was sad not to be at a live conference I still had a blast delivering the [Zero to ASIC](/post/remoticon-talk) demos and presentation. About 100 people signed up for a course over the next few weeks and so I decided to go for it.

November was the date for submitting our designs to the shuttle so I was super busy with getting that working. I had to get 3 of my own designs ready, along with another 5 from some interested collaborators, at the same time working out a way to combine them all into one chip.

Not a great time to get COVID19, but luckily not severely. I was out of action for about 5 days, and the rest of my quarantine period was spent fixing issues on the shuttle application, [interviewing people](/tags/interviews) and creating a video introduction to the course. 

This was a pretty hard time - looking back at my project log, it's full of complaints about the tools not working and feeling disheartened. Efabless made a huge effort, and I got a lot of help from Ahmed and Amr in these final stages getting everything wired up. Putting lots of designs together wasn't the 'normal' way of using the tools getting used so I was running into a lot of issues that hadn't been solved by other people.

Finally in mid December [all the designs were submitted](/post/asic_submitted) and my first tape-out was complete!

![ASIC submission](/caravel-numbered.png)

On the 23rd of December I put 15 tickets on sale for the first course and they sold out in 2 hours! It was a great feeling, but also scary - I had to actually create the course now!

In January I worked pretty much every day developing content and creating videos to support them. I had a chat with [Joe FitzPatrick](https://securinghardware.com/) about how he structures his course content, and that helped me decide how I wanted to lay the course out. One of the first course participants kindly agreed to be my beta tester and reviewed the material after I finished each section.

Late January we got word that some designs had faults in them and had to be fixed before they could be sent to Skywater. My design had [short circuits in the MUX](/post/last_minute_drc/) that would have wrecked the whole chip! Luckily this was not too hard to fix, but it was amazing how much I had forgotten since making the first application just a few months before. I was pretty happy I had written a project log and had the git commit history.

The first course started in February and it's just finishing now. Feedback has been great and I'm working to improve the course and satisfy demand.

I'm very happy to have this opportunity. I've done a lot of science communication and always really enjoyed it. This course combines my love of electronics and teaching. 
The demand for tickets is helping me continue my study of Open Source ASIC tooling, contribute back to the community and help spread this experience to people who, like me, would never have thought that they'd one day get to make their own chips.

![Matt with ASIC print](/matt_photo.jpg)
