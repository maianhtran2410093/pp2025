from domains.Students import Student
from domains.Courses import Course
import zipfile
import os
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
                
                #Writing to file students.txt after input
                try:
                    with open("students.txt", "a") as f:
                        for student in students:
                            f.write(str(student) + "\n")
                    print("Complete writing student info into 'students.txt'")
                except IOError:
                    print("Error: Could not write to 'students.txt'")
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
                
                #Writing to file courses.txt after input
                try:
                    with open("courses.txt", "a") as f:
                        for course in courses:
                            f.write(str(course) + "\n")
                    print("Complete writing course info into 'courses.txt'")
                except IOError:
                    print("Error: Could not write to 'courses.txt'")
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
                
                #Writing to file marks.txt after input
                try:
                    with open("marks.txt", "a") as f:
                        for course_id, student_scores in marks.items():
                            for s_id, score in student_scores.items():
                                f.write(f"Course: {course_id} | Student ID: {s_id} | Mark: {score}\n")
                    print("Complete writing mark info into 'marks.txt'")
                except IOError:
                    print("Error: Could not write to 'marks.txt'")
                return marks
            print("Course Not Found")
        except ValueError:
            print("Invalid input")

#Compress all files '.txt' into 'students.dat'
def compress_file():
    files_to_compress = ['students.txt', 'courses.txt', 'marks.txt']
    output_dat_file = 'students.dat'
    try:
        #Open .dat file in 'w' (write) mode
        with zipfile.ZipFile(output_dat_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files_to_compress:
                #check if file exist before adding
                if os.path.exists(file):
                    print(f"Adding {file} to {output_dat_file}...")
                    #add file to archive
                    #write(): file name as will appear inside archive
                    zipf.write(file, os.path.basename(file))
                else:
                    print(f"Error: {file} not found.")
        print(f"Successfully created the archive: {output_dat_file}")
    
    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def decompress_and_load():
    dat_file = 'students.dat'
    if os.path.exists(dat_file):
        print(f"Found {dat_file}. Extracting data...")
        try:
            with zipfile.ZipFile(dat_file, 'r') as zipf:
                zipf.extractall()
            print("Data extracted successfully!")
        except Exception:
            print("Error extracting data")
    else:
        print(f"\nCheck dailed: '{dat_file}' does not exist!")