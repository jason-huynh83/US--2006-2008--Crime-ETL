# US 2006-2008 Crime ETL pipeline
## Introduction
The purpose of this project was to create an ETL pipeline for analytical purposes. A pipeline was created while utilizing a Star Schema data model with Fact and Dimension tables where Data Analyst or Data Scientists are able to execute simple queries for analytical purposes.
## Dataset
The dataset that was used can be found [here](https://ucr.fbi.gov/crime-in-the-u.s/2006).
## Data Schema and Design
- **fact_table** - This table consists of all the measurable factors: 
	- State_id, City_id, Year_id, Population, ViolentCrime, MurderAndNonEgligentManslaughter, ForcibleRape, Robbery, AggravatedAssault, PropertyCrime, Burglary, LarcenyTheft, MotorVehicleTheft, Arson
- **city_dim** - Dimension table for Cities
	- City_id, City, State_id
- **state_dim** - Dimension table for States
	- State_id, State
- **year_dim** - Dimension table for Year
	- Year_id, Year
## Setup 
- Create a MySQL database to store all tables and data
- configure the following:
~~~
    conn = mysql.connector.connect (
        host = "",
        user = "",
        passwd = "",
        database = ""
        )
~~~
## Program Execution
- Run create_tables.py
	- create necessary staging, fact, and dimension tables
- Run crimeETL.py
	- runs the ETL pipeline to load and insert data to corresponding tables

## Files
- create_tables.py
	- create necessary staging, fact, and dimension tables
- crimeETL.py
	- runs the ETL pipeline to load and insert data to corresponding tables
- sql_queries.py
	- queries for creating, loading, and inserting tables
- clean.py
	- clean/transformations of data from dataset
- Crime Analysis.ipynb
	- Jupyter notebook for data analysis on US crime
	