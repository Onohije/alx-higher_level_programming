#!/usr/bin/python3
"""Takes the name of a state as an argument and lists all
cities of that state from the 'hbtn_0e_4_usa' database."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    _, user, passwd, db, state = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         password=passwd, db=db)
    c = db.cursor()
    num = c.execute("SELECT cities.name FROM cities INNER JOIN\
                      states on cities.state_id = states.id WHERE\
                      states.name = %s ORDER BY cities.id ASC", (state,))
    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=",")
    c.close()
    db.close()
