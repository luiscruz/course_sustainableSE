---
author: Simon Biennier, Jasper Heijne, Paul Lindhorst, Huib Sprangers
title: "Measuring the Energy Consumption of SQL vs SQLite"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 28/02/2025
summary: |-
  Summary of our paper
---

# Measuring the Energy Consumption of SQL vs SQLite

For our project, we decided to try measuring the difference between the energy consumption between SQL and SQLite. Specifically, we want to know if there is a significant difference between the two when making join operations.

## Experimental Setup

For our setup, we make use of Zen Mode in order to minimize superfluous energy usage. This means that, to the best of our abilities, we shut off all processes not associated with the experiment. In addition, the screen brightness needs to be set as low as possible, bluetooth and wifi need to be turned off, airplane mode needs to be turned on and the battery consumption needs to be set to prioritize perfomance. All this is in service to ensuring that as little energy as possible is used by applications that are not relevant to our experiment, in order to most accurately be able to measure the energy consumption of making database requests.

The plan for our experiment is to run a version of the SQL database and make about 100(?) requests, since a single request would likely have a small energy profile by itself. This way, the energy profile of the requests should become clearer. After making these requests for the SQL database, we duplicate the experiment with the SQLite database. Due to both SQL variants making use of a 

The dataset we use for our experiment is the imdb database[^imdb], obtained through use of a python package called imdbpy[^dataset]. The software we use to measure the energy consumption will be energibridge[^energibridge], a cross-platform energy measurement program.

### Hardware/Software Specifications

## Results

## Conclusion

## Future Work

## References

[^imdb]: [https://www.imdb.com/](https://www.imdb.com/)

[^dataset]: [https://github.com/MaximShidlovski23/imdbpy](https://github.com/MaximShidlovski23/imdbpy)

[^energibridge]: [https://github.com/tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge)

