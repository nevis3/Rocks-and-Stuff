#only needs to run once

import psycopg2


def Locality():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5433",
        password="*")
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
        ('Southern Africa', 'South Africa'), 
        ('Western United States', 'USA'),
        ('Mediterranean Region', 'Cyprus'),
        ('Great Salt Lake', 'USA'),
        ('Himalayas', 'India'),
        ('Maritimes', 'Canada'),
        ('Pyrenees Mountains', 'France'), 
        ('Greek Islands', 'Greece'), 
        ('North Africa', 'Morocco'), 
        ('Permian Basin', 'USA'), 
        ('Black Forest', 'Germany'), 
        ('Yunnan Province', 'China'), 
        ('Okavango Delta', 'Botswana'),
        ('Ural Mountains', 'Russia'), 
        ('Hardangervidda', 'Norway'), 
        ('Patagonia', 'Argentina'), 
        ('Faroe Islands', 'Faroe');"""

    cursor.execute(sql_locality)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


Locality()
