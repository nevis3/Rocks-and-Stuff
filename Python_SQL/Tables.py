#only needs to run once

import psycopg2


def Tables():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5433",
        password="*")
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
        age VARCHAR(255)
        )"""

    cursor.execute(sql_rock_types)


    sql_samples = """CREATE TABLE samples(
       id VARCHAR(255) PRIMARY KEY,
       rock_type VARCHAR(255) NOT NULL,
       locality_name VARCHAR(255) NOT NULL,
       coordinates VARCHAR(255),
       date date,
       
       FOREIGN KEY (rock_type) REFERENCES rock_types(id),
       FOREIGN KEY (locality_name) REFERENCES localities(name)
    )"""

    cursor.execute(sql_samples)

    sql_locality_rock_types = """CREATE TABLE locality_rock_types(
        locality_name VARCHAR(255) NOT NULL,
        rock_type_id VARCHAR(255) NOT NULL,
        CONSTRAINT PK_locality_rock_type PRIMARY KEY (locality_name,rock_type_id),
        
        FOREIGN KEY (locality_name) REFERENCES localities(name),
        FOREIGN KEY (rock_type_id) REFERENCES rock_types(id)
        )"""

    cursor.execute(sql_locality_rock_types)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()


Tables()
