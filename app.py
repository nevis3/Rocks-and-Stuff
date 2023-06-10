
import flask
from flask import Flask, redirect, url_for, render_template, request
import psycopg2

from sqlUtils import sqlUtils

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    port="5432",
    password="asdf")

cursor = conn.cursor()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/localities", methods=["GET"])
def get_localities():
    get_status = get_locality(request.args["locality_name"], request.args["country_name"]) \
        if request.args \
        else None
    return render_template("localities.html", response_status=get_status)


@app.route("/localities", methods=["POST"])
def post_localities():
    insert_status = insert_locality(request.form["locality_name"], request.form["country_name"])
    return render_template("localities.html", response_status=insert_status)


def get_locality(locality_name, country_name):
    sql_util = sqlUtils()
    try:
        return sql_util.get_locality(locality_name, country_name)
    except Exception as e:
        return str(e)


def insert_locality(locality_name, country_name):
    sql_util = sqlUtils()
    try:
        sql_util.insert_locality(locality_name, country_name)
        return "succesfully added"
    except Exception as e:
        return str(e)


@app.route("/rocks_type_localities", methods=["GET"])
def get_rock_type_localities():
    get_status = get_locality_rock_type(request.args["rock_name"]) \
        if request.args \
        else None
    return render_template("rock_type_localities.html", response_status=get_status)


def get_locality_rock_type(rock_name):
    sql_util = sqlUtils()
    try:
        return sql_util.get_locality_rock_type(rock_name)
    except Exception as e:
        return str(e)


@app.route("/rock_types", methods=["POST"])
def post_rock_type():
    insert_status = insert_rock_type(request.form["rock_id"], request.form["rock_name"], request.form["locality_name"],
                                     request.form["rock_type"], request.form["age_number"])
    return render_template("rocks.html", response_status=insert_status)

@app.route("/rock_types", methods=["GET"])
def get_rock_types():
    get_status = get_rock_type(request.args["rock_id"]) \
        if request.args \
        else None
    return render_template("rocks.html", response_status=get_status)

def insert_rock_type(rock_type_id, rock_type_name, locality_name, rock_type, rock_age):
    sql_util = sqlUtils()
    try:
        sql_util.insert_rock_types(rock_type_id, rock_type_name, locality_name, rock_type, rock_age)
        return "succesfully added"
    except Exception as e:
        return str(e)

def get_rock_type(rock_id):
    sql_util = sqlUtils()
    try:
        return sql_util.get_rock_type(rock_id)
    except Exception as e:
        return str(e)

@app.route("/samples", methods=["POST"])
def post_sample():
    insert_status = insert_sample(request.form["id"], request.form["rock_type"], request.form["locality_name"],
                                  request.form["coordinates"], request.form["date"])
    return render_template("samples.html", response_status=insert_status)


def insert_sample(sample_id, rock_type, locality_name, coordinates, date_data):
    sql_util = sqlUtils()
    try:
        sql_util.insert_sample(sample_id, rock_type, locality_name, coordinates, date_data)
        return "succesfully added"
    except Exception as e:
        return str(e)


@app.route("/samples", methods=["GET"])
def get_sample():
    get_status = get_samples(request.args["id"]) \
        if request.args \
        else None
    return render_template("samples.html", response_status=get_status)

def get_samples(sample_id):
    sql_util = sqlUtils()
    try:
        return sql_util.get_sample(sample_id)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)

