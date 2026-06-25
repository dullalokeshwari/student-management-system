from sqlite3 import Cursor

from database import connect_db
def add_student():
    conn, cursor = connect_db()
    student_id = int(input("Enter Student ID:"))
    name = input("Enter Name:")
    dob = input("Enter Date Of Birth:")
    gender = input("Enter Gender:")
    phone = input("Enter Phone Number:")
    email = input("Enter Email:")
    department = input("Enter Department:")
    semester = input("Enter Semester:")
    marks = float(input("Enter Marks:"))
    attendance =float(input("Enter Attendance percentage:"))
    cursor.execute("""
                   INSERT INTO students
                   (student_id, name, dob, gender,
                    phone, email, department, semester, marks, attendance)
                   VALUES
                 (?,?,?,?,?,?,?,?,?,?)
                   """, (student_id, name, dob, gender,
                   phone, email, department, semester, marks,
                    attendance))
    conn.commit()
    conn.close()
    print("Student Added Successfully!")

def view_students():
    conn, cursor, = connect_db()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if records:
        print("\n==== STUDENT RECORDS ====")
        for row in records:
            print(row)
        else:
            print("No student records found.")
            conn.close

def search_students():
    conn, cursor = connect_db()
    student_id = int(input("Enter Student ID:"))
    cursor.execute("SELECT * FROM students WHERE student_id = ?",(student_id,))
    record = cursor.fetchone()
    if record:
        print(record)
    else:
        print("student not found.")
        conn.close()

def delete_student():
    conn, cursor = connect_db()
    student_id = int(input("Enter Student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE student_id = ?",(student_id,))
    conn.commit()
    print("Student deleted successfully!")
    conn.close()

def update_student():
    conn, Cursor = connect_db()
    student_id = int(input("Enter Student_ID:"))
    phone = input("Enter New Phone Number:")
    email = input("Enter New Email:")
    Cursor.execute("UPDATE Students SET phone=?, email=? WHERE student_id=?",
                   (phone, email, student_id)
    )
    conn.commit()
    print("Student updated successfully!")
    conn.close()


    




    
    


        