#only needs to run once

import psycopg2


def Locality():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5432",
        password="asdf")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_locality = """INSERT INTO localities (name, country) VALUES
                ('South Dakota', 'USA'), 
        ('British Isles', 'England'), 
        ('Southwest USA', 'USA'), 
        ('Upper Peninsula', 'USA'), 
        ('Andes Mountains', 'Chile'), 
        ('Australia', 'Australia'), 
        ('Amazon Rainforest', 'Brazil'), 
        ('Southern Africa', 'South Africa');"""

    cursor.execute(sql_locality)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


Locality()
