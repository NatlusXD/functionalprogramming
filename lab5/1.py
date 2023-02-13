students = {}

while True:
    student = input('Введите студента: ')
    if student == '':
        break
    subject = input('Введите предмет: ')
    if subject in students:
        students[subject].append(student)
    else:
        students[subject] = [student]

for subject, student_list in sorted(students.items()):
    print(f'Предмет: {subject}')
    print(f'Студенты: {", ".join(sorted(student_list))}')