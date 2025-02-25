---
author: Sofia Konovalova, Rafaël Labbé, Kaijen Lee, Violeta Macsim
title: "Sustainable Servers: Benchmarking energy consumption of various backend frameworks"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
  abstract Lorem ipsum dolor sit amet, consectetur adipisicing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
  reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
  pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
  culpa qui officia deserunt mollit anim id est laborum.
---

- Problem statement - why is our project important/relevant, real-world examples
- datacenters are very big energy consumptors -> can a frameworks make it slightly better?
- Relevant/useful things to read:
  - https://greensoftware.foundation/articles/how-to-measure-the-energy-consumption-of-your-backend-service
  - https://greenlab.di.uminho.pt/wp-content/uploads/2017/09/paperSLE.pdf
  - https://datacenters.lbl.gov/sites/default/files/Masanet_et_al_Science_2020.full_.pdf

# Introduction

With more people spending time online than ever before, the world generates nearly 400 million terabytes of data per day ([Statista, 2024](https://www.statista.com/statistics/871513/worldwide-data-created/)). As technological demands rise, backend servers must handle complex data streams, from video and audio to AI-powered applications, while maintaining low latency and high reliability. However, this increasing demand comes at a cost: in 2022, European data centers consumed **2.6% of global energy** ([European Commission, 2024](https://publications.jrc.ec.europa.eu/repository/handle/JRC135926)), and in 2023, US-based data centers consumed **4.4% of national energy expenditures**([Shehabi et. al., 2024](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf)). While a significant portion of this energy is used to cool servers  ([Jin et. al., 2020](https://www.sciencedirect.com/science/article/abs/pii/S0306261920303184)), the computational overhead of processing millions of backend requests per second also contributes significantly to their power consumption.

Given the massive energy demands of data centers, even minor improvements to backend frameworks could help reduce overall power consumption. Some frameworks handle requests more efficiently, requiring fewer CPU cycles or better utilizing system resources, resulting in lower energy consumption per request. But how big an impact can a backend framework really have? In this project, we compare the energy consumption of **Express.js**, **Spring Boot**, and **Flask** to see if software choices can help data centers become even more efficient.

## Backend frameworks
Backend frameworks are software tools that enable backend functionality in web applications. Their attributions range from server-side logic to database interactions, user authentication, and API communication. They ensure that data is processed between the server and the client.

When a user interacts with a website or app, for example, by submitting a form, making a purchase, or loading personalized content, the backend framework processes the request, retrieves the necessary data, and sends the response. This enables applications to run smoothly without requiring users to interact directly with the server or database.

### Express.js
**[Express.js](https://expressjs.com/)** is a _Node.js_ framework that simplifies server-side application development with its lightweight skeleton and customizable routing via middleware modules for both web and mobile applications. Its design enables developers to quickly create APIs and online apps by drawing on JavaScript's asynchronous event-driven architecture. Its adaptability allows it to work with a wide range of libraries, making it a popular choice for scalable, real-time applications.

### Flask
**[Flask](https://flask.palletsprojects.com/en/latest/)** is a simple _Python_ [microframework](https://medium.com/codex/what-are-microframeworks-best-ones-you-should-consider-using-f77eacc44dcb#9873) that offers the necessary tools for building a web app without any strict structure. Because of its lightweight nature, it is compatible with a wide range of other database management, form validation, and user authentication extensions. Flask's considerate design and ease of implementation make it an ideal choice for both small and rapidly evolving projects. 

### SpringBoot

# Methodology

## Experiment
- describe what steps are run in the automation script
- elaborate in the report how representative our experiment is, how does it simulate or reflect real-world use cases
- Docker + any other preparation steps are done _before_ energibridge begins collecting data in order to not take in data from trhe overhead generated by initialising a docker container

## Tools
- energibridge

## Hardware Specifications
- hardware specifications of the machine running the experiment

# Results
- Energy data analysis - how we draw conclusion for our result
- Violin box plot
- Simple joules over time comparison
- data significance with p-testin

## Limitations
- discuss limitations

# Conclusions


