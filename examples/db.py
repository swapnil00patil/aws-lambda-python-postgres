import json

from examples import db_util

def db(event, context):
    query_cmd = "select count(*) from public.users"
    print(query_cmd)
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = db_util.make_conn()

    result = db_util.fetch_data(conn, query_cmd)
    conn.close()
    print("db result: %s" % (result))

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response