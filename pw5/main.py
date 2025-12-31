from input import input_student_info, input_course_info, input_marks
from output import list_students, list_courses, show_marks
from domains.Students import Student
from domains.Courses import Course
import numpy as np #type: ignore

def GPA(students, courses, marks):
    c_credits = {c.id: c.credit for c in courses}
    for student in students:
        mark_list = []
        credit_list = []
        #Get all marks and credits from student
        for c_id in marks:
            if student.id in marks[c_id]:
                score = marks[c_id][student.id]
                credit = c_credits.get(c_id, 0)

                mark_list.append(score)
                credit_list.append(credit)
        #Calculate and Assign GPA, no return
        if mark_list:
            marks_array = np.array(mark_list)
            credits_array = np.array(credit_list)

            if np.sum(credits_array) > 0:
                gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
                student.gpa = round(gpa, 2)
            else:
                student.gpa = 0.0
        else:
            student.gpa = 0.0   #if student have no mark => gpa = 0.0

def sort_students(students):
    students.sort(key = lambda s: s.gpa, reverse = True)

def main():
    students = []
    courses = []
    marks = {}
    while True:
        print("\n--- Student Mark Management ---\n")
        print("0. Exit Program")
        print("1. Input Student Info")
        print("2. Input Course Info")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Course Marks")
        print("7. Students GPA sorted list")

        try:
            opt = int(input("\nSelect an option: "))

            if opt == 0:    
                print("End Program!")   
                break
            if opt == 1:  
                s = input_student_info()
                students.extend(s)      #add student's info into list
            elif opt == 2:  
                c = input_course_info()
                courses.extend(c)       #add course's info into list
            elif opt == 3:  
                m = input_marks(courses, students)
                for c_id, s_marks in m.items():
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id].update(s_marks)
            elif opt == 4:  list_students(students)
            elif opt == 5:  list_courses(courses)
            elif opt == 6:  
                c_id = input("Enter Course ID to show marks: ")
                if c_id in marks:
                    show_marks(students, c_id, marks[c_id])
                else:
                    print("No marks found!")
            elif opt == 7:  
                GPA(students, courses, marks)
                sort_students(students)
                list_students(students)
                
        except ValueError:
            print("Invalid option. Please enter any option from 0-7")

main()