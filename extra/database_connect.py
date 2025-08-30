import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="root"
)

cur = conn.cursor()
cur.execute("SELECT version();")
print("DB Version:", cur.fetchone())

cur.close()
conn.close()
