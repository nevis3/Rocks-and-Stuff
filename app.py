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
    get_status = get_localities(request.args["locality_name"], request.args["country_name"]) \
        if request.args \
        else None
    return render_template("localities.html", response_status=get_status)

def get_localities(locality_name, country_name):
    sql_util = sqlUtils()
    try:
        return sql_util.get_locality(locality_name, country_name)
    except:
        return 500

@app.route("/localities", methods=["POST"])
def post_localities():
    insert_status = insert_locality(request.form["locality_name"], request.form["country_name"])
    return render_template("localities.html", response_status=insert_status)


def insert_locality(locality_name, country_name):
    sql_util = sqlUtils()
    try:
        sql_util.insert_locality(locality_name, country_name)
        return "succesfully added"
    except Exception as e:
        return str(e)


def insert_rock_type(rock_type_id, rock_type_name, rock_type, rock_age, rock_strike, rock_dip, rock_dip_direction):
    sql_util = sqlUtils()
    try:
        sql_util.insert_rock_types(rock_type_id, rock_type_name, rock_type, rock_age, rock_strike, rock_dip, rock_dip_direction)
        return 100
    except:
        return 500


def insert_locality_rock_type(locality_name, rock_type_name):
    sql_util = sqlUtils()
    try:
        sql_util.insert_locality_rock_type(locality_name, rock_type_name)
        return 200
    except:
        return 500


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


if __name__ == "__main__":
    app.run(debug=True)

