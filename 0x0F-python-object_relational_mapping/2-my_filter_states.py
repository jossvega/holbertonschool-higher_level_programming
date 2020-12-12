#!/usr/bin/python3
# script that takes in an argument and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument.
# sintax: mysql username, mysql password, database name and state name searched

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="192.168.1.55", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
               WHERE name = '{}'".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
