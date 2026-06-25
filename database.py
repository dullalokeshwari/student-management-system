import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dob TEXT,
        gender TEXT,
        phone TEXT,
        email TEXT,
        department TEXT,
        semester TEXT,
        marks REAL,
        attendance REAL
    )
    """)

    conn.commit()
    return conn, cursor

def initialize_database():
    conn, cursor = connect_db()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database Created Successfully!")