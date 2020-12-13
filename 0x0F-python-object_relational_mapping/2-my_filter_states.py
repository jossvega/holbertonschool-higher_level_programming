#!/usr/bin/python3
"""script that takes in an argument
   and displays all values in the states table"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}'\
                 ORDER BY id".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
