---
title: "CI with Github Actions"
date: 2022-01-05T18:33:02+01:00
tags: ["tools"]
featured_image: "github_action.png"
images: ["github_action.png"]
---

I have slowly been learning how to use Github actions to help me build microchips.

It's harder than it should be to get a working toolchain up. There are lots of repositories,
submodules, docker images, environment variables, and they all have to be exactly right. 
If not, either the flow won't work correctly, or you'll make some [GDS](/terminology/gds) that will fail
the precheck or tapeout tests.

For the course, I have a VM and a set of instructions to do a manual install.

And sometimes the instructions start failing. The most recent fail was due to some more hidden state - the default submodule that caravel_user_project installs was updated automatically by a github action.

So I have now put all the instructions into a Github action: https://github.com/mattvenn/project0_test

Every night, this project automatically:

* installs [Magic](/terminology/magic) - used to build the [PDK](/terminology/pdk),
* clones caravel_user_project and builds [OpenLane](/terminology/openlane) and the PDK,
* builds the example project [GDS](/terminology/gds),
* builds the final submission GDS,
* saves the GDS and build summaries.

If anything goes wrong, I get an email and I can correct the instructions before the next person registers for my course.

![github action](/github_action.png)

I'm also working on an action that will test if a project is ready for group submission with the [multi project tools](https://github.com/mattvenn/multi_project_tools). 
The idea is that you could add this action to your repo and it would continually check that all the required tests pass and even build the GDS ready for submission.

{{< twitter user="matthewvenn" id="1478071480814653443" >}}

# Update

The group project action and multi tools actions are both live and working well. We use them regularly now, including for [MPW6](/post/mpw6_submitted), [MPW7](/post/mpw7_submitted), and [MPW8](/post/mpw8_submitted) submissions, as well as [Tiny Tapeout](http://tinytapeout.com/) and [GF180](/post/tinyuserproject/). 

* [multi project tools](https://github.com/mattvenn/zero_to_asic_mpw8/actions/workflows/multi_tool.yaml),
* [submission template](https://github.com/mattvenn/wrapped_project_template/actions/workflows/multi_tool.yaml).

Here's a video explaining how GitHub actions are used to generate the GDS files for Tiny Tapeout:
{{< youtube lXKt7CKRUes >}}

