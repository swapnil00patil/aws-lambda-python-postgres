import psycopg2

db_host = "test-db.cmeky7ng29ie.us-east-1.rds.amazonaws.com"
db_port = 5432
db_name = "test-db"
db_user = "postgres"
db_pass = "OP$tgresPSwap"


def make_conn():
    print("make_conn called")
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print("I am unable to connect to the database")
    return conn


def fetch_data(conn, query):
    print("fetch_data called")
    result = []
    print("Now executing: %s" % (query))
    cursor = conn.cursor()
    cursor.execute(query)

    raw = cursor.fetchall()
    print("cursor fetchall: %s" % (raw))
    for line in raw:
        result.append(line)
    print("result: %s" % (result))
    return result
