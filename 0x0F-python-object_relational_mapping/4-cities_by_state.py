#!/usr/bin/python3
"""Lists all cities from the 'hbtn_0e_4_usa' database."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    _, user, passwd, db = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         password=passwd, db=db)
    c = db.cursor()
    c .execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states on cities.state_id = \
                states.id ORDER BY cities.id ASC")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
