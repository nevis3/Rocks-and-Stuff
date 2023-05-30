Create TABLE IF NOT EXISTS localities(
       name VARCHAR(255) PRIMARY KEY,
       country VARCHAR(255) NOT NULL);

CREATE TABLE IF NOT EXISTS rock_types(
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255),
        type VARCHAR(255),
        age VARCHAR(255),
        strike FLOAT,
        dip FLOAT,
        dip_direction VARCHAR(255));

CREATE TABLE IF NOT EXISTS elements(
        name VARCHAR(255) PRIMARY KEY,
        symbol VARCHAR(255) NOT NULL,
        weight FLOAT,
        state VARCHAR(255));

CREATE TABLE IF NOT EXISTS samples(
       id VARCHAR(255) PRIMARY KEY,
       rock_type VARCHAR(255) NOT NULL,
       locality_name VARCHAR(255) NOT NULL,
       coordinates VARCHAR(255),
       date date,

       FOREIGN KEY (rock_type) REFERENCES rock_types(id),
       FOREIGN KEY (locality_name) REFERENCES localities(name));

CREATE TABLE IF NOT EXISTS locality_rock_types(
        locality_name VARCHAR(255) NOT NULL,
        rock_type_id VARCHAR(255) NOT NULL,
        sample_id VARCHAR(255),
        CONSTRAINT PK_locality_rock_type PRIMARY KEY (locality_name,rock_type_id),

        FOREIGN KEY (locality_name) REFERENCES localities(name),
        FOREIGN KEY (rock_type_id) REFERENCES rock_types(id));

CREATE TABLE IF NOT EXISTS samples_chemical_data(
        sample_id VARCHAR(255) PRIMARY KEY,
        element_name VARCHAR(255),
        weight_percentage FLOAT,
        FOREIGN KEY (element_name) REFERENCES elements(name),
        FOREIGN KEY (sample_id) REFERENCES samples(id));