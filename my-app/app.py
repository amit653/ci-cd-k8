import psycopg2, os,time
from datetime import datetime
from flask import Flask

app=Flask(__name__)
DB_CONFIG = {
    'dbname': 'student',
    'user': 'postgres',
    'password': 'postgres',
    #'host': '192.x.x',
    'host': 'postgres',  ## service name of postgres pod
    'port': 5432,
    'connect_timeout': 5  # Tell psycopg2 to wait up to 5s per attempt
}
def get_db_connection():
    """Attempts to connect to Postgres with a retry loop for startup."""
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            return conn
        except psycopg2.OperationalError as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Postgres not ready yet. Retrying in 2s...")
            time.sleep(2)

@app.route("/")
def display():
 conn=get_db_connection()
 cur = conn.cursor()
 cur.execute("SELECT version();")
 version=cur.fetchone()
 cur.close()
 conn.close()
 return f"Connected to Postgres! Version: {version}"

if __name__== '__main__':
 app.run(host="0.0.0.0",port=5000)
 
 #print("Postgres version:", cur.fetchone())
