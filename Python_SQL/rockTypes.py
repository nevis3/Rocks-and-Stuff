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
        ('A', 'Gneiss', 'South Dakota', 'Metamorphic', '2.5 GA'),
        ('B', 'Basalt', 'British Isles', 'Sedimentary', '500 MA'),
        ('C', 'Dacite', 'Southwest USA', 'Igneous', '1 GA'),
        ('D', 'Dunite', 'Upper Peninsula', 'Sedimentary', '2.4 GA'),
        ('E', 'Kimberlite',  'Andes Mountains', 'Metamorphic', '1.7 GA'),
        ('F', 'Monzonite', 'Australia', 'Sedimentary', '700 MA'),
        ('G', 'Pegmatite', 'Amazon Rainforest', 'Igneous', '1.2 GA'),
        ('H', 'Obsidian', 'Southern Africa', 'Metamorphic', '2 GA');"""

    cursor.execute(sql_rock_types_data)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


RockType()
