import sqlite3


def generate_csv_report(student_data):
    csv_content = "Student,Total Credit,Course Name,Time,Credit,Instructor\n"

    for student_name, courses_data in student_data.items():
        total_credit = sum(course[2] for course in courses_data)
        csv_content += f'"{student_name}",{total_credit},,,,\n'
        for course_data in courses_data:
            course_name, total_time, credit, instructor_name = course_data
            csv_content += f',,{course_name},{total_time},{credit},"{instructor_name}"\n'

    return csv_content


def generate_html_report(student_data):
    html_content = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Report</title>
        <style>
        table {
            border-collapse: collapse;
            width: 50%;
        }

        th, td {
            border: 2px solid black;
            padding: 8px;
            text-align: center;

        }

        .blue-row {
            background-color: #2f75b5;
            color: black;
        }

        .sky-blue-row {
            background-color: #bdd7ee;
            color: black;
        }

        .green-row {
            background-color: #c6e0b4;
            color: black;
        }

    </style>
    </head>
    <body>
    <table>
        <tr class="blue-row">
            <th>Student</th>
            <th>Total Credit</th>
            <th></th>
            <th></th>
            <th></th>
        </tr>
        <tr class="blue-row">
            <th></th>
            <th>Course Name</th>
            <th>Time</th>
            <th>Credit</th>
            <th>Instructor</th>
        </tr>"""

    for student_name, courses_data in student_data.items():
        total_credit = sum(course[2] for course in courses_data)
        html_content += f'''
        <tr class="sky-blue-row">
            <th>{student_name}</th>
            <th>{total_credit}</th>
            <th></th>
            <th></th>
            <th></th>
        </tr>'''
        for course_data in courses_data:
            course_name, total_time, credit, instructor_name = course_data
            html_content += f'''
        <tr class="green-row">
            <td></td>
            <td>{course_name}</td>
            <td>{total_time}</td>
            <td>{credit}</td>
            <td>{instructor_name}</td>
        </tr>'''

    html_content += """
        </table>
    </body>
</html>
        """

    return html_content


def fetch_student_data_from_db(pins, min_credit, start_date, end_date):
    conn = sqlite3.connect('coursera.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            s.first_name || ' ' || s.last_name AS student_name,
            c.name AS course_name,
            c.total_time,
            c.credit,
            i.first_name || ' ' || i.last_name AS instructor_name
        FROM 
            students s
        JOIN 
            students_courses_xref scx ON s.pin = scx.student_pin
        JOIN 
            courses c ON scx.course_id = c.id
        JOIN 
            instructors i ON c.instructor_id = i.id
        WHERE
            s.pin IN ({})
        AND s.pin IN (
            SELECT 
                s.pin
            FROM 
                students s
            JOIN 
                students_courses_xref scx ON s.pin = scx.student_pin
            JOIN 
                courses c ON scx.course_id = c.id
            GROUP BY 
                s.pin
            HAVING 
                SUM(c.credit) > ?
        )
        AND (scx.completion_date BETWEEN ? AND ? OR scx.completion_date IS NULL)
        ORDER BY 
            student_name
    """.format(','.join(['?']*len(pins))), pins + [min_credit, start_date, end_date])

    student_data = {}
    for row in cursor.fetchall():
        student_name = row[0]
        course_data = (row[1], row[2], row[3], row[4])
        if student_name not in student_data:
            student_data[student_name] = []
        student_data[student_name].append(course_data)

    conn.close()

    return student_data
