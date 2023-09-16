#!/usr/bin/python3
"""
Displays all rows from the 'states' table in the 'hbtn_0e_0_usa' database
where the 'name' column matches the provided argument.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    _, user, passwd, db, name = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         password=passwd, db=db)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name = '{}' \
                ORDER BY states.id ASC".format(name))
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
