Student Management System (Tkinter + Oracle DB)

A simple **Student Management System** built using **Python Tkinter** for the GUI and **Oracle Database** for backend storage.  
The application supports **Admin** and **Student** roles with features like student management, enrollment, attendance, and reports.

---

## 🚀 Features

### Login System
- Login as **Admin** or **Student**
- Role-based dashboard

### Admin Features
- Add and manage students
- Record student attendance
- View reports (Students, Enrollments, Attendance)

### Student Features
- Course enrollment

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Oracle Database (XE)**
- **oracledb** Python library

---

## 📂 Project Structure

student-management-system/
│
├── main.py # Main application file
├── README.md # Project documentation

yaml
Copy code

---

## 🧩 Database Schema

Make sure the following tables exist in your Oracle database:

### Students Table
```sql
CREATE TABLE students (
    student_id NUMBER PRIMARY KEY,
    name VARCHAR2(100)
);
Enrollments Table
sql
Copy code
CREATE TABLE enrollments (
    student_id NUMBER,
    course_name VARCHAR2(100)
);
Attendance Table
sql
Copy code
CREATE TABLE attendance (
    student_id NUMBER,
    status VARCHAR2(20)
);
🔧 Configuration
Update the database connection details in the code:

python
Copy code
conn = oracledb.connect(
    user='SYSTEM',
    password='tiger',
    dsn='localhost:1521/XE'
)
Ensure:

Oracle XE is running

Tables are created

oracledb package is installed

📦 Installation
Clone the repository

bash
Copy code
git clone https://github.com/your-username/student-management-system.git
Install dependencies

bash
Copy code
pip install oracledb
Run the application

bash
Copy code
python main.py
🖥️ Application Flow
Launch application

Select login type (Admin / Student)

Access dashboard based on role

Perform operations (Add Student, Enrollment, Attendance, Reports)

Logout

⚠️ Known Issues / Notes
Error handling is minimal

Database connection should ideally be handled globally

Passwords are hardcoded (not recommended for production)

UI is basic (can be improved with styling)

🔮 Future Enhancements
Secure authentication (username/password)

Edit & delete records

Search functionality

Improved UI/UX

Role-based access control

Exception handling and logging

👨‍💻 Author
Developed as a Python + Database mini project for learning GUI and database integration.

📜 License
This project is for educational purposes only.
