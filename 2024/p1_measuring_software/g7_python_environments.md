---
author: Smruti Kshirsagar, Esha Dutta, Giovanni Fincato de Loureiro
title: "Comparing Energy Consumptions of Python Execution Environments"
date: 28/02/2024
summary: |-
  abstract 
---

## Introduction
The TIOBE index, which is an indicator of the popularity of programming languages, shows that Python is currently ranked as the top programming language in 2024[^1]. It is vastly used in various software projects all around the world and executed through various environments. Python also remains a popular choice for data analysis and data science use cases due to its flexibility, scalability, and a wide range of libraries and tools which facilitate data manipulation easily. It's popularity can also be attributed to the fact that it is easy to learn and simple to use. \
However, very little is known about the energy consumption of the environments in which Python code is executed. In this experiment, we have chosen three ways to run a Python code which performs data analysis on a dataset; Jupyter notebook, PyCharm IDE, and through Python's command line interface. The Python code uses Pandas[^2] to read and perform some analysis queries on three e-commerce user behaviour datasets of sizes 1 GB, 2 GB, and 5 GB. \
In this article, we will begin by introducing each execution environment and discuss their strengths and weaknesses. Then, we will describe the methodology used to compare the energy consumption of each environment. Finally, we will present the results of our comparison and draw conclusions about the energy efficiency of each library. Overall, this report aims to provide valuable insights into the energy consumption of executing python code in different environments and how they can be run in a more sustainable way.

## Methodology

We use the Python library ```Pandas``` for data analysis. ```Pandas``` is selected since it offers a wide range of functionalities that make it a powerful tool for working with structured data. We perform operations such as read, groupby, sort and unique on the data. These operations are performed on a large dataset for different file sizes: 
* Full data size: 5,67 GB
* Half data size: 2,83 GB
* Quarter data size: 1,42 GB
 
The Python code is run on 3 environments:
* Terminal using CLI command
* PyCharm
* Jupyter Notebook

<img src="../img/p1_measuring_software/g7_python_environments/python_logo.png" alt="Python Logo" width="180"/><img src="../img/p1_measuring_software/g7_python_environments/pycharm_logo.png" alt="Pycharm Logo" width="180"/><img src="../img/p1_measuring_software/g7_python_environments/jupyter_logo.png" alt="Jupyter Logo" width="180"/>


The motivation is to find which of the environment is most energy efficient for data processing and while keeping in mind the trade-offs of functionalities they offer. Link to the repository can be found [here](<insert github link> "code_repository").

**Python CLI** \
Python from the Command Line Interface (CLI) using the terminal allows you to execute Python code and interact with Python's interpreter directly from the command line or terminal. Running Python from the terminal gives flexibility and control over Python scripts and allows user to interact with the system seamlessly.

**PyCharm** \
PyCharm is a powerful integrated development environment (IDE) specifically designed for Python development. Developed by JetBrains, PyCharm provides a wide range of features to enhance productivity, including code completion, syntax highlighting, debugging tools, version control integration, and code refactoring.

**Jupyter Notebook** \
Jupyter is an open-source web-based application that allows users to create and share documents containing live code, equations, visualizations, and narrative text. Notebooks consist of cells that can contain code, Markdown text, or raw content. Users can execute code cells interactively and see the results immediately within the notebook. Jupyter notebooks are widely used for data analysis, scientific computing, research, education, and collaborative projects. They enable reproducible research and facilitate the creation of interactive data-driven narratives.

### Dataset
We selected a dataset from Kaggle for the experiment . Link to the data can be found [here](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store/data "Kaggle Dataset"). \
It contains behavior data for 7 months (from October 2019 to April 2020) from a large multi-category online store. Each row in the file represents an event. All events are related to products and users. Each event is like many-to-many relation between products and users. The description of the columns is given below.


| Column        | Description                                                |
|---------------|------------------------------------------------------------|
| event_time    | Time when event happened at (in UTC).                      |
| event_type    | Only one kind of event: purchase.                          |
| product_id    | ID of a product                                            |
| category_id   | Product's category ID                                      |
| category_code | Product's category taxonomy (code name). Optional.         |
| brand         | Downcased string of brand name. Optional.                  |
| price         | Float price of a product.                                  |
| user_id       | Permanent user ID.                                         |
| user_session  | Temporary user's session ID. Same for each user's session. |

The python code performs the following operations:
* Reads data from CSV
* Computes count of total purchases per category
* Computes max and average spend for each user
* Computes the number of brands purchased by each user
* Computes number of distinct user ids, product ids, category ids and brands

Python code can be found [here](<insert github link> "main.py").

### Experiment Setup 
**Machine Specifications** \
The experiment was run on a MacBook Air. 

* **Model**  \
Name: MacBook Air (Model Identifier: MacBookAir10,1) \
System Firmware Version: 7459.121.3 \
OS Loader Version: 7459.121.3 \
Chipset Model: Apple M1 \
Total Number of Cores: 7 \ 
Vendor: Apple (0x106b) \
Metal Family: Supported, Metal GPUFamily Apple 7 \
RAM: 8 GB LPDDR4 
* **Graphics Processing Unit (GPU)** \
Type: Built-In \
Total Number of Cores: 8 (4 performance and 4 efficiency) 
* **Display** \
Type: Built-In Retina LCD \ 
Resolution: 2560x1600 Retina  

**Steps to obtain unbiased data**
In order to minimize competing tasks, the following steps are taken:
* All other applications are closed. It is also ensured that no background tasks are running.
* Notifications are turned off
* No external hardware is connected
* Laptop is put in flight mode
* Laptop is plugged in to charge
* Brightness is kept at a minimum
* Order of execution is shuffled
* There is one minute of sleep time between executions

**Experiment Automation**
Automation is done using a shell script found [here](<insert github link> "exec.sh"). Twenty readings are taken for each of the environment and file sizes. For each execution, the environment is launched, code is executed and energy readings for this process are stored to a CSV file. The order of execution is shuffled. Prerequisites for running the experiment are given below:
* Energibridge setup
* Python version : 
* Jupyter notebook version : 
* PyCharm version : 
* Open project in pycharm and add ```main.py``` to Pycharm > Preferences > Tools > Startup tasks
This step is required to ensure that the code runs on startup in PyCharm.

**Energy Measurement**
EnergiBridge is used to collect resource usage data. It uses LibreHardwareMonitor and measures CPU frequency, CPU usage, System power and Memory usage.

## Future Work
As part of future work, bigger datasets can be used for data analysis to emulate real world scenarios. In this experiment, we only used smaller datasets of sizes ranging approximately from 1 to 5 GB. Moreover, we have only used the pandas library in the Python code. In the future, the energy consumption of a wider variety of libraries and operations could be measured and compared. These steps would give us a more accurate picture of the energy consumption of data analysis scenarios that are employed in real-world software use cases. The code can also be run on different machines to investigate if that impacts the results. Lastly, one could argue that running code is not the only action a software engineer performs. A substantial amount of time is spent in developing and debugging software systems. Thus, in the future, the entire process of writing, debugging, and running the code can be simulated to measure energy consumption.

### References
[1]:[TIOBE Index](https://www.tiobe.com/tiobe-index/) \
[2]:[Pandas Documentation](https://pandas.pydata.org/docs/)