#only needs to run once. creates 2 databases, dont know why

import psycopg2

def Tables():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5432",
        password="asdf")
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    sql_localities = """CREATE TABLE localities(
       name VARCHAR(255) PRIMARY KEY,
       country VARCHAR(255) NOT NULL
    )"""

    cursor.execute(sql_localities)

    sql_rock_types = """CREATE TABLE rock_types(
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255),
        type VARCHAR(255),
        age VARCHAR(255),
        strike FLOAT,
        dip FLOAT,
        dip_direction VARCHAR(255)
        )"""

    cursor.execute(sql_rock_types)

    sql_elements = """CREATE TABLE elements(
        name VARCHAR(255) PRIMARY KEY,
        symbol VARCHAR(255) NOT NULL,
        weight FLOAT,
        state VARCHAR(255)
    )"""

    cursor.execute(sql_elements)

    sql_samples = """CREATE TABLE samples(
       id VARCHAR(255) PRIMARY KEY,
       rock_type VARCHAR(255) NOT NULL,
       locality_name VARCHAR(255) NOT NULL,
       coordinates VARCHAR(255),
       date date
    )"""

    cursor.execute(sql_samples)

    sql_locality_rock_types = """CREATE TABLE locality_rock_types(
        locality_name VARCHAR(255) PRIMARY KEY,
        rock_type_id VARCHAR(255),
        sample_id VARCHAR(255),
        FOREIGN KEY (locality_name) REFERENCES localities(name),
        FOREIGN KEY (rock_type_id) REFERENCES rock_types(id),
        FOREIGN KEY (sample_id) REFERENCES samples(sample_id)
        )"""

    cursor.execute(sql_locality_rock_types)


    sql_samples_chemical_data = """CREATE TABLE samples_chemical_data(
        sample_id VARCHAR(255) PRIMARY KEY,
        element_name VARCHAR(255),
        weight_percentage FLOAT,
        FOREIGN KEY (element_name) REFERENCES elements(name),
        FOREIGN KEY (sample_id) REFERENCES samples(id)
        )"""

    cursor.execute(sql_samples_chemical_data)


    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


Tables()