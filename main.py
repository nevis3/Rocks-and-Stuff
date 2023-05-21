import psycopg2

def add_locality(input_data):
    # creating a cursor object
    cursor = conn.cursor()

    # inserting record into employee table
    for d in input_data:
        cursor.execute("INSERT into localities(name, country) VALUES (%s,%s)", d)

    #print("List has been inserted to employee table successfully...")


def fetch_data(database_info):
    # creating a cursor object
    cursor = conn.cursor()
    sql2 = "select * from %s" %database_info
    # executing query
    cursor.execute(sql2)

    # fetching the result
    print(cursor.fetchall())

def delete_entries(input_data):
    cursor = conn.cursor()
    sql = "DELETE FROM localities WHERE country = '%s'" %input_data

    cursor.execute(sql)

if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port="5432",
        password="asdf")

    data = [('Friesland', 'Germany'), ('Grassland', 'Germany')]
    add_locality(data)

    fetch_data("localities")

    delete_entries('Germany')

    fetch_data("localities")

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

