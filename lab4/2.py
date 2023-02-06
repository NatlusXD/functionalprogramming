def students_sort():
    students = []
    while True:
        student = input()
        if student == "":
            break
        name, grade = student.split()
        students.append((name, int(grade)))

    def sort_by(x):
        return x[1]

    students.sort(key=sort_by)

    for name, grade in students:
        print(f"{name} класс {grade}")

students_sort()