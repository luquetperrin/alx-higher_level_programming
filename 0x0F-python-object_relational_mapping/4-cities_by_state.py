#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>")
        exit(1)

    try:
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])

        with db.cursor() as cur:
            cur.execute("""
                SELECT
                    cities.id, cities.name, states.name
                FROM
                    cities
                JOIN
                    states
                ON
                    cities.state_id = states.id
                ORDER BY
                    cities.id ASC
            """)

            rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        if db:
            db.close()
