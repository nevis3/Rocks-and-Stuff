import psycopg2

class sqlUtils:
    def __init__(self):
        # Creating a cursor object using the cursor() method
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            port="5432",
            password="asdf")
        self.cursor = self.conn.cursor()

    def insert_locality(self, locality_name, country_name):
        self.cursor.execute(f"INSERT INTO localities(name, country) VALUES ('{locality_name}','{country_name}')")
        self.conn.commit()

    def insert_rock_types(self, rock_type_id, rock_type_name, locality_name, rock_type, rock_age):
        self.cursor.execute(f"INSERT INTO rock_types(id, name, locality_name, type, age) VALUES"
                            f"('{rock_type_id}', '{rock_type_name}', '{locality_name}', '{rock_type}', '{rock_age}')")
        self.conn.commit()

    def get_locality(self, locality_name, country_name):
        if not locality_name:
            self.cursor.execute(f"SELECT * FROM localities WHERE country = '{country_name}'")
            return self.cursor.fetchall()
        else:
            self.cursor.execute(f"SELECT * FROM localities WHERE name = '{locality_name}'")
            return self.cursor.fetchall()


    def get_locality_rock_type(self, rock_name):
        self.cursor.execute(f"SELECT rock_types.locality_name FROM rock_types WHERE name = '{rock_name}'")
        return self.cursor.fetchall()

    def get_rock_type(self, rock_id):
        self.cursor.execute(f"SELECT * FROM rock_types WHERE id = '{rock_id}'")
        return self.cursor.fetchall()


    def insert_sample(self, sample_id, rock_type, locality, coordinates, date):
        self.cursor.execute(f"INSERT INTO samples(id, rock_type, locality_name, coordinates, date) VALUES ('{sample_id}'"
                            f",'{rock_type}', '{locality}', '{coordinates}', '{date}')")
        self.conn.commit()

    def get_sample(self, sample_id):
        self.cursor.execute(f"SELECT * FROM samples WHERE id = '{sample_id}'")
        return self.cursor.fetchall()