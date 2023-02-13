grades = {
    'Gosha': [85, 95, 88, 90],
    'Sasha': [88, 82, 85, 95],
    'Alibek': [86, 83, 94, 92]
}

def get_student_grades(student_name):
    if student_name in grades:
        return grades[student_name]
    else:
        return None

student_name = input("Введите имя студента: ")

student_grades = get_student_grades(student_name)

if student_grades:
    print(f'Grades for student {student_name}: {student_grades}')
else:
    print(f'No grades found for student {student_name}')