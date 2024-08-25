#!/usr/bin/python3
"""
This script takes 4 arguments: MySQL username, MySQL password, database name,
and a state name. It safely displays all values in the `states` table where the
`name` matches the provided argument from the database `hbtn_0e_0_usa`.

The script is designed to be safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
