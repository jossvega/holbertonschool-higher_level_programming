#!/usr/bin/python3
"""script that lists all states with
   a name starting with N (upper N)"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="192.168.1.55", user=argv[1], passwd=argv[2],
                           conn=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
