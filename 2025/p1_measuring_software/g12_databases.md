---
author: Simon Biennier, Jasper Heijne, Paul Lindhorst, Huib Sprangers
title: "Measuring the Energy Consumption of SQL vs SQLite"
image: "https://miro.medium.com/v2/resize:fit:1200/1*VDoCtgMoTijXbq1P73PuFg.jpeg"
date: 28/02/2025
summary: |-
  In this paper we analyse the difference in energy consumption between usage of SQL and SQLite. After running our experiments and analysing the results, we find that the distribution is not as expected, and discuss why this might have been. Even still, we can see that the difference between the two is significant enough to conclude that SQLite is more energy efficient under the presented circumstances.
---

# Measuring the Energy Consumption of SQL vs SQLite

For our project, we decided to try measuring the difference between the energy consumption between SQL and SQLite. Specifically, we want to know if there is a significant difference between the two when making join operations. Specifically, we want to know which is more efficient for local testing for a single user. This experiment does not aim to find out which is more efficient for a production environment or at a larger scale. An example of a use case would be a developer who wants to locally run a testing set using SQL on a particular application, and wishes to find out if SQL or SQLite would be more energy efficient for this test.

The Structured Query Language[^sql], also reffered to as SQL or sequel, is a well-known cross-platform language most commonly used for managing relational databases. It is used to create, query, change, delete, define and control access to data. SQLite[^sqlite] is based on SQL as its parent language, but uses a local file system to store the database instead of a separate server process to run the database. For the standard SQL database, we made use of mySQL[^mysql].

## Experimental Setup

For our setup, we make use of Zen Mode in order to minimize superfluous energy usage. This means shutting off all processes not associated with the experiment. In addition, the screen brightness needs to be set as low as possible, bluetooth and wifi need to be turned off, airplane mode needs to be turned on and the battery consumption needs to be set to prioritize perfomance. In addition, to prevent the processor from needing to warm up during our experiment, offsetting the energy consumption results, we first run calculations on the CPU for about 1.5(?) minutes. 

In our experiment, we follow the magic number of repeating the experiment 30 times, pausing the process about a minute between each run in order to prevent tail energy consumption from previous runs from overflowing into the next. For consistency, the charger needs to either be connected or disconnected throughout the entire process. All this is in service to ensuring that as little energy as possible is used by applications that are not relevant to our experiment, and ensuring as little fluctuation in the power usage as possible, in order to most accurately be able to measure the energy consumption of making database requests.

The plan for our experiment is to run a version of the SQL database and make about 100(?) join requests, since a single operation would likely have too small of an energy profile by itself. This way, the energy profile of the requests should become clearer. After making these requests for the SQL database, we duplicate the experiment with the SQLite database. Due to both SQL variants making use the same kinds of requests, we can reuse the same operations, purely comparing the server based structure against the file based structure. Considering the server running in the background can also use up energy, it is recommended this server is process is ended while the SQLite process is running, by finishing the experiments on the standard SQL variant first.

The dataset we use for our experiment is a brazilian ecommerce record of around 100 thousand orders made to the Olist store[^dataset]. The software we use to measure the energy consumption will be energibridge[^energibridge], a cross-platform energy measurement program.

The code and setup we used, as well as instructions for how to run it, can be found on a specific branch for our github repository, linked in our references[^github].

### Hardware/Software Specifications

## Results
<!-- stat		             	p -->
<!-- shapiro mysql:	(0.9252632856369019, 	0.04153070226311684) -->
<!-- shapiro sqlite:	(0.915923535823822, 	0.021052313968539238) -->
<!-- #non-normal: -->
<!-- mannwhitneyu:	(870.0, 		            4.461750341666232e-11) -->

<!-- Mean difference: 37.283578806910015 -->
<!-- Percentage change: 49.46321041252181 -->
<!-- Cohen's d: 31.75638868642015 -->

<!-- mysql energy usage mean: 75.37638276198814 -->
<!-- sqlite mean: 38.092803955078125  -->

The following are the results of our experiment. First, we show the raw energy consumption by both forms of SQL:

![Raw Energy Consumption](../img/p1_measuring_software/g12_databases/Raw_energy.png)

After running the experiment we compare the energy usage of the SQL and SQLite databases. The results of the exepriment can be found in figure ![Raw Energy Consumption]. To compare the distributions we remove the outliers of the results (see figure ![mySQL]) and check if they are normally distributed. The experiment produced one outlier for the SQL database. To check normallity of the distributions we perform the Shapiro-Wilk test. This results in a p-value of 0.04153 for the SQL energy distribution and a p-value of 0.02105 for the SQLite energy distribution. This means both distributions are not normally distibuted. Therefore, to measure the significance of the difference of the distributions we perforn the Mann–Whitney U test, resulting in a U value of 870.0 and p-value of 4.46175 e-11 << 0.05. This signifies that the difference in distributions is significant.

The result of our mySQL runs, normalized with any glaring outliers removed (1 outlier):

![mySQL](../img/p1_measuring_software/g12_databases/mysql.png)

The result of our SQLite runs, also normalized with severe outliers removed (0 outliers):

![SQLite](../img/p1_measuring_software/g12_databases/sqlite.png)

The means of the SQL and SQLite distributions are 75.38 and 38.09 respectively. With a mean difference of 37.28 and percentage change of 49.46% we can cunclude that the difference is very significant. To further explore the effect size we compute the Cohen's d to indicate the standardised difference between two means, this results in a value of 31.76639. We will discuss these resutls in the following section.

## Conclusion

## Future Work

## References

[^github]: [https://github.com/HuibSprangers-leiden/course_sustainableSE/tree/code](https://github.com/HuibSprangers-leiden/course_sustainableSE/tree/code)

[^sql]: [https://www.iso.org/standard/76583.html](https://www.iso.org/standard/76583.html)

[^mysql]: [https://www.mysql.com/](https://www.mysql.com/)

[^sqlite]: [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)

[^dataset]: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

[^energibridge]: [https://github.com/tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge)

