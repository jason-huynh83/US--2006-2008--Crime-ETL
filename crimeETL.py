# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:03:26 2020

@author: User
"""
import pandas as pd
import mysql.connector
from sql_queries import insert_tables_queries
import sqlalchemy

database_connection = sqlalchemy.create_engine("mysql+mysqlconnector://root:password123@localhost:3306/crime")
file_path = 'C:\\Users\\User\\Documents\\School\\code\\CrimeETL\\'

def load_staging_tables():
    #reading file in
    df = pd.read_csv(file_path + '06-08 Crime.csv', index_col = 0)
    
    #load staging table
    df.to_sql('staging_table', con = database_connection, if_exists = 'append', chunksize = 1000)   
    
def insert_tables(cur, conn):
    
    for query in insert_tables_queries:
        cur.execute(query)
        conn.commit()
    
def main():
    conn = mysql.connector.connect (
        host = "localhost",
        user = "root",
        passwd = "password123",
        database = "crime"
        )
    cur = conn.cursor()
    
    load_staging_tables()
    insert_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()

