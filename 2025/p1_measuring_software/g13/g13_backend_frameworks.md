---
author: Sofia Konovalova, Kaijen Lee, Violeta Macsim
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

# Introduction

With more people spending time online than ever before, the world generates nearly 400 million terabytes of data per day ([Statista, 2024](https://www.statista.com/statistics/871513/worldwide-data-created/)). As technological demands rise, backend servers must handle complex data streams, from video and audio to AI-powered applications, while maintaining low latency and high reliability. However, this increasing demand comes at a cost: in 2022, European data centers consumed **2.6% of global energy** ([European Commission, 2024](https://publications.jrc.ec.europa.eu/repository/handle/JRC135926)), and in 2023, US-based data centers consumed **4.4% of national energy expenditures**([Shehabi et. al., 2024](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf)). While a significant portion of this energy is used to cool servers  ([Jin et. al., 2020](https://www.sciencedirect.com/science/article/abs/pii/S0306261920303184)), the computational overhead of processing millions of backend requests per second also contributes significantly to their power consumption.

Given the massive energy demands of data centers, even minor improvements to backend frameworks could help reduce overall power consumption. Some frameworks handle requests more efficiently, requiring fewer CPU cycles or better utilizing system resources, resulting in lower energy consumption per request. But how big an impact can a backend framework really have? In this project, we compare the energy consumption of **Express.js**, **Spring Boot**, and **Flask** to see if software choices can help data centers become even more efficient.

## Backend frameworks
Backend frameworks are software tools that enable backend functionality in web applications. Their attributions range from server-side logic to database interactions, user authentication, and API communication. They ensure that data is processed between the server and the client.

When a user interacts with a website or app, for example, by submitting a form, making a purchase, or loading personalized content, the backend framework processes the request, retrieves the necessary data, and sends the response. This enables applications to run smoothly without requiring users to interact directly with the server or database.

### Express.js
**[Express.js](https://expressjs.com/)** is a _Node.js_ framework that simplifies server-side application development with its lightweight skeleton and customizable routing via middleware modules for both web and mobile applications. Its design enables developers to quickly create APIs and online apps by drawing on JavaScript's asynchronous event-driven architecture. Its adaptability allows it to work with a wide range of libraries, making it a popular choice for scalable, real-time applications.

### Flask
**[Flask](https://flask.palletsprojects.com/en/latest/)** is a simple _Python_ [microframework](https://medium.com/codex/what-are-microframeworks-best-ones-you-should-consider-using-f77eacc44dcb#9873) that offers the necessary tools for building a web app without any strict structure. Because of its lightweight nature, it is compatible with a wide range of other database management, form validation, and user authentication extensions. Flask's considerate design and ease of implementation make it an ideal choice for both small and rapidly evolving projects. 

### SpringBoot
[**SpringBoot**](https://spring.io/projects/spring-boot) is a powerful open-source Java framework included in the Spring package that provides solutions for various products. This framework automatically configures the boilerplate, giving you the freedom to add whatever extensions you want. It provides support for database connections, authentication services, and web servers. Spring enables developers to build scalable, production-ready applications with minimal setup time.


# Methodology 

We created a containerized Docker environment for each framework, resulting in three isolated server instances. Using Docker containers, we eliminate unnecessary local processes and ensure that energy measurements reflect only the server's activity. Each container runs solely on developer-supplied resources, leading to more consistent data.

To simplify the setup, we extracted two `.tsv` files` from the [IMDb database](https://developer.imdb.com/non-commercial-datasets/), each containing 50,000 movies and industry professionals. Instead of connecting to an external database, the data is loaded directly into each server during startup, simplifying configuration and accelerating deployment. This practice also mitigates any potential caching, as data is erased when the container is deleted.

## Tools
To measure the energy consumption of **Flask**, **Express.js**, and **Springboot**, we set up a reproducible testing repository with minimal external interference. Let's take a closer look at how we organized the experiment!

[**Energibridge**](https://github.com/tdurieux/energibridge) is a command-line tool for measuring the energy consumption of computer processes that can be integrated into a containerized development pipeline. In our case, the process would be the currently running server. The tool outputs the values as `.csv` files, allowing you to track your operations' "energy footprint".

For each framework, we use the [Apache Benchmark](https://httpd.apache.org/docs/2.4/programs/ab.html) as it is lightweight and comes installed in most Unix systems. Using this benchmarking tool, we can specify the amount of requests we want to be made concurrently. In our case, we make 10,000 requests with 150 concurrent requests.

The experiment was automated with the use of a bash script. Before any measurements are taken, the script builds the necessary Docker containers, waits 15 seconds, and then begins energy measurements as the benchmarking tool is run. At the end of the run, the docker container is torn down and the script waits for 60 seconds before continuing on with the next iteration or framework in order to prevent as much tail energy consumption as possible.

## Hardware Specifications

The experiment is performed by running the automation bash script on a Linux laptop, running no other services and warmed up before the script is run by running some intensive tasks. The laptop was kept in a room-temperature room, with the laptop plugged in to a power supply throughout the whole experiment. The only external package in use during this experiment was a package called "caffeine" which disabled sleep after a period of inactivity.

| Laptop | Dell XPS13 |
| ------ | ------------------ |
| CPU    | Intel Core i7-6700HQ @ 2.6GHz |
| RAM    | 8 GB      |
| GPU    | Intel TigerLake-LP GT2  |
| OS     | Pop_OS! 22.04 Jammy    |

##### Table 1: Laptop specifications used in our experiment

# Results
- Energy data analysis - how we draw conclusion for our result
- Violin box plot
- Simple joules over time comparison
- data significance with p-testin

## Limitations
- discuss limitations

# Conclusions


