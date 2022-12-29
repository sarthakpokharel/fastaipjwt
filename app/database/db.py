import psycopg2
from messages import Messages

message = Messages

def execute_query(sql):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                users = cursor.fetchall()
            except:
                return message.error()
        return users

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="root",
        dbname="hlabsdb"
    )
    return conn