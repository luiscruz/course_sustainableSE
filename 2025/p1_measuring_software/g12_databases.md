---
author: Simon Biennier, Jasper Heijne, Paul Lindhorst, Huib Sprangers
title: "Measuring the Energy Consumption of SQL vs SQLite"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
  Summary of our paper
---

# Measuring the Energy Consumption of SQL vs SQLite

For our project, we decided to try measuring the difference between the energy consumption between SQL and SQLite. Specifically, we want to know if there is a significant difference between the two when making join operations. Specifically, we want to know which is more efficient for local testing for a single user. This experiment does not aim to find out which is more efficient for a production environment or at a larger scale. An example of a use case would be a developer who wants to locally run a testing set using SQL on a particular application, and wishes to find out if SQL or SQLite would be more energy efficient for this test.

The Structured Query Language[^sql], also reffered to as SQL or sequel, is a well-known cross-platform language most commonly used for managing relational databases. It is used to create, query, change, delete, define and control access to data. SQLite[^sqlite] is based on SQL as its parent language, but uses a local file system to store the database instead of a separate server process to run the database.

## Experimental Setup

For our setup, we make use of Zen Mode in order to minimize superfluous energy usage. This means that, to the best of our abilities, we shut off all processes not associated with the experiment. In addition, the screen brightness needs to be set as low as possible, bluetooth and wifi need to be turned off, airplane mode needs to be turned on and the battery consumption needs to be set to prioritize perfomance. All this is in service to ensuring that as little energy as possible is used by applications that are not relevant to our experiment, in order to most accurately be able to measure the energy consumption of making database requests.

The plan for our experiment is to run a version of the SQL database and make about 100(?) join requests, since a single operation would likely have too small of an energy profile by itself. This way, the energy profile of the requests should become clearer. After making these requests for the SQL database, we duplicate the experiment with the SQLite database. Due to both SQL variants making use the same kinds of requests, we can reuse the same operations, purely comparing the two database variants.

The dataset we use for our experiment is a brazilian ecommerce record of around 100 thousand orders made to the Olist store[^dataset]. The software we use to measure the energy consumption will be energibridge[^energibridge], a cross-platform energy measurement program.

### Hardware/Software Specifications

## Results

## Conclusion

## Future Work

## References

[^sql]: [https://www.iso.org/standard/76583.html](https://www.iso.org/standard/76583.html)

[^sqlite]: [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)

[^dataset]: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

[^energibridge]: [https://github.com/tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge)

