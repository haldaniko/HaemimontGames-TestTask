import sqlite3

conn = sqlite3.connect('coursera.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    instructor_id INTEGER NOT NULL,
                    total_time INTEGER NOT NULL,
                    credit INTEGER NOT NULL,
                    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS instructors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    pin TEXT PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS students_courses_xref (
                    student_pin TEXT NOT NULL,
                    course_id INTEGER NOT NULL,
                    completion_date DATE,
                    FOREIGN KEY(student_pin) REFERENCES students(pin),
                    FOREIGN KEY(course_id) REFERENCES courses(id),
                    PRIMARY KEY (student_pin, course_id)
                  )''')

conn.commit()
conn.close()

print("Таблицы успешно созданы в базе данных coursera.db")
