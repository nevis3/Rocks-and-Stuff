#only needs to run once

import psycopg2


def LocalityRockTypes():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5433",
        password="*")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_locality_rock_types_data = """INSERT INTO locality_rock_types (locality_name, rock_type_id) VALUES
        ('South Dakota', 'Au'), 
        ('British Isles', 'Ag'), 
        ('Southwest USA', 'Cu'), 
        ('Upper Peninsula', 'Fe'), 
        ('Andes Mountains', 'Pb'), 
        ('Australia', 'Zn'), 
        ('Amazon Rainforest', 'Al'), 
        ('Southern Africa', 'Ti'), 
        ('Western United States', 'SiO2'),
        ('Mediterranean Region', 'CaCO3'),
        ('Great Salt Lake', 'NaCl'),
        ('Himalayas', 'KAlSi3O8'),
        ('Maritimes', 'CaSO4 2H2O'),
        ('Pyrenees Mountains', 'Al2SiO5'), 
        ('Greek Islands', 'MgCO3'), 
        ('North Africa', 'Ca5(PO4)3 (OH, F, Cl)'), 
        ('Permian Basin', 'CaSO4'), 
        ('Black Forest', 'FeCO3'), 
        ('Yunnan Province', 'CaMg(CO3)2'), 
        ('Okavango Delta', 'CaF2'),
        ('Ural Mountains', 'MgSiO3'), 
        ('Hardangervidda', 'NaAlSi3O8'), 
        ('Patagonia', 'CaAl2Si2O8'), 
        ('Faroe Islands', 'Na2O Al2O3 2SiO2 2H2O');"""
    
    cursor.execute(sql_locality_rock_types_data)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


LocalityRockTypes()
