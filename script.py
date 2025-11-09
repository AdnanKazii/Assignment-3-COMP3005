"""
By Adnan Kazi 101304031
"""

import psycopg2
from datetime import date

# Database connection parameters - Change where needed
DB_NAME = "student_db" # Change this
DB_USER = "postgres"
DB_PASSWORD = "postgres"  # Change this
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
    """Establish connection to PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connected to database")
        return connection
    except Exception as e:
        print(f"Connection error: {e}")
        return None


def getAllStudents(connection):
    """Retrieve and display all student records."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY student_id;")
        students = cursor.fetchall()
        
        print("\n--- ALL STUDENTS ---")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]} {student[2]}, "
                  f"Email: {student[3]}, Enrolled: {student[4]}")
        cursor.close()
    except Exception as e:
        print(f"Error getting students: {e}")


def addStudent(connection, first_name, last_name, email, enrollment_date):
    """Insert a new student record."""
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (first_name, last_name, email, enrollment_date))
        connection.commit()
        print(f"Added student: {first_name} {last_name}")
        cursor.close()
    except Exception as e:
        connection.rollback()
        print(f"Error adding student: {e}")


def updateStudentEmail(connection, student_id, new_email):
    """Update email address for a specific student."""
    try:
        cursor = connection.cursor()
        query = "UPDATE students SET email = %s WHERE student_id = %s;"
        cursor.execute(query, (new_email, student_id))
        connection.commit()
        
        if cursor.rowcount > 0:
            print(f"Updated email for student ID {student_id}")
        else:
            print(f"Student ID {student_id} not found")
        
        cursor.close()
    except Exception as e:
        connection.rollback()
        print(f"Error updating email: {e}")


def deleteStudent(connection, student_id):
    """Delete a student record."""
    try:
        cursor = connection.cursor()
        query = "DELETE FROM students WHERE student_id = %s;"
        cursor.execute(query, (student_id,))
        connection.commit()
        
        if cursor.rowcount > 0:
            print(f"Deleted student ID {student_id}")
        else:
            print(f"Student ID {student_id} not found")
        
        cursor.close()
    except Exception as e:
        connection.rollback()
        print(f"Error deleting student: {e}")


def main():
    print("\nCOMP 3005 ASSIGNMENT 3 Q 1\n")
    
    # Connect to database
    connection = connect_db()
    if not connection:
        return
    
    # 1. READ - Display initial data
    print("\n1. INITIAL DATA:")
    getAllStudents(connection)
    
    # 2. CREATE - Add new student
    print("2. ADDING NEW STUDENT:")
    addStudent(connection, "Adnan", "Kazi", "adnan.kazi@cmail.carleton.ca", date(2023, 9, 5))
    getAllStudents(connection)
    
    # 3. UPDATE - Change email
    print("3. UPDATING EMAIL:")
    updateStudentEmail(connection, 1, "john.doe@cmail.carleton.ca")
    getAllStudents(connection)
    
    # 4. DELETE - Remove student
    print("4. DELETING STUDENT:")
    deleteStudent(connection, 3)
    getAllStudents(connection)
    
    # Close connection
    connection.close()
    print(" Database connection closed")
    print("\nDEMONSTRATION COMPLETE\n")


if __name__ == "__main__":
    main()