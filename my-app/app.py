import psycopg2, os

DB_CONFIG = {
    'dbname': 'student',
    'user': 'postgres',
    'password': 'postgres',
    #'host': 'pg_test-postgres-1',
    'host': 'x.x.xx.xx',
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


if __name__== '__main__':
 conn = get_db_connection()
 cur = conn.cursor()
 cur.execute("SELECT version();")
 print("Postgres version:", cur.fetchone())
