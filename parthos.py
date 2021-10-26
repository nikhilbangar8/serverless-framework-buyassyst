import json


def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function PARTHOS executed successfully!",
        "input": event,
    }
    connect()
    return {"statusCode": 200, "body": json.dumps(body)}


    def connect():
        """ Connect to MySQL database """
        conn = None
        try:
            conn = mysql.connector.connect(host='mydatabase.cobb2ri2wqur.us-east-1.rds.amazonaws.com',
                                        database='myDatabase',
                                        user='DBADMIN',
                                        password='password')
            if conn.is_connected():
                print('Connected to MySQL database')

        except Error as e:
            print(e)

        finally:
            if conn is not None and conn.is_connected():
                conn.close()