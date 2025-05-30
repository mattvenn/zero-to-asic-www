---
title: "Testing projects with GitHub actions"
tags: ["tools"]
date: 2025-05-30T13:10:39+02:00
featured_image: "project_github_action_hero.png"
images: ["project_github_action_hero.png"]
---

For the past two years, I've used GitHub Actions to [automatically test the install instructions](/post/github_actions) for the Zero to ASIC course. Now, as I work on a major update, I'm taking it further: I'm adding CI tests for every one of the 10 practical projects.

The goal? Make sure students never run into out-of-date instructions or broken software.

To do this, I've been exploring [Harald's IIC-OSIC-TOOLs Docker image](https://github.com/iic-jku/IIC-OSIC-TOOLS) and built a new [composite GitHub Action](https://github.com/mattvenn/z2a-course-regressions/blob/main/action.yaml).

Here's an example action that leverages the composite action. The top section specifies that it should run monthly, on manual trigger or a push.

```
name: Monthly Check

on:
  push:
  schedule:
    - cron: '0 8 1 * *'  # Run at 08:00 UTC on the 1st of every month
  workflow_dispatch:
```
Then you can see the composite being used in the jobs section. The only thing I have to change are the 4 arguments: repo, ref, command and artifact_file.

```
jobs:
  simulate:
    runs-on: ubuntu-latest

    steps:
      - uses: mattvenn/z2a-course-regressions@main
        with:
          repo: mattvenn/simulate-gate
          ref: nand-ci
          command: make check
          artifact_file: nand.svg
```

When it runs, it leaves a new log on the [action page](https://github.com/mattvenn/simulate-gate/actions).
If you click the most recent action, you should see something like this:

![simulate-gate-action](/simulate-gate-action.png)

You can expand the logs or download the graph of the simulation.

If the check goes wrong for any reason I'll get an email so I can fix it before one of the course participants hits it.
