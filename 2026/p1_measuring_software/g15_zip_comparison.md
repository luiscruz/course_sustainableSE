---
author: Dragos Erhan, Tae yong Kwon, Priyansh Rajusth, Vincent Ruijgrok
group_number: 15
title: "Comparison of different file compression providers"
image: "img/g15_zip_comparison/zip.jpg"
date: 12/02/2026
summary: |-
  Zipping your files has become as ubiquotous as Googling for information or, by now, asking Chat (knowing as ChatGPT'ing). Zip archives are the standard in consumer and business data distribution. But there are multiple providers that can compress your folders. We will investigate if there's a difference, and if there is one choice, that could significantly influence our global ICT energy usage.
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

Compressing files before sending them over a slow connection, such as the Internet or a USB flash drive, has major benefits for both sides of the distribution. The sender compresses the files, which will take some time and energy, but it will almost always outweigh the advantage of sending fewer bytes over the connection. The receiver decompresses these files to completely restore the data. Everyone is happier for it.

However, there are many compression providers, each with its own trade-offs. Some provide better compression ratios at the cost of time and memory usage, while others offer lower compression ratios but are quicker at compression and inflation. 

In this project, we'll concern ourselves with four alternatives, each with its own advantages and disadvantages. We will provide a comprehensive overview of the compression ratios and energy usage per archive provider. We will concern ourselves with: PeaZip, 7-Zip, and gzip.
