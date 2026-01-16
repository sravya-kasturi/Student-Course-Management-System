import tkinter as tk
from tkinter import ttk, messagebox
import oracledb
def dbconnection():
    try:
        conn = oracledb.connect(user='SYSTEM',Password='tiger',dsn='localhost:1521/XE')
    except Exception:
        print(Exception)
    else:
          print("Database connected successfully")
    cursor = conn.cursor()
    sql="select * from student"
    cursor.excute(sql)
    for row in cursor:
        print(row)

# ---------------- GLOBALS ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x450")

user_type = tk.StringVar()

# ---------------- COMMON FUNCTION ----------------
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# ---------------- LOGIN SCREEN ----------------
def login_screen():
    clear_window()

    tk.Label(root, text="Student Management System",
             font=("Arial", 18, "bold")).pack(pady=20)

    tk.Label(root, text="Login As", font=("Arial", 12)).pack(pady=10)

    ttk.Radiobutton(root, text="Student",
                    variable=user_type,
                    value="Student").pack()

    ttk.Radiobutton(root, text="Admin",
                    variable=user_type,
                    value="Admin").pack()

    ttk.Button(root, text="Login",
               command=dashboard).pack(pady=15)

# ---------------- DASHBOARD ----------------
def dashboard():
    if not user_type.get():
        messagebox.showerror("Error", "Please select login type")
        return

    clear_window()

    tk.Label(root, text=f"{user_type.get()} Dashboard",
             font=("Arial", 18, "bold")).pack(pady=20)

    if user_type.get() == "Admin":
        ttk.Button(root, text="Manage Students",
                   command=manage_students).pack(pady=5)

        ttk.Button(root, text="Attendance",
                   command=attendance_screen).pack(pady=5)

        ttk.Button(root, text="Reports",
                   command=reports).pack(pady=5)
    else:
        ttk.Button(root, text="Enrollment",
                   command=enrollment).pack(pady=5)

    ttk.Button(root, text="Logout",
               command=login_screen).pack(pady=10)

# ---------------- MANAGE STUDENTS ----------------
def manage_students():
    clear_window()

    tk.Label(root, text="Manage Students",
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Student ID").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()

    tk.Label(root, text="Student Name").pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    def save_student():
        if entry_id.get() and entry_name.get():
            cursor.execute(
                "INSERT INTO students (student_id, name) VALUES (:1, :2)",
                (entry_id.get(), entry_name.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Student Saved in Database")
            entry_id.delete(0, tk.END)
            entry_name.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields required")

    ttk.Button(root, text="Add Student",
               command=save_student).pack(pady=5)

    ttk.Button(root, text="Back",
               command=dashboard).pack(pady=5)

# ---------------- ENROLLMENT ----------------
def enrollment():
    clear_window()

    tk.Label(root, text="Enrollment",
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Student ID").pack()
    student_entry = tk.Entry(root)
    student_entry.pack()

    tk.Label(root, text="Course Name").pack()
    course_entry = tk.Entry(root)
    course_entry.pack()

    def enroll():
        if student_entry.get() and course_entry.get():
            dbconnection()
            cursor.execute(
                "INSERT INTO enrollments (student_id, course_name) VALUES (:1, :2)",
                (student_entry.get(), course_entry.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Enrollment Saved in Database")
            student_entry.delete(0, tk.END)
            course_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields required")

    ttk.Button(root, text="Enroll",
               command=enroll).pack(pady=5)

    ttk.Button(root, text="Back",
               command=dashboard).pack()

# ---------------- ATTENDANCE ----------------
def attendance_screen():
    clear_window()

    tk.Label(root, text="Attendance",
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Student ID").pack()
    student_entry = tk.Entry(root)
    student_entry.pack()

    tk.Label(root, text="Status (Present / Absent)").pack()
    status_entry = tk.Entry(root)
    status_entry.pack()
    dbconnection()

    def mark_attendance():
        if student_entry.get() and status_entry.get():
            cursor.execute(
                "INSERT INTO attendance (student_id, status) VALUES (:1, :2)",
                (student_entry.get(), status_entry.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Attendance Marked")
            student_entry.delete(0, tk.END)
            status_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields required")

    ttk.Button(root, text="Mark Attendance",
               command=mark_attendance).pack(pady=5)

    ttk.Button(root, text="Back",
               command=dashboard).pack()

# ---------------- REPORTS ----------------
def reports():
    clear_window()

    tk.Label(root, text="Reports",
             font=("Arial", 16)).pack(pady=10)

    text_area = tk.Text(root, width=65, height=18)
    text_area.pack()

    report = "STUDENTS (From Database):\n"
    cursor.execute("SELECT student_id, name FROM students")
    dbconnection()
    for row in cursor.fetchall():
        report += f"{row[0]} - {row[1]}\n"

    report += "\nENROLLMENTS (From Database):\n"
    cursor.execute("SELECT student_id, course_name FROM enrollments")
    for row in cursor.fetchall():
        report += f"{row[0]} → {row[1]}\n"

    report += "\nATTENDANCE (From Database):\n"
    cursor.execute("SELECT student_id, status FROM attendance")
    for row in cursor.fetchall():
        report += f"{row[0]} : {row[1]}\n"

    text_area.insert(tk.END, report)
    text_area.config(state=tk.DISABLED)

    ttk.Button(root, text="Back",
               command=dashboard).pack(pady=5)

# ---------------- START APP ----------------
login_screen()
root.mainloop()