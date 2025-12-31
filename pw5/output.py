def list_students(students):
    print("\n--- Student List ---")
    for student in students:
        print(student)

def list_courses(courses):
    print("\n--- Course List ---")
    for course in courses:
        print(course)

def show_marks(students, course_id, course_marks):
    print(f"\n--- Marks for Course ID: {course_id} ---")
    for student in students:
        mark = course_marks.get(student.id, "N/A")
        print(f"Student: {student.name} (ID: {student.id})\t Mark: {mark}")