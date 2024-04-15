# Data Engineering Project oregon_crime_de_project_with_gcp


## Problem Statement: Consolidation and Preservation of Crime Data in Oregon

**Background:**
Crime data is a critical resource for law enforcement, policymakers, researchers, and the public to understand crime trends, develop safety strategies, and allocate resources effectively. In Oregon, crime data is currently distributed across various platforms and is only available in CSV format on the police public data websites. This scattered data structure poses significant challenges in terms of accessibility, analysis, and long-term data preservation.

**Current Challenge:**
The primary issue with the existing setup is the fragmentation of crime data across multiple repositories, each maintained independently by various law enforcement agencies within Oregon. This data is presented in non-uniform formats and is not integrated, making comprehensive analysis cumbersome and time-consuming. Additionally, each year the oldest data is removed from the public websites, leading to a loss of valuable historical crime records. This practice not only hinders the ability to perform longitudinal studies but also affects the accuracy of crime trend analysis and forecasting.

**Proposed Solution:**
To address these challenges, there is a pressing need to develop a centralized data warehouse that consolidates all crime data across Oregon. This solution involves the following strategic actions:

1. **Data Collection and Integration:**
   - Establish a protocol for collecting annual crime data from all relevant law enforcement agencies in Oregon.
   - Standardize data formats to ensure uniformity, making the data easier to process and analyze.

2. **Data Warehouse Development:**
   - Design and implement a secure data warehouse that can store large volumes of crime data efficiently.
   - Ensure that the warehouse supports scalable and flexible data models to accommodate various types of crime data and potential future requirements.

3. **Historical Data Preservation:**
   - Implement procedures to regularly update the data warehouse with new data while maintaining all historical data.
   - Develop archival strategies to safeguard data integrity and ensure that data is not lost over time.

4. **Access and Security Measures:**
   - Provide controlled access to the data warehouse, allowing researchers, policymakers, and public stakeholders to retrieve and analyze data as needed.
   - Ensure robust security measures to protect sensitive data and comply with legal and ethical standards.

5. **Ongoing Maintenance and Support:**
   - Establish a dedicated team to manage the data warehouse operations, including data updates, system upgrades, and user support.
   - Monitor and evaluate the system performance regularly to ensure it meets the evolving needs of its users.

**Expected Benefits:**
Implementing this solution will provide multiple benefits:
   - **Enhanced Accessibility:** Centralizing crime data will make it more accessible to stakeholders, enabling more effective data sharing and collaboration.
   - **Improved Data Utilization:** A unified data model will facilitate more comprehensive and sophisticated analyses, improving our understanding of crime patterns and effectiveness of crime prevention strategies.
   - **Preservation of Historical Data:** Maintaining a complete historical dataset will enhance the quality of research and allow for accurate trend analysis and forecasting.
   - **Cost Efficiency:** Reducing data redundancy and streamlining data management processes will lower costs related to data storage and maintenance.

By consolidating crime data into a single, well-managed data warehouse, Oregon can enhance its crime analysis capabilities, preserve valuable data for future generations, and ultimately foster a safer and more informed community.

## Resources 
- Create GCP account
- Create ssh key to connect to the cloud resources
- Install terraform
- Create Python enviroment for the project with the libraries needed 
- Install MageAI

## Create and set up GCP account
See documentation [here](gcp.md)

## Create ssh key and connect to the cloud
SSH link [here](https://cloud.google.com/compute/docs/connect/create-ssh-keys)

Steps in the video [here](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=14)

## Install terrafomr
See documentation [here](terraform_setup.md)

## Create Python enviroment in the project folder
See documentation [here](python_env_creation.md)

## MageAI installation with Docker
- Install Docker. [Docker installation process here: ](https://docs.docker.com/engine/install/)

Run after installing docker inside the project folder
```bash
docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start mage-oregon-crime
```

## Download the project repository.

```bash
git clone https://github.com/DRPproton/oregon_crime_de_project_with_gcp.git
```

- Download the service account key from GCP
- Add the path of the credential to the variables.tf file inside the folder "terrafile"

Run
```bash
terraform init
terraform plan
terraform apply
```
More help in the [file.](terraform_setup.md)

## Set up and run pipelines
> Replace the files magic-oregon-crime with the files inside magic-oregon-crime-piplines.

> Replace line 40 in the io_config.yaml with the path of the service account key (You should make a coty of the file inside the folder)


Run pipelines:
- oregon_crime_etl	
- uniform_arrest_data	
- uniform_leoka_data	
- uniform_offenses_data	
- uniform_victims_data


## Run Noetbook to trasform the data and load back to GCS

Run 
```bash
jupyter notebook
```

- Run the notebook data_trans_spark.ipynb

### After running notebook  run pipelines 

- arrests_to_bigquery	
- crime_to_bigquery	
- leoka_to_bigquery	
- offenses_to_big_query	
- victims_to_bigquery	


## Table Partition in BigQuery

> In GCP BigQuery run the queries provided in the file "**queries_for_partition**" [file here](queries_for_partition)

## Report file 
> The report was built in PowerBi. A copy of the report is in the file [oregon_crime_report](oregon_crime_report.pdf)

> The file used to made the reports is "**oregon_crime_report.pbix**"

### To reproduce the report
- First download PowerBi Desktop
- Connect PowerBi to BigQuery
