class Entity:
    def input(self):
        pass
    def display(self):
        pass

class Student(Entity):
    def __init__(self):
        self.s_id = None
        self.s_name = ""
        self.dob = ""
    
    def input(self):
        self._name = input("Student Name: ")
        self._id = int(input("Student ID: "))
        self._dob = input("DoB: ")

    def print(self):
        print("Name:", self.s_name)
        print("ID:", self.s_id)
        print("DOB:", self.dob)

    def id(self):   return self._id
    def name(self): return self._name
    def dob(self):  return self._dob

class Course(Entity):
    def __init__(self):
        self.c_id = None
        self.c_name = ""
    
    def input(self):
        self._name = input("Course Name: ")
        self._id = int(input("Course ID: "))

    def print(self):
        print("Course Name:", self.c_name)
        print("Course ID:", self.c_id)

    def id(self):   return self._id
    def name(self): return self._name
        

class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}
    
    #this function to get nb of course and nb of students to be always positive
    def get_positive_int(self, message):
        while True:
            try:
                n = int(input(message))
                if n <= 0:
                    print("Must be positive number")
                    continue
                return n
            except ValueError:
                print("Invalid input. Please enter a positive number!")
    
    def input_students(self):
        n = self.get_positive_int("Input number of students: ")
        for i in range(n):
            print(f"\n--- Student {i+1} Info ---")
            s = Student()
            s.input()
            self._students.append(s)

    def input_courses(self):
        m = self.get_positive_int("Input number of courses: ")
        for i in range(m):
            print(f"\n--- Course {i+1} Info ---")
            c = Course()
            c.input()
            self._courses.append(c)

    def get_valid_course(self):
        print("\n--- Available Courses ---")
        for course in self._courses:
            course.print()
        while True:
            try:
                course_id_to_check = int(input('\nEnter the Course ID: '))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            for course in self._courses:
                if course.id == course_id_to_check:
                    return course
            print("Course Not Found")
        
    def input_marks(self):
        course = self.get_valid_course()
        course_id = course.id
        if course not in self._marks:
            self._marks[course_id] = {}
        print(f"\n--- Entering Marks for Course ID: {course_id} ---")
        for student in self._students:
            mark_value = float(input("Enter mark: "))
            self._marks[course_id][student.id] = mark_value
    
    def list_students(self):
        print("\n--- Student List ---")
        for student in self._students:
            student.print()

    def list_courses(self):
        print("\n--- Course List ---")
        for course in self._courses:
            course.print()
    
    def show_marks(self):
        course = self.get_valid_course()
        course_id = course.id
        marks_for_course = self._marks.get(course_id, {})
        print(f"\n--- Marks for Course ID: {course_id} ---")
        for student in self._students:
            mark = marks_for_course.get(student.id, "N/A")
            print(f"Student: {student.name} (ID: {student.id})\t Mark: {mark}")

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

            try:
                opt = int(input("Select an option: "))
            except ValueError:
                print("Invalid option. Please enter any option from 0-6")
                continue

            if opt == 1:
                self.input_students()
            elif opt == 2:
                self.input_course()
            elif opt == 3:
                self.input_marks()
            elif opt == 4:
                self.list_students()
            elif opt == 5:
                self.list_courses()
            elif opt == 6:
                self.show_marks()
            elif opt == 0:
                print("End program!")
                break
            else:
                print("Invalid option. Please enter any option from 0-6")
                continue
        
if __name__ == "__main__":
    run = StudentMarkManagement()
    run.main()