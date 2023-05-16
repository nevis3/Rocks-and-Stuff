import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database="postgres",
    user="postgres",
    password="asdf"
)



if __name__ == '__main__':
    cur = conn.cursor()
    query = "SELECT * FROM teaches NATURAL JOIN attends NATURAL JOIN likes"
    cur.execute(query)
    data = cur.fetchall()
    conn.commit()
    for row in data:
        print(row)

    conn.close()
