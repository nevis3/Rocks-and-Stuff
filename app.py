from flask import Flask, redirect, url_for, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    port="5432",
    password="asdf")

cursor = conn.cursor()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def home2():
    return render_template("index.html")
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/localities", methods=["POST", "GET"])
def localities():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("localities.html")

@app.route("/rocks", methods=["POST", "GET"])
def rocks():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("rocks.html")

@app.route("/samples", methods=["POST", "GET"])
def samples():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("samples.html")

@app.route("/elements", methods=["POST", "GET"])
def elements():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("elements.html")
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

"""def add_locality(input_data):
    # creating a cursor object
    cursor = conn.cursor()

    # inserting record into employee table
    for d in input_data:
        cursor.execute("INSERT INTO localities(name, country) VALUES (%s,%s)", d)

    #print("List has been inserted to employee table successfully...")

@app.route('/', methods=['GET'])
def fetch_data(database_info):
    # creating a cursor object
    cursor = conn.cursor()
    sql2 = f"SELECT * FROM {database_info}"
    # executing query
    cursor.execute(sql2)

    # fetching the result
    print(cursor.fetchall())

@app.route('/', methods=['GET'])
def delete_entries(input_data):
    cursor = conn.cursor()
    sql = f"DELETE FROM localities WHERE country = {input_data}"

    cursor.execute(sql)"""


if __name__ == "__main__":
    app.run(debug=True)
    """data = [('Friesland', 'Germany'), ('Grassland', 'Germany')]
    add_locality(data)

    fetch_data("localities")

    delete_entries('Germany')

    fetch_data("localities")

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()"""