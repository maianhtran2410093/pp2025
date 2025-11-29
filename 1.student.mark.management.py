STUDENTS = []
COURSES = []
MARKS = {}

def input_nb_of_students():
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

def input_student_info():
    n = input_nb_of_students()
    for i in range (n):
        print(f"\n--- Enter Student {i+1} Info ---")
        s_id = int(input("Student ID: "))
        s_name = input("Student Name: ")
        dob = input("DoB: ")
        student = {"ID": s_id, "Name": s_name, "DoB": dob}
        STUDENTS.append(student)

def input_nb_of_courses():
    while True:
        try:
            m = int(input('Number of courses: '))
            if (m <= 0):
                print('Must be positive')
                continue
            else:
                return m
        except ValueError:
            print('Invalid input. Please enter a number!')

def input_course_info():
    m = input_nb_of_courses()
    for i in range (m):
        print(f'\n--- Enter Course {i+1} Info ---')
        c_id = int(input('Course ID: '))
        c_name = input('Course Name: ')
        course = {'ID': c_id, 'Name': c_name}
        COURSES.append(course)

def get_valid_course_id():
    print('\n--- Available Courses ---')
    for course in COURSES:
        print(f'ID: {course['ID']}, Name: {course['Name']}')
    while True:
        try:
            course_id_to_check = int(input('\nEnter the Course ID to input marks for: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        for course in COURSES:
            if course['ID'] == course_id_to_check:
                return course_id_to_check
        print('Course Not Found')

def input_marks():
        valid_course_id = get_valid_course_id()
        if valid_course_id not in MARKS:
            MARKS[valid_course_id] = {}
        print(f'\n--- Entering Marks for Course ID: {valid_course_id} ---')
        for student in STUDENTS:
            student_id = student['ID']
            student_name = student['Name']
            mark_value = float(input("Enter mark: "))
            MARKS[valid_course_id][student_id] = mark_value

def list_students():
    print("\n--- Student List ---")
    for student in STUDENTS:
        print(f"ID: {student['ID']}, Name: {student['Name']}, DoB: {student['DoB']}")

def list_courses():
    print("\n--- Course List ---")
    for course in COURSES:
        print(f"ID: {course['ID']}, Name: {course['Name']}")

def show_marks():
    valid_course_id = get_valid_course_id()
    marks_for_course = MARKS.get(valid_course_id, {})
    print(f"\n--- Marks for Course ID: {valid_course_id} ---")
    for student in STUDENTS:
        student_id = student['ID']
        student_name = student['Name']
        mark = marks_for_course.get(student_id, 'N/A')
        print(f"Student: {student_name} (ID: {student_id})\t Mark: {mark}")

def main():
    while True:
        print("\n---Student Mark Management ---\n")
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
            input_student_info()
        elif opt == 2:
            input_course_info()
        elif opt == 3:
            input_marks()
        elif opt == 4:
            list_students()
        elif opt == 5:
            list_courses()
        elif opt == 6:
            show_marks()
        elif opt == 0:
            print("End program!")
            break
        else:
            print("Invalid option. Please enter any option from 0-6")
            continue
        
if __name__ == "__main__":
    main()