#only needs to run once

import psycopg2


def RockType():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5433",
        password="*")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_rock_types_data = """INSERT INTO rock_types (ID, Name, Type, Age) VALUES
        ('Au', 'Gold', 'Metamorphic', '2.5 GA'),
        ('Ag', 'Silver', 'Sedimentary', '500 MA'),
        ('Cu', 'Copper', 'Igneous', '1 GA'),
        ('Fe', 'Iron', 'Sedimentary', '2.4 GA'),
        ('Pb', 'Lead', 'Metamorphic', '1.7 GA'),
        ('Zn', 'Zinc', 'Sedimentary', '700 MA'),
        ('Al', 'Aluminum', 'Igneous', '1.2 GA'),
        ('Ti', 'Titanium', 'Metamorphic', '2 GA'),
        ('SiO2', 'Quartz', 'Sedimentary', '2.7 GA'),
        ('CaCO3', 'Calcite', 'Igneous', '1.5 GA'),
        ('NaCl', 'Halite', 'Sedimentary', '600 MA'),
        ('KAlSi3O8', 'Orthoclase', 'Metamorphic', '1.8 GA'),
        ('CaSO4 2H2O', 'Gypsum', 'Sedimentary', '800 MA'),
        ('Al2SiO5', 'Andalusite', 'Metamorphic', '1.9 GA'),
        ('MgCO3', 'Magnesite', 'Sedimentary', '1.3 GA'),
        ('Ca5(PO4)3 (OH, F, Cl)', 'Apatite', 'Metamorphic', '2.2 GA'),
        ('CaSO4', 'Anhydrite', 'Sedimentary', '900 MA'),
        ('FeCO3', 'Siderite', 'Metamorphic', '1.6 GA'),
        ('CaMg(CO3)2', 'Dolomite', 'Sedimentary', '2.1 GA'),
        ('CaF2', 'Fluorite', 'Metamorphic', '1.4 GA'),
        ('MgSiO3', 'Enstatite', 'Sedimentary', '2 GA'),
        ('NaAlSi3O8', 'Albite', 'Metamorphic', '1.2 GA'),
        ('CaAl2Si2O8', 'Anorthite', 'Sedimentary', '1.7 GA'),
        ('Na2O Al2O3 2SiO2 2H2O', 'Natrolite', 'Sedimentary', '1.5 GA');"""

    cursor.execute(sql_rock_types_data)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


RockType()
