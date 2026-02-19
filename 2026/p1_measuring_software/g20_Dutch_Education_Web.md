---
author: Ocean Wang, Erkin Başol, Yasar Kocdas
group_number: 20
title: "Comparing Dutch education apps"
image: "img/gX_template/project_cover.png"
date: 12/02/2026
summary: |-
  Comparison of highschool education websites. We will benchmark multiple use-case features across 2 websites. Somtoday and Magister. 
  First visit (cold cache) vs repeat visit (warm cache)
  Single tab vs multiple tab
  Timetable loading
  Grades loading
  Sending and Loading Messages
  Opening a pdf that is loaded in the app
  Attendancy loading in websites
  
  
identifier: p1_measuring_software_2026 # Do not change this
all_projects_page: "../p1_measuring_software" # Do not change this
---

## 

## Project Topic:

We want to compare the energy consumption of **Somtoday** and **Magister**, two websites that almost every Dutch high school student uses daily. They both offer the same core features (timetables, grades, messages, attendance, documents) but are built by different companies. On top of comparing the two websites, we also look at how caching and having multiple tabs open affects energy usage.

### Motivation

Millions of students visit these websites every day, yet nobody has looked into how much energy they actually consume. Even small differences per session could matter at that scale. We think it is worth investigating.

### Research Question

**How does the energy consumption of common student workflows differ between the Somtoday and Magister websites, and how do caching and multi-tab usage affect consumption?**

### Methodology

We run all experiments on the same machine, browser, OS, and network connection. Energy is measured using **EnergiBridge**. Each scenario is repeated multiple times to get reliable results.

The scenarios we test on both websites are: timetable loading, grades loading, sending and loading messages, opening a PDF, and attendance loading. For each of these we also compare cold cache (first visit) vs. warm cache (repeat visit) and single tab vs. multiple tabs open.

We plan to automate the browser interactions with Selenium or Playwright and will publish a replication package alongside our results.

### Expected Outcomes

We expect warm cache visits to use less energy than cold cache ones, and having multiple tabs open to increase consumption. Between the two websites, differences could come from things like page size, how much JavaScript runs, or how many network requests are made. We will present everything in a blog-style report of around 2500 words with charts comparing the results.



