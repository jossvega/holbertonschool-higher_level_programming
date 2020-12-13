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
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name= %s
                ORDER BY cities.id ASC""",
                (argv[4],))
    query_rows = cur.fetchall()
    array_1 = []
    for row in query_rows:
        array_1.append(row[0])
    print(', '.join(array_1))
    """Close all cursors"""
    cur.close()
    """Close all databases"""
    conn.close()
