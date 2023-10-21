#!/usr/bin/python3
import psycopg2
from psycopg2 import sql
from collections import Counter
from colors_data import colors_data

all_colors = [color for colors in colors_data.values() for color in colors]

conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
cur = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(50),
        frequency INT
    );
'''
cur.execute(create_table_query)
conn.commit()

for color, frequency in Counter(all_colors).items():
    insert_query = sql.SQL("INSERT INTO color_frequencies (color, frequency) VALUES ({}, {});").format(
        sql.Literal(color), sql.Literal(frequency)
    )
    cur.execute(insert_query)
    conn.commit()

cur.close()
conn.close()
