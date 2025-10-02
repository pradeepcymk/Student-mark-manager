#!/usr/bin/env python3
"""
Student Marks Management System - MySQL Version
Author: Python Learning Project
Date: October 2025

This program demonstrates:
- Using MySQL database with mysql-connector-python
- Database operations (CREATE, INSERT, SELECT)
- Object-oriented programming with database integration
- Error handling for database operations

Prerequisites:
- pip install mysql-connector-python
- MySQL server running locally
- Database named 'student_db' (will be created automatically)
"""

import mysql.connector
from mysql.connector import Error

class StudentMarksManagerDB:
    def __init__(self, host='localhost', user='root', password='', database='student_db'):
        """
        Initialize database connection and create tables if they don't exist

        Args:
            host (str): MySQL server host
            user (str): MySQL username
            password (str): MySQL password
            database (str): Database name
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

        # Initialize database and table
        self.connect_and_setup()

    def connect_and_setup(self):
        """Connect to MySQL and setup database and table"""
        try:
            # First connect without database to create it if needed
            temp_connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            temp_cursor = temp_connection.cursor()

            # Create database if it doesn't exist
            temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            temp_cursor.close()
            temp_connection.close()

            # Now connect to the specific database
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()

            # Create students table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                roll_no INT UNIQUE NOT NULL,
                name VARCHAR(100) NOT NULL,
                subject VARCHAR(50) NOT NULL,
                marks DECIMAL(5,2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()

            print("✅ Database connection established successfully!")

        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            print("\nMake sure MySQL is running and credentials are correct.")
            print("You can also use the basic version without MySQL.")

    def add_student(self, roll_no, name, subject, marks):
        """Add a new student record to the database"""
        try:
            query = "INSERT INTO students (roll_no, name, subject, marks) VALUES (%s, %s, %s, %s)"
            values = (roll_no, name, subject, marks)

            self.cursor.execute(query, values)
            self.connection.commit()

            print(f"✓ Added student: {name}")
            return True

        except Error as e:
            print(f"❌ Error adding student {name}: {e}")
            return False

    def display_all_students(self):
        """Display all student records from database"""
        try:
            query = "SELECT roll_no, name, subject, marks FROM students ORDER BY roll_no"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            if not records:
                print("❌ No student records found!")
                return

            print("\n" + "="*70)
            print("                    ALL STUDENT RECORDS (FROM DATABASE)")
            print("="*70)
            print(f"{'Roll No':<10} {'Name':<20} {'Subject':<15} {'Marks':<10}")
            print("-"*70)

            for record in records:
                roll_no, name, subject, marks = record
                print(f"{roll_no:<10} {name:<20} {subject:<15} {marks:<10}")
            print("="*70)

        except Error as e:
            print(f"❌ Error retrieving records: {e}")

    def find_highest_marks(self):
        """Find the student with highest marks from database"""
        try:
            query = "SELECT roll_no, name, subject, marks FROM students ORDER BY marks DESC LIMIT 1"
            self.cursor.execute(query)
            record = self.cursor.fetchone()

            if not record:
                print("❌ No student records found!")
                return None

            roll_no, name, subject, marks = record

            print("\n" + "="*50)
            print("         STUDENT WITH HIGHEST MARKS (FROM DATABASE)")
            print("="*50)
            print(f"Roll No: {roll_no}")
            print(f"Name: {name}")
            print(f"Subject: {subject}")
            print(f"Marks: {marks}")
            print("="*50)

            return record

        except Error as e:
            print(f"❌ Error finding highest marks: {e}")
            return None

    def calculate_average_marks(self):
        """Calculate average marks from database"""
        try:
            # Get total marks and count
            query = "SELECT COUNT(*), SUM(marks), AVG(marks) FROM students"
            self.cursor.execute(query)
            result = self.cursor.fetchone()

            if not result or result[0] == 0:
                print("❌ No student records found!")
                return 0

            count, total_marks, average = result

            print("\n" + "="*40)
            print("        CLASS AVERAGE MARKS (FROM DATABASE)")
            print("="*40)
            print(f"Total Students: {count}")
            print(f"Total Marks: {total_marks}")
            print(f"Average Marks: {average:.2f}")
            print("="*40)

            return float(average)

        except Error as e:
            print(f"❌ Error calculating average: {e}")
            return 0

    def get_subject_wise_stats(self):
        """Get subject-wise statistics from database"""
        try:
            query = """
            SELECT 
                subject, 
                COUNT(*) as student_count,
                AVG(marks) as avg_marks,
                MAX(marks) as max_marks,
                MIN(marks) as min_marks
            FROM students 
            GROUP BY subject
            ORDER BY subject
            """
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print("\n📊 SUBJECT-WISE STATISTICS (FROM DATABASE)")
            print("="*45)

            for record in records:
                subject, count, avg, max_marks, min_marks = record
                print(f"{subject}:")
                print(f"  Students: {count}")
                print(f"  Average: {avg:.2f}")
                print(f"  Highest: {max_marks}")
                print(f"  Lowest: {min_marks}")
                print("-"*25)

        except Error as e:
            print(f"❌ Error getting subject-wise stats: {e}")

    def close_connection(self):
        """Close database connection"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("\n🔌 Database connection closed.")
        except Error as e:
            print(f"❌ Error closing connection: {e}")

def main():
    """Main function demonstrating MySQL version"""
    print("🎓 STUDENT MARKS MANAGEMENT SYSTEM - MySQL Version")
    print("="*60)
    print("⚠️  Note: This requires MySQL server and mysql-connector-python")
    print("    Install with: pip install mysql-connector-python")
    print("="*60)

    # Initialize the system with database
    # Modify these credentials according to your MySQL setup
    sms_db = StudentMarksManagerDB(
        host='localhost',
        user='root',
        password='',  # Add your MySQL password here
        database='student_db'
    )

    if sms_db.connection is None:
        print("\n❌ Could not establish database connection.")
        print("Falling back to basic version or check your MySQL setup.")
        return

    # Insert sample student records
    print("\n📝 Adding Sample Student Records to Database...")
    print("-"*40)

    sample_students = [
        (101, "Alice Johnson", "Mathematics", 95),
        (102, "Bob Smith", "Physics", 87),
        (103, "Carol Davis", "Chemistry", 92),
        (104, "David Wilson", "Mathematics", 78),
        (105, "Emma Brown", "Physics", 89),
        (106, "Frank Miller", "Chemistry", 91),
        (107, "Grace Lee", "Mathematics", 96),
        (108, "Henry Clark", "Physics", 82),
        (109, "Ivy Martinez", "Chemistry", 88)
    ]

    success_count = 0
    for roll_no, name, subject, marks in sample_students:
        if sms_db.add_student(roll_no, name, subject, marks):
            success_count += 1

    print(f"\n✅ Successfully added {success_count}/{len(sample_students)} records to database!")

    print("\n🔥 DEMONSTRATING ALL FUNCTIONS WITH DATABASE")
    print("="*60)

    # Demonstrate all required functions
    sms_db.display_all_students()
    sms_db.find_highest_marks()
    sms_db.calculate_average_marks()
    sms_db.get_subject_wise_stats()

    # Close database connection
    sms_db.close_connection()

    print("\n🎯 MySQL version completed successfully!")

if __name__ == "__main__":
    main()
