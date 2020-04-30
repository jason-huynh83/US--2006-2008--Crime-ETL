# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:24:11 2020

@author: User
"""

import mysql.connector
from sql_queries import create_tables_queries, drop_tables_queries

def drop_tables(cur, conn):
    for query in drop_tables_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_tables_queries:
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

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()