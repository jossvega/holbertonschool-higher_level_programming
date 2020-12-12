#!/usr/bin/python3
# script that lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa

if __name__ == "__main__":

    import sys
    import MySQLdb

    if len(argv) != 4:
        exit()
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           conn=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
