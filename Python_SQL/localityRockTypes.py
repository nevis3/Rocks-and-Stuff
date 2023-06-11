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
        ('South Dakota', 'A'), 
        ('British Isles', 'B'), 
        ('Southwest USA', 'C'), 
        ('Upper Peninsula', 'D'), 
        ('Andes Mountains', 'E'), 
        ('Australia', 'F'), 
        ('Amazon Rainforest', 'G'), 
        ('Southern Africa', 'H');"""
    
    cursor.execute(sql_locality_rock_types_data)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


LocalityRockTypes()
