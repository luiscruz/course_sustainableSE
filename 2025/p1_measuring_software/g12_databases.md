---
author: Simon Biennier, Jasper Heijne, Paul Lindhorst, Huib Sprangers
title: "Measuring the Energy Consumption of SQL vs SQLite"
image: "https://miro.medium.com/v2/resize:fit:1200/1*VDoCtgMoTijXbq1P73PuFg.jpeg"
date: 28/02/2025
summary: |-
  In this paper we analyse the difference in energy consumption between usage of SQL and SQLite. After running our experiments and analysing the results, we find that the distribution is not as expected, and discuss why this might have been. Even still, we can see that the difference between the two is significant enough to conclude that SQLite is more energy efficient under the presented circumstances.
---

# Measuring energy consumption of SQL databases

For our project, we decided to try measuring the difference between the energy consumption between SQL and SQLite. Specifically, we want to know if there is a significant difference between the two when making join operations. Specifically, we want to know which is more efficient for local testing for a single user. This experiment does not aim to find out which is more efficient for a production environment or at a larger scale. An example of a use case would be a developer who wants to locally run a testing set using SQL on a particular application, and wishes to find out if SQL or SQLite would be more energy efficient for this test.

The Structured Query Language[^sql], also reffered to as SQL or sequel, is a well-known cross-platform language most commonly used for managing relational databases. It is used to create, query, change, delete, define and control access to data. SQLite[^sqlite] is based on SQL as its parent language, but uses a local file system to store the database instead of a separate server process to run the database. For the standard SQL database, we made use of mySQL[^mysql].

The plan for our experiment is to run select queries on these two versions of SQL, namely MySQL and SQLite. Due to both SQL variants making use the same kinds of requests, we can reuse the same operations, purely comparing the server based structure against the file based structure.

## Experimental setup

This project will use a Brazilian ecommerce public dataset of orders made at Olist Store, containing real world commercial data which has been anonymised. "The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers."[^dataset]

From this dataset, we used 5 tables, namely 'customers' (99441 rows), 'geolocation' (1000163 rows), orders (99441 rows), 'products' (32951 rows), 'sellers' (3095 rows).

For our setup, we made use of 'zen mode' in order to minimise superfluous energy usage, not relevant to the measurements. This meant shutting off all processes not associated with the experiment, connecting only required hardware, turning off notifications, setting screen brightness to a (fixed) minimum, turning off bluetooth and wifi. Moreover, for consistency and accuracy, we disconnected power from the computer during the whole experiment. Finally, to warm up the system (and thus the processor) during our experiment, we first ran five queries to both databases totaling about 100 seconds.

The experiment follows the magic number of experiments, repeating 30 times for each database (for a total of 60), with 1 select-all query to each of the 5 tables per experiment.

One experiment, i.e. the queries to all tables, would take approximately 2-3 seconds each. As such, we incorporated 20 seconds (slightly lower than the usual 1 minute) of rest after each test run, which we thought should be enough in order to prevent tail energy consumption from previous runs from overflowing into the next. We considered several factors, namely the fact that the experiments are not extremely resource-intensive and we also open and close connections each time to mitigate caching effects.

Finally, of note is that the order of testing the databases was shuffled in order to try and circumvent any confounding factors as much as possible.

### Specifications

The experiment was conducted at a temperature of 18.5 degrees Celsius.

The hardware used to run the experiments was as follows:

- OS: Windows 11
- CPU: Intel Core i7-10750H @ 2.60GHz
- RAM: 16GB
- Storage: 512GB SSD

As for software, we used:

- Python 3.10.0
- MySQL 8.0.41 (Windows x86, 32-bit)
- SQLite 3.49.1 (Windows x64, 64-bit).

To measure energy consumption EnergiBridge[^energibridge], a cross-platform energy measurement program, was used.

## Results

The following are the results of our experiment. First, we show the raw energy consumption by both forms of SQL:

![Raw Energy Consumption](../img/p1_measuring_software/g12_databases/Raw_energy.png)

Next, we show the result of our mySQL runs, normalized with any glaring outliers removed:

![mySQL](../img/p1_measuring_software/g12_databases/mysql.png)

And finally, we show the result of our SQLite runs, also normalized with severe outliers removed:

![SQLite](../img/p1_measuring_software/g12_databases/sqlite.png)

## Discussion

Not normally distributed, but still signifcant diff

### Future work

As stated previously, the experiments might not be resource-intensive enough to have a significant impact on the energy consumption. Therefore, it would be interesting to enhance the experiment by running more SQL queries in succession, resulting in a higher energy profile.

Moreover, the MySQL server is a service running permanently in the background, and to remove any noise from this process it would be better to run the standard SQL variant first and quit the server after, so it doesn't affect the energy consumption of the SQLite experiment.

## Conclusion

## References

[^github]: [https://github.com/HuibSprangers-leiden/course_sustainableSE/tree/code](https://github.com/HuibSprangers-leiden/course_sustainableSE/tree/code)
[^sql]: [https://www.iso.org/standard/76583.html](https://www.iso.org/standard/76583.html)
[^mysql]: [https://www.mysql.com/](https://www.mysql.com/)
[^sqlite]: [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)
[^dataset]: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
[^energibridge]: [https://github.com/tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge)
