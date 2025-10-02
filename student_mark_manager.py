#!/usr/bin/env python3
"""
Student Marks Management System
Author: Python Learning Project
Date: October 2025

This program demonstrates:
- Using Lists and Dictionaries to store data
- Object-oriented programming with classes
- Functions for data manipulation
- Console-based user interface
"""

class StudentMarksManager:
    def __init__(self):
        """Initialize the student management system with an empty list"""
        self.students = []

    def add_student(self, roll_no, name, subject, marks):
        """
        Add a new student record to the system

        Args:
            roll_no (int): Student's roll number
            name (str): Student's name
            subject (str): Subject name
            marks (int/float): Marks obtained
        """
        student = {
            'roll_no': roll_no,
            'name': name,
            'subject': subject,
            'marks': marks
        }
        self.students.append(student)
        print(f"✓ Added student: {name}")

    def display_all_students(self):
        """Display all student records in a formatted table"""
        if not self.students:
            print("❌ No student records found!")
            return

        print("\n" + "="*70)
        print("                    ALL STUDENT RECORDS")
        print("="*70)
        print(f"{'Roll No':<10} {'Name':<20} {'Subject':<15} {'Marks':<10}")
        print("-"*70)

        for student in self.students:
            print(f"{student['roll_no']:<10} {student['name']:<20} {student['subject']:<15} {student['marks']:<10}")
        print("="*70)

    def find_highest_marks(self):
        """Find and return the student with the highest marks"""
        if not self.students:
            print("❌ No student records found!")
            return None

        top_student = max(self.students, key=lambda x: x['marks'])

        print("\n" + "="*50)
        print("         STUDENT WITH HIGHEST MARKS")
        print("="*50)
        print(f"Roll No: {top_student['roll_no']}")
        print(f"Name: {top_student['name']}")
        print(f"Subject: {top_student['subject']}")
        print(f"Marks: {top_student['marks']}")
        print("="*50)

        return top_student

    def calculate_average_marks(self):
        """Calculate and return the average marks of all students"""
        if not self.students:
            print("❌ No student records found!")
            return 0

        total_marks = sum(student['marks'] for student in self.students)
        average = total_marks / len(self.students)

        print("\n" + "="*40)
        print("        CLASS AVERAGE MARKS")
        print("="*40)
        print(f"Total Students: {len(self.students)}")
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average:.2f}")
        print("="*40)

        return average

    def get_student_count(self):
        """Return the total number of students"""
        return len(self.students)

    def find_student_by_roll_no(self, roll_no):
        """Find a student by roll number"""
        for student in self.students:
            if student['roll_no'] == roll_no:
                return student
        return None

    def get_subject_wise_stats(self):
        """Calculate subject-wise statistics"""
        subjects = {}
        for student in self.students:
            subject = student['subject']
            if subject not in subjects:
                subjects[subject] = []
            subjects[subject].append(student['marks'])

        print("\n📊 SUBJECT-WISE STATISTICS")
        print("="*35)
        for subject, marks_list in subjects.items():
            avg = sum(marks_list) / len(marks_list)
            max_marks = max(marks_list)
            min_marks = min(marks_list)
            print(f"{subject}:")
            print(f"  Average: {avg:.2f}")
            print(f"  Highest: {max_marks}")
            print(f"  Lowest: {min_marks}")
            print(f"  Students: {len(marks_list)}")
            print("-"*20)

def main():
    """Main function to run the student management system"""
    print("🎓 STUDENT MARKS MANAGEMENT SYSTEM")
    print("="*50)

    # Initialize the system
    sms = StudentMarksManager()

    # Insert sample student records (more than 5 as required)
    print("\n📝 Adding Sample Student Records...")
    print("-"*30)

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

    for roll_no, name, subject, marks in sample_students:
        sms.add_student(roll_no, name, subject, marks)

    print(f"\n✅ Successfully added {len(sample_students)} student records!")

    print("\n🔥 DEMONSTRATING ALL REQUIRED FUNCTIONS")
    print("="*50)

    # Required Function 1: Display all student records
    sms.display_all_students()

    # Required Function 2: Find student with highest marks
    sms.find_highest_marks()

    # Required Function 3: Calculate average marks of the class
    sms.calculate_average_marks()

    # Bonus: Additional statistics
    sms.get_subject_wise_stats()

    print("\n🎯 Program execution completed successfully!")

if __name__ == "__main__":
    main()
