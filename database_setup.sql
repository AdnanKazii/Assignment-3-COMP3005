-- Added this justi nase we run it again to avoid any errors if the table already exists
DROP TABLE IF EXISTS students;

-- Create the students table with specified schema
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,  -- Auto-incrementing integer primary key
    first_name TEXT NOT NULL,        -- Student's first name (required)
    last_name TEXT NOT NULL,         -- Student's last name (required)
    email TEXT NOT NULL UNIQUE,      -- Student's email (required and unique)
    enrollment_date DATE             -- Date when student enrolled
);

-- Sample data from brightspace
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


SELECT * FROM students;