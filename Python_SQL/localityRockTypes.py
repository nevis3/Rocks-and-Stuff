#only needs to run once

import psycopg2


def LocalityRockTypes():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5432",
        password="asdf")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_locality_rock_types_data = """INSERT INTO locality_rock_types (locality_name, rock_type_id) VALUES
        ('South Dakota', '1a'), 
        ('British Isles', '1b'), 
        ('Southwest USA', '1c'), 
        ('Upper Peninsula', '1d'), 
        ('Andes Mountains', '2a'), 
        ('Australia', '2b'), 
        ('Amazon Rainforest', '2c'), 
        ('Southern Africa', '2d');"""
    
    cursor.execute(sql_locality_rock_types_data)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


LocalityRockTypes()
