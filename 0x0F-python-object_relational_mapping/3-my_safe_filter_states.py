#!/usr/bin/python3
"""
Safely displays all rows from the 'states' table in the 'hbtn_0e_0_usa'
database where the 'name' column matches the provided argument.
This script connects to a MySQL database using command-line arguments,
retrieves matching rows, and displays in ascending order by 'states.id'.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    _, user, passwd, db, name = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         password=passwd, db=db)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name = %s \
                ORDER BY states.id ASC", (name,))
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
