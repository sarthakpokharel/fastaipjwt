import psycopg2
from app.messages import Messages
from decouple import config

message = Messages

def execute_query(sql, params, res):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                if (res == True):
                    result = cursor.fetchall()                
                    return result
            except Exception as e:
                return message.custom_message(e.args[0])
        return message.success()

def get_db_connection():
    conn = psycopg2.connect(
        host=config('host'),
        port=config('port'),
        user=config('user'),
        password=config('password'),
        dbname=config('dbname')
    )
    return conn