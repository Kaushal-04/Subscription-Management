import psycopg2

curr = None
conn = None
try:
    conn = psycopg2.connect(host = 'localhost', dbname = 'database', user = 'postgres', password = '1234', port = 5432)
    cur = conn.cursor()





except Exception as erro:
    print("Error in connection of database")
finally:
    if curr is not None:
        curr.close
    if conn is not None:
        conn.close