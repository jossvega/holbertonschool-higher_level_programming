#!/usr/bin/python3
# List state database hbtn_0e_0_usa
# Sintax: ./0-select_states.py username password database_name
from sys import argv
import MySQLdb

if __name__ == "__main__":
    if len(argv) != 4:
        exit()

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
