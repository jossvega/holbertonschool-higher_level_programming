#!/usr/bin/python3
"""AVOID SQL INJECTIONS. script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                 ORDER BY id", (argv[4],))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    """Close all cursors"""
    cur.close()
    """Close all databases"""
    conn.close()
