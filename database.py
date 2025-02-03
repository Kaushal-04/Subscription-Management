import psycopg2
from psycopg2 import sql

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host='localhost', 
            dbname='mem_management', 
            user='postgres', 
            password='12345', 
            port=5432
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    try:
        conn = get_db_connection()
        if conn is None:
            return
        cur = conn.cursor()
        member_table = '''
            CREATE TABLE IF NOT EXISTS member (
                mem_id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                mobile VARCHAR(10) NOT NULL,
                email VARCHAR(50),
                mem_type VARCHAR(10) CHECK (mem_type IN ('Monthly', 'Quarterly', 'Yearly')),
                start_date DATE DEFAULT CURRENT_DATE,
                end_date DATE
            )
        '''
        cur.execute(member_table)
        conn.commit()
        cur.close()
        conn.close()
        print('Table created or already exists.')
    except Exception as e:
        print(f"Error creating table: {e}")

def add_member(mem_info):
    try:
        conn = get_db_connection()
        if conn is None:
            return
        cur = conn.cursor()
        new_member = '''
            INSERT INTO member (name, mobile, email, mem_type, start_date, end_date) 
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cur.execute(new_member, (
            mem_info["name"], mem_info["mobile"], mem_info["email"], 
            mem_info["mem_type"], mem_info["start_date"], mem_info["end_date"]
        ))
        conn.commit()
        cur.close()
        conn.close()
        print("Member added successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error adding member: {e}")

def update_member(update_info):
    try:
        conn = get_db_connection()
        if conn is None:
            return
        cur = conn.cursor()
        mem_update = '''UPDATE member 
                        SET mobile = %s, email = %s, mem_type = %s 
                        WHERE mem_id = %s'''
        
        cur.execute(mem_update, (update_info["mobile"], update_info["email"], update_info["mem_type"], update_info["id"]))
        conn.commit()
        cur.close()
        conn.close()
        print("Member updated successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error updating member: {e}")

def fetch_all_members():
    try:
        conn = get_db_connection()
        if conn is None:
            return []
        cur = conn.cursor()
        cur.execute('SELECT * FROM member')
        records = cur.fetchall()
        cur.close()
        conn.close()
        return records
    except Exception as e:
        print(f"Error fetching members: {e}")
        return []

def fetch_member_by_id(mem_id):
    try:
        conn = get_db_connection()
        if conn is None:
            return None
        cur = conn.cursor()
        cur.execute('SELECT * FROM member WHERE mem_id = %s', (mem_id,))
        record = cur.fetchone()
        cur.close()
        conn.close()
        return record
    except Exception as e:
        print(f"Error fetching member by ID: {e}")
        return None

# Initialize Database
create_table()
