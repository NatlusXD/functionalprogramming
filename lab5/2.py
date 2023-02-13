grades = {
    'Gosha': [85, 95, 88],
    'Sasha': [88, 82, 85],
    'Alibek': [86, 83, 94]
}

def get_student_grades(student_name):
    if student_name in grades:
        return grades[student_name]
    else:
        return None

student_name = input('Введите имя студента: ')

student_grades = get_student_grades(student_name)

if student_grades:
    print(f'Оценки студента {student_name}: {student_grades}')
else:
    print(f'Студент с именем {student_name}: не найден')