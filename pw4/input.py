from domains.Students import Student
from domains.Courses import Course
import math

def input_student_info():
    students = []
    while True:
        try:
            n = int(input("Number of students: "))
            if (n > 0):
                for i in range (n):
                    print(f"\n--- Enter Student {i+1} Info ---")
                    try:
                        s_id = int(input("Student ID: "))
                        s_name = input("Student Name: ")
                        s_dob = input("DoB: ")
                        student = Student(s_id, s_name, s_dob)
                        students.append(student)
                    except ValueError:
                        print("Invalid input data!")
                return students
            else:
                print("Must be positive!")
        except ValueError:
            print("Invalid input. Please enter a number!")

def input_course_info():
    courses = []
    while True:
        try:
            m = int(input("Number of courses: "))
            if (m > 0):
                for i in range (m):
                    print(f"\n--- Enter Course {i+1} Info ---")
                    try:
                        c_id = (input("Course ID: "))
                        c_name = input("Course Name: ")
                        c_credit = int(input("Course Credits: "))
                        course = Course(c_id, c_name, c_credit)
                        courses.append(course)
                    except ValueError:
                        print("Invalid input data!")
                return courses
            else:
                print("Must be positive!")
        except ValueError:
            print("Invalid input. Please enter a number!")
    
def input_marks(courses, students):
    marks = {}
    while True:
        try:
            course_id_to_check = input("\nEnter the Course ID: ")
            
            #1. Find valid course
            selected_course = None
            for course in courses:
                if course.id == course_id_to_check:
                    if course.id not in marks:
                        selected_course = course
                        break
            #2. If found, enter marks
            if selected_course:
                if selected_course.id not in marks:
                    marks[selected_course.id] = {}
                print(f'\n--- Entering Marks for Course ID: {selected_course.id} ---')
                for student in students:
                    while True:
                        try:
                            mark = float(input(f"Enter mark for {student.name}: "))
                            if 0 <= mark <= 20:
                                marks[selected_course.id][student.id] = mark
                                break
                            else:
                                print("Mark must be in range 0-20!")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                return marks
            print("Course Not Found")
        except ValueError:
            print("Invalid input")