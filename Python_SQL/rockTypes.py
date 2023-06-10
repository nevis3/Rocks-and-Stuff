#only needs to run once

import psycopg2


def RockType():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5432",
        password="asdf")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_rock_types_data = """INSERT INTO rock_types (ID, Name, Locality_name, Type, Age) VALUES
        ('1a', 'Gneiss', 'Metamorphic', 'South Dakota', '2.5 GA'),
        ('1b', 'Basalt', 'Sedimentary', 'British Isles', '500 MA'),
        ('1c', 'Dacite', 'Igneous', 'Southwest USA', '1 GA'),
        ('1d', 'Dunite', 'Sedimentary', 'Upper Peninsula', '2.4 GA'),
        ('2a', 'Kimberlite', 'Metamorphic', 'Andes Mountains','1.7 GA'),
        ('2b', 'Monzonite', 'Sedimentary', 'Australia','700 MA'),
        ('2c', 'Pegmatite', 'Igneous', 'Amazon Rainforest', '1.2 GA'),
        ('2d', 'Obsidian', 'Metamorphic', 'Southern Africa', '2 GA');"""

    cursor.execute(sql_rock_types_data)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


RockType()
