import psycopg2
from app.messages import Messages

message = Messages

def execute_query(sql, res):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                if (res == True):
                    result = cursor.fetchall()                
                    return result
            except Exception as e:
                return message.custom_message(e.args[0])
        return message.success()

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="root",
        dbname="hlabsdb"
    )
    return conn