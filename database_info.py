import psycopg2

# DATABASE CONNECTION
def create_connection():
    conn = psycopg2.connect(
        database="YOUR_DB_NAME",
        user="YOUR_USER",
        password="YOUR_DB_PASSWORD",
        host="YOUR_HOST",
        port="YOUR_PORT"
    )
    return conn