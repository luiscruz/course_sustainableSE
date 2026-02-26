---
author: Cosmin Anton, Jan Kuhta, Ada Turgut, Thomas van der Boon
group_number: 34
title: "Effect of video quality and browser type on youtube energy consumption"
image: "img/g34_measuring_software/project_cover.png"
date: 12/02/2026
summary: |-
  The goal is to measure the effect of video quality and the different types of browsers have on the energy consumption of youtube. 
  We are planning on using a variety of browsers such as chrome, edge, safari, opera and on each check a variety of qualities ranging from 240px - 4k. 
  This will also be tested on different laptops to both compare and average out the results to get a less biased view.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

# Introduction

YouTube is one of the most widely used online video platforms in the world. According to Global Media Insight, the
platform attracts approximately 122 million daily active users, collectively watching over 1 billion hours of video each
day [1]. This scale of consumption translates into a significant and growing energy footprint, spread across data
centers, network infrastructure, and the client devices of viewers worldwide.

In addition to the established YouTube settings, such as video quality, playback speed, and subtitles, YouTube has
recently
introduced several optional player features to improve user experience: Ambient Mode, Stable Volume, and Voice Boost.
Notably, two of these (Ambient Mode and Stable Volume) are enabled by default, regardless of whether the users are
aware of or want these features.

In this blog post, we investigate whether these non-essential YouTube settings have a measurable effect on client-side
energy consumption. We conducted a controlled experiment in which each feature was enabled in isolation and energy
consumption was recorded over repeated trials. Our hypothesis is that each of these features introduces additional
computational work and therefore increases energy consumption relative to the baseline, where all those features are
disabled. This raises a broader question about the sustainability of enabling such features by default and whether
the platform designers should reconsider these defaults in the interest of energy efficiency and sustainability.

# Methodology

## Explored YouTube settings

YouTube offers several optional settings that can be toggled in the settings menu. For this experiment, we isolated
three
non-essential features, testing each individually against a common baseline.

**Ambient Mode** extends the video's color onto the surrounding page background, creating a soft glow effect
that mirrors the on-screen content in real time, dynamically adjusting when scenes change [2]. This feature is only
active in dark mode and is enabled by default.

**Stable Volume** automatically normalizes audio levels during playback, dynamically adjusting the volume to reduce
sudden loudness spikes and flatten the dynamic range within a video [3]. This setting is also enabled by default.

**Voice Boost** enhances the clarity of speech in videos by using AI to identify vocal frequencies and amplify spoken
dialogue relative to background sounds such as music or ambient noise, with all processing occurring in real time on the
client side [4]. Unlike the other two settings, Voice Boost is disabled by default, but remains relevant to our
experiment as it represents a feature that a significant portion of users may choose to enable.

The baseline condition (all-off) disables all three features simultaneously and serves as our reference point for energy
consumption.

## Experiment procedure

We defined four conditions (one per setting plus the baseline) and conducted 30 trials per condition, running 120
trials in total. To minimize human error and ensure consistency across trials, the entire experiment was automated using
Python and Playwright [2]. The Hardware and software details of the machine on which we conducted the
experiment are provided below in section [Hardware/Software Details](#hardwaresoftware-details). The video used throughout all trials was a fixed,
publicly available YouTube video **(TODO: ADD VIDEO)** with no ads and streamed at a consistent quality (480p).
### Zen Mode
Before the start of experiment began, we prepared the machine by closing all applications, disabling
all notifications, disabling brightness adjusting. Display brightness and system volume were both fixed at 30% for the duration
of the experiment, this is discussed further in the [Limitation section](#limitations). Although a wired ethernet connection would have been preferable for network stability, it was not
nto feasible throughout the timeline of the project, so all trials were conducted over the same Wi-Fi network. We acknowledge this as a potential source of variance in our
measurements.

### Workflow
With our computer in "_zen mode_", we started a 5-minute warm-up phase in which we ran a Fibonacci sequence computation
to bring the CPU to a stable temperature and avoid cold-start effects in the early trials. After the warm-up,
we executed 120 trials (30 per condition) in a randomly shuffled order to mitigate any temporal correlations between
trials.

Between each trial, the system was left idle for 30 seconds to allow it to stabilize before the next measurement began.

Each trial proceeded the workflow as follows:

1. Opening Chrome browser in incognito mode with dark mode enabled via a pre-set YouTube cookie.
2. Navigating to the chosen YouTube video, accepting the cookies, and temporarily pausing playback.
3. Applying the designated YouTube setting for that trial.
4. Resuming playback and recording energy consumption using
   EnergiBridge [5] for 60 seconds of video playback.
5. Closing the browser and waiting 30 seconds before the next trial.

### Hardware/Software Details
- Model Name:	MacBook Air
- Model Identifier:	Mac14,2
- Chip:	Apple M2
- Total Number of Cores:	8 (4 performance and 4 efficiency)
- Memory:	8 GB
- Resolution:	2560x1664 Retina
- Refresh Rate:	60Hz

## Analysis

## Limitations
Since the settings are concerned with brightness and sound settings, the initial version of the experiment included highest brightness and volume on to the maximum setting. However ,
# References

[1] Global Media Insight. YouTube Users
Statistics. https://www.globalmediainsight.com/blog/youtube-users-statistics/#Daily_Active_Users_on_YouTube

[2] Tactiq. What is Ambient Mode on YouTube. https://tactiq.io/learn/what-is-ambient-mode-youtube

[3] Epic Lab. How YouTube's New Stable Volume Feature Destroys Your Carefully Crafted Audio
Mix. https://epic-lab.com/how-youtubes-new-stable-volume-feature-destroys-your-carefully-crafted-audio-mix/

[4] Nymynet. Voice Boost YouTube Explained: When and Why You Should Use
It. https://nymynet.com/voice-boost-youtube-explained-when-and-why-you-should-use-it/

[5] T. Durieux. EnergiBridge. GitHub. https://github.com/tdurieux/EnergiBridge/tree/main/src
