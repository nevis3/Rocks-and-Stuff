from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    port="5432",
    password="asdf")

cursor = conn.cursor()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/')
def add_locality(input_data):
    # creating a cursor object
    cursor = conn.cursor()

    # inserting record into employee table
    for d in input_data:
        cursor.execute("INSERT INTO localities(name, country) VALUES (%s,%s)", d)

    #print("List has been inserted to employee table successfully...")

@app.route('/')
def fetch_data(database_info):
    # creating a cursor object
    cursor = conn.cursor()
    sql2 = f"SELECT * FROM {database_info}"
    # executing query
    cursor.execute(sql2)

    # fetching the result
    print(cursor.fetchall())

@app.route('/')
def delete_entries(input_data):
    cursor = conn.cursor()
    sql = f"DELETE FROM localities WHERE country = {input_data}"

    cursor.execute(sql)


if __name__ == "__main__":
    app.run(debug=True)
    data = [('Friesland', 'Germany'), ('Grassland', 'Germany')]
    add_locality(data)