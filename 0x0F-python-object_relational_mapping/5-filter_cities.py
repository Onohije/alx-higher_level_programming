#!/usr/bin/python3
"""Takes the name of a state as an argument and lists all
cities of that state from the 'hbtn_0e_4_usa' database."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    _, user, passwd, db, state = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id
                 WHERE states.name=%s""", (sys.argv[4].))
    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=",")
    c.close()
    db.close()
