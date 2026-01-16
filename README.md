# Student Management System

The Student Management System is a desktop-based application developed using Python. It provides an easy-to-use graphical interface for managing student information, enrollments, attendance, and reports. The system uses Oracle Database as the backend and Tkinter for the graphical user interface.

# Project Overview

This application is designed to support two types of users: Admin and Student. Based on the selected role, users are given access to different functionalities. Admin users can manage students, mark attendance, and view reports, while students can enroll in courses.

# Features
## Login System

Role-based login (Admin or Student)

Simple dashboard navigation

## Admin Module

Add new student records

Mark student attendance

View consolidated reports from the database

## Student Module

Enroll in courses

# Technologies Used

Python 3

Tkinter for GUI

Oracle Database (XE)

oracledb Python library

# System Requirements

Python 3.x installed

Oracle XE Database

Oracle Instant Client

oracledb Python package

Windows / Linux operating system

# Database Used

The system uses Oracle Database to store all application data, including:

Student details

Course enrollments

Attendance records

Ensure the required database tables are created before running the application.

# Application Workflow

The application starts with a login screen.

The user selects a login role (Admin or Student).

After login, the dashboard is displayed based on the selected role.

Admin users can manage students, record attendance, and generate reports.

Student users can enroll in courses.

Users can log out and return to the login screen.

# Advantages

User-friendly interface

Role-based access control

Centralized database storage

Easy to extend and customize

# Limitations

No authentication using username and password

Basic error handling

UI design is minimal

Database credentials are hardcoded

# Future Enhancements

Secure login with username and password

Edit and delete functionality for records

Search and filter options

Enhanced UI design

Improved database connection management

# Conclusion

The Student Management System is a simple yet effective project for learning Python GUI development and database connectivity. It is suitable for academic mini-projects and demonstrates the integration of frontend and backend technologies.

# License
This project is created for educational purposes only.







