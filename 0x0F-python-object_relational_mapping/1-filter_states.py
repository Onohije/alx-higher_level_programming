#!/usr/bin/python3
"""Connects to the MySQL database using command-line arguments,
   retrieves and prints all rows from the 'states' table."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name
                 LIKE BINARY 'N%' ORDER BY states.id""")

    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    c.close()
    db.close()
