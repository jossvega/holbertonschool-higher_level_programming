#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="192.168.1.55", user=argv[1], passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    """, to the end of argv[4] because second paramether is a tuple"""
    cur.execute("SELECT c.name \
                 FROM cities as c \
                 INNER JOIN states as s \
                 ON c.state_id = s.id \
                 WHERE s.name = %s \
                 COLLATE latin1_general_cs \
                 ORDER BY c.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    """Close all cursors"""
    cur.close()
    """Close all databases"""
    conn.close()
