
from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentsdb"
   
)
mycursor = mydb.cursor()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id VARCHAR(20) PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        email VARCHAR(100),
        password VARCHAR(100),
        dob DATE,
        gender VARCHAR(10),
        religion VARCHAR(20),
        department VARCHAR(20)
    )
""")


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id VARCHAR(20),
        semester VARCHAR(20),
        subject1 INT,
        subject2 INT,
        subject3 INT,
        subject4 INT,
        subject5 INT,
        cgpa FLOAT,
        acc_cgpa DECIMAL(5,2)  
    )
""")

mydb.commit()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = (
            request.form['id'],
            request.form['firstname'],
            request.form['lastname'],
            request.form['email'],
            request.form['password'],
            request.form['dob'],
            request.form['gender'],
            request.form['religion'],
            request.form['department']
        )
        sql = """
            INSERT INTO students (id, firstname, lastname, email, password, dob, gender, religion, department)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        mycursor.execute(sql, data)
        mydb.commit()
        return render_template('view.html', data=data)
    return render_template('register.html')

@app.route('/password_check', methods=['GET', 'POST'])
def password_check():
    if request.method == 'POST':
        entered_password = request.form['password']
        correct_password = 'result'  

        if entered_password == correct_password:
            return redirect(url_for('cgpa'))  
        else:
            return redirect(url_for('register'))  

    return render_template('password_check.html')

@app.route('/cgpa', methods=['GET', 'POST'])
def cgpa():
    if request.method == 'POST':
        student_id = request.form['student_id']
        semester = request.form['semester']
        one = int(request.form['one'])
        two = int(request.form['two'])
        three = int(request.form['three'])
        four = int(request.form['four'])
        five = int(request.form['five'])

       
        def marks_to_grade_point(marks):
            if 80 <= marks <= 100:
                return 4.0
            elif 75 <= marks < 80:
                return 3.75
            elif 70 <= marks < 75:
                return 3.5
            elif 65 <= marks < 70:
                return 3.25
            elif 60 <= marks < 65:
                return 3.0
            elif 55 <= marks < 60:
                return 2.75
            elif 50 <= marks < 55:
                return 2.5
            elif 45 <= marks < 50:
                return 2.25
            elif 40 <= marks < 45:
                return 2.0
            else:
                return 0.0

        grade_points = [marks_to_grade_point(mark) for mark in [one, two, three, four, five]]
        
        semester_gpa = round(sum(grade_points) / len(grade_points), 2)

        
        insert_sql = """
            INSERT INTO marks 
            (student_id, semester, subject1, subject2, subject3, subject4, subject5, cgpa, acc_cgpa)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        mycursor.execute(insert_sql, (student_id, semester, one, two, three, four, five, semester_gpa, 0.0))
        mydb.commit()

        
        mycursor.execute("SELECT AVG(cgpa) FROM marks WHERE student_id = %s", (student_id,))
        acc_cgpa = mycursor.fetchone()[0] or 0.0

        acc_cgpa = round(acc_cgpa, 2)

     
        mycursor.execute("""
            UPDATE marks 
            SET acc_cgpa = %s 
            WHERE student_id = %s AND semester = %s
        """, (acc_cgpa, student_id, semester))
        mydb.commit()

        return render_template('result.html', student_id=student_id, semester=semester,
                               one=one, two=two, three=three, four=four, five=five,
                               cgpa=semester_gpa, acc_cgpa=round(acc_cgpa, 2))
    return render_template('cgpa.html')


if __name__ == '__main__':
    app.run(debug=True)
