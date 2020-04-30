# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:41:01 2020

@author: Jason
"""


# DROP TABLES
drop_table_dimState = 'DROP TABLE IF EXISTS state_dim'
drop_table_dimCity = 'DROP TABLE IF EXISTS city_dim'
drop_table_dimYear = 'DROP TABLE IF EXISTS year_dim'
drop_fact_table = 'DROP TABLE IF EXISTS fact_table'
drop_staging_table = 'DROP TABLE IF EXISTS staging_table'


# CREATE DIMENSION TABLES
create_state_dim = """CREATE TABLE IF NOT EXISTS state_dim (
                            State_id INT NOT NULL AUTO_INCREMENT,
                            State VARCHAR (256),
                            PRIMARY KEY (State_id))"""

create_city_dim = """CREATE TABLE IF NOT EXISTS city_dim (
                            City_id INT NOT NULL AUTO_INCREMENT,
                            City VARCHAR (256),
                            State_id INT,
                            PRIMARY KEY (City_id),
                            FOREIGN KEY (State_id) REFERENCES state_dim (State_id))"""

create_year_dim = """CREATE TABLE IF NOT EXISTS year_dim (
                            Year_id INT NOT NULL AUTO_INCREMENT,
                            Year INT,
                            PRIMARY KEY (Year_id))"""

# CREATE FACT TABLE
create_fact_table = """CREATE TABLE IF NOT EXISTS fact_table (
                            id INT NOT NULL AUTO_INCREMENT,
                            State_id INT,
                            City_id INT,
                            Year_id INT,
                            Population INT,
                            ViolentCrime INT,
                            MurderAndNonEgligentManslaughter INT,
                            ForcibleRape INT,
                            Robbery INT,
                            AggravatedAssault INT,
                            PropertyCrime INT,
                            Burglary INT,
                            LarcenyTheft INT,
                            MotorVehicleTheft INT,
                            Arson INT,
                            PRIMARY KEY (id)
                            )"""

# CREATE STAGING TABLE (might have to be all VARCHAR b/c of .csv file)
create_staging_table = """CREATE TABLE IF NOT EXISTS staging_table (
                            stage_id INT NOT NULL AUTO_INCREMENT,
                            ROWID INT,
                            State VARCHAR (256),
                            City VARCHAR (256),
                            Year VARCHAR (256),
                            Population INT,
                            ViolentCrime INT,
                            MurderAndNonEgligentManslaughter INT,
                            ForcibleRape INT,
                            Robbery INT,
                            AggravatedAssault INT,
                            PropertyCrime INT,
                            Burglary INT,
                            LarcenyTheft INT,
                            MotorVehicleTheft INT,
                            Arson INT,
                            Year_id INT,
                            City_id INT,
                            State_id INT,
                            PRIMARY KEY (stage_id)
                            )"""

                    
# INSERTING     
insert_state_table = """INSERT INTO state_dim (State)
                    SELECT DISTINCT 
                           State
                    FROM staging_table"""

insert_city_table = """INSERT INTO city_dim (City)
                    SELECT DISTINCT 
                           City
                    FROM staging_table"""

insert_Year_table = """INSERT INTO year_dim (Year)
                    SELECT DISTINCT 
                           Year
                    FROM staging_table"""
                    
insert_fact_table = """INSERT INTO fact_table (State_id, City_id, Year_id, Population, ViolentCrime, MurderAndNonEgligentManslaughter,
                                               ForcibleRape, Robbery, AggravatedAssault, PropertyCrime, Burglary,
                                               LarcenyTheft, MotorVehicleTheft, Arson)
                      SELECT DISTINCT State_id,
                             City_id, 
                             Year_id,
                             Population,
                             ViolentCrime,
                             MurderAndNonEgligentManslaughter,
                             ForcibleRape,
                             Robbery,
                             AggravatedAssault, 
                             PropertyCrime, 
                             Burglary,
                             LarcenyTheft,
                             MotorVehicleTheft,
                             Arson  
                    FROM staging_table"""

# QUERIES
drop_tables_queries = [drop_table_dimState, drop_table_dimCity, drop_table_dimYear, drop_fact_table, drop_staging_table]
create_tables_queries = [create_state_dim, create_city_dim, create_year_dim, create_staging_table, create_fact_table]
insert_tables_queries = [insert_state_table, insert_city_table, insert_Year_table, insert_fact_table]

