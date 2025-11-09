A Python application that does CRUD operations on a PostgreSQL database

Setup Instructions
1. Install PostgreSQL
    Download and install PostgreSQL from https://www.postgresql.org/download/

2. Create Database
    Open pgAdmin and create a new database called students_db

3. Run Setup Script
    In pgAdmin, right-click students_db → Query Tool
    Open database_setup.sql (or copy and paste the script)
    Click Execute (F5)

4. Install Python Package
    pip install psycopg2
5. Update Database Password
    Open student_manager.py and change line 11:
    pythonDB_PASSWORD = "your_password"  # Put your PostgreSQL password here
6. Run the Application
    In your command line(or terminal/bash) Go to the directory where the script is located and then run the following:
    python script.py

Video Demonstration
youtube.com/watch?v=Kx-X0_2Onok&feature=youtu.be
