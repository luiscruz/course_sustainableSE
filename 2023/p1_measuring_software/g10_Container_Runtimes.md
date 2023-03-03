---
author: Joey de Water, Leon de Klerk, Merlijn Mac Gillavry, Valentijn van de Beek
title: "Comparing Energy and Power consumption of different container runtimes"
image: "https://i.imgur.com/MDS86tT.png"
date: 03/03/2023
summary: "abstract Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
bibtex: |-
  @misc{cruz2021green,
    title = {Green Software Engineering Done Right: a Scientific Guide to Set Up Energy Efficiency Experiments},
    author = {Lu\'{i}s Cruz},
    year = {2021},
    howpublished={\url{http://luiscruz.github.io/2021/10/10/scientific-guide.html}},
    note = {Blog post.}
  }
---


# Comparing Energy and Power consumption of different container runtimes
![](https://i.imgur.com/MDS86tT.png)
## Introduction
Nowadays, most software is hosted on the cloud instead of on premise. To ensure scalability, compatibility and reliability on cloud hosted and also local machines, people turn to container runtime solutions. These container solutions also use less resources then other approaches like VMs or Hypervisors. In ___Sustainable Software Engineering___ good research tries to investigate sustainable solutions for widely used applications, practices and technologies. 

### What are container runtimes and what is their use? 
Virtualization is one of the most important pillars of modern computer engineering and a crucial element for safe, fair and scalable computing. The term is best described as creating a virtual instance of an operating system that uses some abstraction layer to make use of the underlying physical resources. Reasons for using virtualization technology may vary, but their main uses are:
- Allocating resources across muliple programs 
- Isolating instances of programs
- Reliable and transferable computing systems
- Testing programs that may otherwise not be able to run

There are many techniques for virtualization, but the main ones are (1) virtual machines, (2) virtualiation layers and (3) containers. Virtual machines are the heaviest form of virtualization in common use and refers to simulating a fictional computer with set resources. On a VM, programs can be run as if they are run on the virtual hardware which allows for complete isolation, full control and no interference, but causes high resource overhead. Virtualization layers (e.x. WINE or WSL) are layers built-in the kernels and translate system calls from the target OS to that of the  base OS. Such layers are uncommon, difficult to write and complex, but they do reduce the overhead significantly since only system calls need to be translated. Containers are the mildest form of virtualization since they reuse the original kernel and mainly focus on process isolation rather than full-on virtualazation. They are an evolution of the earlier UNIX feature of Change Root (chroot) which isolated the file system of process, by adding additional namespaces for networks, processes and stronger security garantuees. 

### Relevance 
According to a 2019 Survey by Portworx (a market research firm), with responses from 501 IT professionals, over 87% of the respondents stated that they were running container technologies with 90% of them also running them in production. Containerization is  widely prevalent in real-world applications and therefore a prime research topic when investigating sustainability in software engineering. With docker being the first and most well-known container runtime a natural question to ask is: 

___"Compared to alternatives, how energy and power efficient are docker containers?"___

This would be especially relevant if it turns out that docker uses more energy and power than its alternatives. In this blog we first discuss what container technologies are and which ones we chose to compare to docker. Then, we discuss our methodology and experiment setup to answer the question posed above. Next, we discuss our results and also find limitations to our work. Finally, we conclude our main findings and propose future work.

### Container Technologies (TODO: Valentijn)
The chosen container runtimes for our experiment are: 
![](https://i.imgur.com/bC11uqy.jpg)

#### [Podman](https://www.youtube.com/watch?v=1S2nuZsBz8g)
Something about Podman.

#### Docker

Something about Docker.

#### Containerd
Something about Containerd.

#### LXC
Something about LXC.

## Methodology <!-- (Joey) -->
To test the energy and power consumption of different container runtimes, we want to run multiple images, consisting of a database, website and reverse proxy, on these different container runtimes. We ran these images, tests and energy measurements on an intel powered Ubuntu (22.04 LTS) system. To ensure similar speeds over every cycle, which consists of building and running the images, running the tests and running the energy and power measurements, turbo-boost on CPU was disabled. Moreover, we set the screen bightness to a known value (max), plugged the laptop in, closed all unnecessary services and turned sleep off. Finally, we run our experiments in cycles to make sure that for every container there is the same warm up and cool down structure, which results in a reliable experiment.

### Container configuration
For our system under test we decided to create a setup containing a simple web application, database, and proxy.
This is a common use case for, personal, setups in containerized environments.
For simplicity we created a simple docker-compose file that would run all three services and expose their ports on the host system.
This docker-compose file could be run by docker, containerd (via a CLI tool called NerdCTL), and podman (via podman-compose).
Though specifically for podman there is a second file, podman-compose, in which the networking setup is changed to use the container hostnames instead of localhost to access the other containers.

For LXC we created one container based on the Alpine distribution image, in this we installed all required services with a shell script. Compared to the other runtimes, for LXC we only exposed port 80 for the proxy.

#### Database
For the database we used the standard PostgreSQL docker image. This image was configured with the user `postgres` with password `postgres`. We intialized Postgres with an empty database that is filled by the webapplication. It also exposes the default port on 5432.

For LXC we defined a script to install Postgres from the package repository, create the folders, and initialize the application.


#### Website
The website is a simple Medium-style blogging site called Conduit. The image itself is from the [Gobuff realworld project](https://github.com/remast/gobuff_realworld_example_app). This website allows for users to create accounts, login, write simple posts in Markdown, and view posts from other users. The website also runs migrations on startup to popuplate the database and is accessible on port 3000 by default.
The only configuration needed is a link to the database. 

For LXC we had to extract the build application file from a docker container and run it in the LXC container after everything was setup. It does also not expose port 3000 as we only defined port 80 to be exposed on the LXC container.


#### Reverse proxy
For the reverse proxy we used Nginx. This allows us to redirect any request on the external port 80 to the webapplication running at port 3000. 
For this we created a simple configuration called `nginx.conf` which was added to the containers. The Nginx image is taken from the default Docker repository. There is a second file called `podman-nginx.conf` which uses the hostname of the website,`web`, instead of `localhost` and is only used for podman.

As with the database, for LXC we had to manually install Nginx and enable the service on the Alpine image. The setup is the same as is done in the official Docker image and we also use the same configuration as with the other containers.


### Selenium tests
To automate interaction with the website, we chose to use Selenium. Selenium is an open-source automated testing framework. It is used to test web applications on different browsers. At the core of this framework is WebDriver, an interface designed to communicate directly and effectively with the browser. 

For our experiment we used Selenium WebDriver to headlessly run Chrome and interact with the web application. Through the following eight tests different pages were visited and interacted with: 

1. The first test, `open_main_page`, simply opens the main page and checks whether the WebDriver arrived.
2. The second test, `goto_login_page`, opens the main page, tries to find the login button and clicks it. Finally, it will check whether we actually arrived at the login page.
3. The third test, `goto_signup_page`, opens the main page, tries to find the sign up button and clicks it. Finally, it will again check whether we actually arrived at the sign up page.
4. In the fourth test, `create_account`, the WebDriver *drives* to the sign up page, fills in username, email and password, and creates an account.
5. In the fifth test, `login_account`, the Webdriver *drives* to the login page, fills in email and password, and logs into the account created in test 4.
6. The sixth test, `goto_account_page`, logs into the account created in test 4, tries to find the profile button and clicks it. Finally, it will check whether the WebDriver arrived at the account page.
7. The seventh test, `goto_article_page`, logs into the account created in test 4, tries to find the new article button and clicks it. Finally, it will check whether the WebDriver arrived at the article page.
8. In the final test, `publish_article`, the WebDriver *drives* through the Website to login to an account, created in a previous test, and publish an article.

Note: The order of the tests is maintained by naming them in alfabetical order.

### Energy measurements (Todo: Valentijn)
For each container runtime, the system service is brought up and the workload is started. After starting the workload, the selenium tests are run to emulate the usage of the site by some user. Finally, the power over this period is measured using 20s as the interval (which is the minimal time required for the test suite). Power is measured using the Powertop tool where the joules and the wattage are extracted. This process is repeated ten times before the system moves on to the next runtime. The averages of the joules and wattage are then reported together with the raw results.

## Results (Todo: Valentijn)
Show visualization of result data.
![](https://i.imgur.com/GbzSZaU.jpg)
![](https://i.imgur.com/yJZK11s.jpg)

## Discussion & Possible Future Work
Based on our work we have identified a few points of interests and limitations.
Additionally we also identify some options for possible future work that could be done on this topic.

The results of the baseline test are rather high compared to the other results. The baseline was run without any tests, therefore we expected this to have a lower power usage compared to the other tests. The most likely cause for the higher results is the use of a stress test before running the test suite. This was done with the intention to warm up the system, but when the test suite was actually run the system would cooldown. This is due to the fact that the test suite is not as load intensive as a stress test.

The first point directly relates to the second point, where the load of our test suite might have been too low. Compared to running a stress test on the host system, the containers used signicantly less resources, even when running our test suite. Based on the results we can see that under de current load we specified, simulating a single user, the differences are negligble between the different runtimes. But this might not be the case for different sizes and/or types of system load. This is therefore a limitation of our experiment. We propose the following options for future research to mitigate this limitation:
- First we could increase the load on the webserver. The current test suite only emulates the usage of the site by a single user. The test suite could be expanded to simulate a large number, e.g. thousands, of users connecting and interacting with the system at the same time.
- Another option is to run a stress test in the containers, similar to what we did on the host system when warming up the system. Running stress tests in the containers would make full use of the container's resources. This would more accurately model how the containers make use of the host resources and could also be used to compare power consumption between containerized applications and host applications.
- Lastly it would be intersting to test different types of loads between the different types of runtimes. Some examples include: encryption benchmarks; video encoding/decoding; blockchain applications; write benchmarks. These different types of benchmarks make use of different types of resources from the (host) system, therefore it would be useful to see how the different runtimes handle these types of resources. It could be the case the runtime A is better at handling high write loads compared to runtime B, and therefore has a lower power consumption for this kind of application.

Aside from the limitations in our system load, we also ran the different tests sequentially. Meaning that for example the baseline test was always first. We tried to mitigate interference of the different container services by disabling the other services when running a specific test. Additionally, as mentioned before, we also made sure that each test is run on a fresh container, e.g for docker we did a compose down after each test and a compose up before each test. A further improvement that we could make is to shuffle the order of test execution, such that the tests are not ordered per environment. This could result in changes in for example the results of the baseline test, if it is indeed the case that the results are affected by system temperature.

Additionally our LXC setup included only one container, compared to the three containers of the other runtimes. For LXC we combined the three services into one, due to some technical issues we ran into with the networking between LXC containers. Though based on our results this did not result in a drastically different power consumption of LXC compared to the other runtimes. It could be possible that with three containers the power consumption of the LXC setup would increase. Though it is unlikely that with three containers the consumption would decrease, and therefore LXC would either as efficient or less efficient compared to the other runtimes, but not more efficient, in this context. To mitigate this limitation, future improvements should split the LXC containers into three separate containers and update the LXC environment setup and test script to account for this. In addition we also had to manually add Nginx and PostgreSQL to the LXC container, compared to the already existing images we used for the other environments. Though the internal setup is the same as for the official images, the base image can differ slightly, which could impact the load of the container.

## Conclusion
As is evident from the results, the difference in power consumption between the different containers is very small in the given context. But as discussed before we can only conclude this in the context of our experiment, in a simple setup with low load on the system and containers. In this context we can conclude that Docker is equally efficient compared to some of its alternatives.

## Reproducibility
All scripts and code are available on [Github](https://github.com/leondeklerk/SSE). Together with a basic instruction on how to run the experiment yourself.