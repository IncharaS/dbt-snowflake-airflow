### **Project Title: Scalable Data Transformation Pipeline for TPCH Analytics Using DBT, Airflow, and Docker**

---

### **Project Overview**

This project demonstrates a robust **data transformation and analytics pipeline** designed to process and transform transactional data from the **TPCH Snowflake sample database**. Using **DBT (Data Build Tool)** for programmatic data transformations, **Airflow** for orchestration, and **Docker** for containerized deployment, the pipeline delivers analytics-ready tables optimized for business intelligence (BI) and reporting.

The environment is configured on **Windows** using **WSL (Windows Subsystem for Linux)** to run a Linux-based setup. It incorporates Ubuntu, Docker, and Airflow to ensure seamless integration for data engineering workflows.

---

### **Use Case**

The pipeline is tailored for a sample **e-commerce or supply chain domain** using transactional datasets from TPCH (e.g., `orders`, `lineitem`, `customer`, `parts`). It transforms raw data into structured staging, intermediate, and fact tables, enabling insights such as customer behavior, sales trends, and inventory optimization.

---

### **Key Features**

1. **Raw Data Ingestion**  
   - Pulls transactional data from the **TPCH Snowflake sample database**, including tables like `orders`, `lineitem`, `customer`, and `parts`.

2. **Data Cleaning and Transformation**  
   - Cleans and standardizes data, such as validating email formats, handling null values, and calculating fields like `discounted_amount` or `tax_included_price`.  
   - Transforms raw data into dimensions and metrics (e.g., `gross_item_sales_amount`, `total_price_with_tax`).

3. **Data Aggregation**  
   - Aggregates metrics at various granularities, such as:  
     - **Order-level**: Summing up sales and discounts.  
     - **Customer-level**: Total purchases and tax contributions.

4. **Business Metric Enrichment**  
   - Computes advanced metrics like **discounted amounts**, **tax-inclusive prices**, and **surrogate keys** for analytics-ready data.

5. **Model Creation**  
   - Produces:  
     - **Staging Models**: Cleans raw data for downstream processing.  
     - **Intermediate Models**: Joins datasets and applies business rules.  
     - **Fact Tables**: Finalized tables for BI dashboards.

6. **Automated Data Quality Checks**  
   - Employs rigorous tests for:  
     - **Primary Key Uniqueness**  
     - **Foreign Key Integrity**  
     - **Data Type Validation**

7. **Airflow Orchestration**  
   - Configures DAGs in **Airflow** to automate DBT tasks on a schedule, ensuring timely and consistent transformations.

---

### **Real-World Applications**

1. **Revenue and Order Analytics**  
   - Calculate revenue, taxes, and discounts across customers, products, and time periods.  
   - Identify top customers and high-performing products.

2. **Inventory and Supply Chain Optimization**  
   - Track sales trends for inventory planning and demand forecasting.  
   - Analyze part usage from the `lineitem` table to streamline supply chain operations.

3. **Customer Insights**  
   - Profile customers based on purchasing behavior and lifetime value.  
   - Validate customer data (e.g., email verification) for targeted marketing.

4. **Data-Driven Decision Making**  
   - Enables monitoring of KPIs such as sales performance and discount utilization.  
   - Provides a foundation for predictive analytics (e.g., demand forecasting).

---

### **Project Architecture**

| **Component**               | **Description**                                                                                           |
|-----------------------------|----------------------------------------------------------------------------------------------------------|
| **Staging Models**          | Organizes raw data into structured formats for easier downstream transformations.                        |
| **Intermediate Models**     | Applies joins, aggregations, and business logic to prepare enriched datasets.                            |
| **Fact Tables**             | Stores analytics-ready data with key metrics and dimensions for BI tools.                               |
| **Macros**                  | Modularized transformation logic for consistency and reusability across models.                         |
| **Tests**                   | Ensures data quality at every stage with automated checks for accuracy, integrity, and completeness.     |
| **Airflow DAGs**            | Automates DBT commands and schedules transformations for timely data updates.                           |
| **Docker**                  | Containerizes the environment for portability and reproducibility across systems.                        |

---

### **Technology Stack**

1. **DBT**: Core data transformation tool.  
2. **Airflow**: Workflow orchestration for automating DBT tasks.  
3. **Docker**: Containerization for deploying the pipeline in any environment.  
4. **Snowflake**: Cloud data warehouse for hosting the TPCH sample dataset.  
5. **Ubuntu (via WSL)**: Base environment for local development on Windows.

---

### **Workflow Diagram**
<img width="956" alt="image" src="https://github.com/user-attachments/assets/150c96cc-bed6-4a9a-8d19-291723fff400">


---

### **Value Proposition**

This project exemplifies a **scalable data engineering solution** for transforming and analyzing transactional datasets. By integrating cutting-edge tools like DBT and Airflow, it offers:  
- Structured workflows for data cleaning and transformation.  
- Reliable and tested data pipelines.  
- Ready-to-use analytics tables for decision-making.

The pipeline is an excellent demonstration of how modern data engineering tools can simplify and enhance complex analytics workflows, ensuring businesses derive actionable insights from their data. 




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://www.astronomer.io/docs/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://www.astronomer.io/docs/astro/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.
