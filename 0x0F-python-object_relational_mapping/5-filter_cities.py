#!/usr/bin/python3
"""Takes the name of a state as an argument and lists all
cities of that state from the 'hbtn_0e_4_usa' database."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    c = db.cursor()
    c.execute("""
        SELECT cities.name FROM
        cities INNER JOIN states ON states.id=cities.state_id
        WHERE states.name=%s
    """, (state_name,))

    rows = c.fetchall()
    city_names = [row[0] for row in rows]
    print(*city_names, sep=",")

    c.close()
    db.close()
