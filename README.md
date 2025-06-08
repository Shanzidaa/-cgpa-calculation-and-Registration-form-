# cgpa-calculation-and-Registration-form-

## This project is a web-based application built using **Python** and the **Flask** web framework. It provides two core functionalities:

1. **Student Registration**
2. **CGPA Calculation**

The system is designed for educational institutions to streamline student data entry and automate the process of calculating cumulative grade point averages (CGPA).

### Key Features

- 📝 **Student Registration Form**  
  Collects and stores basic student information (e.g., name, ID, department, semester, etc.) into a MySQL database.

- 🧮 **Marks Entry & CGPA Calculation**  
  Allows authenticated users to input subject-wise marks. The backend processes the input to calculate:
  - Individual semester GPA
  - Accumulated CGPA over multiple semesters

- 🔒 **Password-Protected GPA View**  
  To enhance privacy, students must verify their identity (e.g., via password or ID) to view their CGPA.

- 📦 **Database Integration**  
  Uses MySQL (or SQLite as an alternative) to store:
  - Student details
  - Marks per subject
  - GPA and CGPA results

- 📊 **User-Friendly Interface**  
  Built using HTML, CSS  and Flask templates for a smooth user experience.

### 🛠️ Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** MySQL (or SQLite for local testing)
- **Libraries:** SQLAlchemy, Flask-WTF, Flask-Login (optional)

## 🌐 How It Works

1. A new student fills out a registration form.
2. Admin or user logs in to enter subject marks.
3. The system calculates GPA based on a grading system.
4. CGPA is computed and shown in a protected view.

This system is highly adaptable for colleges and universities to manage and evaluate academic performance efficiently.
