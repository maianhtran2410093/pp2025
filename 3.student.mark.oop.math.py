#import
import math
import numpy as np # type: ignore

class Student:
    def __init__(self, s_id, s_name, s_dob):
        self.__s_id = s_id  #apply encapsulation throughout
        self.__s_name = s_name
        self.__s_dob = s_dob
        #add s_gpa into __init__
        self.__s_gpa = 0.0

    @property
    def id(self):   return self.__s_id
    @property
    def name(self): return self.__s_name
    #getter gpa
    @property
    def gpa(self):  return self.__s_gpa
    #setter gpa
    @gpa.setter
    def gpa(self, value):
        self.__s_gpa = value
    def __str__(self):
        return f"ID: {self.__s_id}  Name: {self.__s_name}   DoB: {self.__s_dob}     GPA: {self.__s_gpa}"

class Course:
    def __init__(self, c_id, c_name, c_credit):
        self.__c_id = c_id 
        self.__c_name = c_name
        #add c_credit into __init__
        self.__c_credit = c_credit

    @property
    def id(self):       return self.__c_id
    @property
    def name(self):     return self.__c_name
    #getter credit
    @property
    def credit(self):   return self.__c_credit

    def __str__(self):
        return f"ID: {self.__c_id}  Name: {self.__c_name}   Credits: {self.__c_credit}"

class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}

    #For Students:
    def input_nb_of_students(self):
        while True:
            try:
                n = int(input("Number of students: "))
                if (n <= 0):
                    print("Must be positive")
                    continue
                else:
                    return n
            except ValueError:
                print("Invalid input. Please enter a number!")
    
    def input_student_info(self):
        n = self.input_nb_of_students()
        for i in range (n):
            print(f"\n--- Enter Student {i+1} Info ---")
            try:
                s_id = int(input("Student ID: "))
                s_name = input("Student Name: ")
                s_dob = input("DoB: ")
                student = Student(s_id, s_name, s_dob)
                self._students.append(student)
            except ValueError:
                print("Invalid input data!")

    def list_students(self):
        print("\n--- Student List ---")
        for student in self._students:
            print(student)
    
    #For Courses:
    def input_nb_of_courses(self):
        while True:
            try:
                m = int(input("Number of courses: "))
                if (m <= 0):
                    print("Must be positive")
                    continue
                else:
                    return m
            except ValueError:
                print("Invalid input. Please enter a number!")

    def input_course_info(self):
        m = self.input_nb_of_courses()
        for i in range (m):
            print(f"\n--- Enter Course {i+1} Info ---")
            try:
                c_id = input("Course ID: ")
                c_name = input("Course Name: ")
                c_credit = int(input("Course Credits: "))
                course = Course(c_id, c_name, c_credit)
                self._courses.append(course)
            except ValueError:
                print("Invalid input data!")

    def list_courses(self):
        print("\n--- Course List ---")
        for course in self._courses:
            print(course)

    #For Marks:
    def get_valid_course_id(self):
        print('\n--- Available Courses ---')
        self.list_courses()
        while True:
            try:
                course_id_to_check = input("\nEnter the Course ID: ")
                for course in self._courses:
                    if course.id == course_id_to_check:
                        return course_id_to_check
                print("Course Not Found")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    #Round scores to 1-digit decimal
    def round_mark(self, mark):
        return math.floor(mark * 10) / 10
    
    def input_marks(self):
        if not self._courses:
            print("No courses available")
            return
        if not self._students:
            print("No students found!")
            return
        
        course_id = self.get_valid_course_id()
        
        if course_id not in self._marks:
            self._marks[course_id] = {}
        print(f'\n--- Entering Marks for Course ID: {course_id} ---')
        for student in self._students:
            origin_mark = float(input(f"Enter mark for {student.name}: "))
            #round mark here
            mark_value = self.round_mark(origin_mark)
            if 0 <= mark_value <= 20:
                self._marks[course_id][student.id] = mark_value
            else:
                print("Mark must be in range 0-20!")

    def show_marks(self):
        if not self._marks:
            print("No marks yet!")
            return
        
        c_id = self.get_valid_course_id()
        c_marks = self._marks.get(c_id, {})

        print(f"\n--- Marks for Course ID: {c_id} ---")
        for student in self._students:
            mark = c_marks.get(student.id, "N/A")
            print(f"Student: {student.name} (ID: {student.id})\t Mark: {mark}")

    #Calculate avg GPA for each student
    def GPA(self, s_id):
        marks_list = []
        credits_list = []

        for course in self._courses:
            c_id = course.id

            if c_id in self._marks and s_id in self._marks[c_id]:
                mark = self._marks[c_id][s_id]
                marks_list.append(mark)
                credits_list.append(course.credit)
        if not marks_list:
            return 0.0
        #list to numpy
        marks_array = np.array(marks_list)
        credits_array = np.array(credits_list)
        #calculate gpa
        gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
        return round(gpa, 2)       #round the GPA to 2-decimal
    
    def updated_GPA(self):
        for student in self._students:
            gpa = self.GPA(student.id)
            student.gpa = gpa
    
    #Sort in descending list of gpa
    def sort_students_by_desc_gpa(self):
        self.updated_GPA()
        self._students.sort(key = lambda s: s.gpa, reverse=True)

    def main(self):
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
                if opt == 1:  self.input_student_info()
                elif opt == 2:  self.input_course_info()
                elif opt == 3:  self.input_marks()
                elif opt == 4:  self.list_students()
                elif opt == 5:  self.list_courses()
                elif opt == 6:  self.show_marks()
                elif opt == 7:  
                    self.sort_students_by_desc_gpa()
                    self.list_students()
            except ValueError:
                print("Invalid option. Please enter any option from 0-7")

if __name__ == "__main__":
    run = StudentMarkManagement()
    run.main()