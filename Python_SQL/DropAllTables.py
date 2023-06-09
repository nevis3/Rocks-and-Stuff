#only needs to run once

import psycopg2


def Drop():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5433",
        password="*")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_locality = """
    DROP TABLE IF EXISTS localities, locality_rock_types, rock_types, samples CASCADE;
    """

    cursor.execute(sql_locality)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


Drop()
