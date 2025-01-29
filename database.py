import psycopg2

cur = None
conn = None
try:
    conn = psycopg2.connect(host='localhost', dbname='mem_management', user='postgres', password='12345', port=5432)
    cur = conn.cursor()

    # Drop the table if it exists
    cur.execute('DROP TABLE IF EXISTS member')
    print("Table delete !")

    member_table = '''
    CREATE TABLE IF NOT EXISTS member (
        mem_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        mobile VARCHAR(10) NOT NULL,
        email VARCHAR(50),
        mem_type VARCHAR(10) CHECK (mem_type IN ('Monthly', 'Quarterly', 'Yearly')),
        start_date DATE DEFAULT CURRENT_DATE,
        end_date DATE ) '''
    
    cur.execute(member_table)
    print('Table created!')

    new_member = 'INSERT INTO member (name, mobile, email, mem_type, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)'
    mem_info = ('Kaushal', '7783868382', 'kaushaljee82@gmail.com', 'Yearly', '2025-01-25', '2025-02-25')
    cur.execute(new_member, mem_info)

    cur.execute('SELECT * FROM member')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Commit the transaction
    conn.commit()

except Exception as erro:
    print(f"Error in connection or execution: {erro}")
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
