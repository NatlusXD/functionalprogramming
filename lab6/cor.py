# Создаем множество студентов
students = {
    ("Георгий", "Статенин", 20, "Computer Science", 3.2),
    ("Студент1", "Студент1", 21, "Mathematics", 3.3),
    ("Студент2", "Студент2", 23, "Mathematics", 3.9),
    ("Студент3", "Студент3", 20, "Computer Science", 3.7),
}

# Функция для вывода всех студентов из множества
def print_students():
    for student in students:
        print(student)

# Функция для поиска студента по имени
def search_student_by_name(name):
    for student in students:
        if student[0] == name:
            return student
    return None

# Функция для добавления нового студента
def add_student(student):
    students.add(student)

# Функция для удаления студента
def remove_student(student):
    students.discard(student)

# Функция для получения количества студентов в множестве
def count_students():
    return len(students)

# Выводим всех студентов
print("Все студенты:")
print_students()

# Ищем студента по имени
print("\nСтудент с именем Георгий:")
print(search_student_by_name("Георгий"))

# Добавляем нового студента
new_student = ("Студент4", "Студент4", 20, "Computer Science", 3.5)
add_student(new_student)
print("\nНовый список всех студентов:")
print_students()

# Удаляем студента
remove_student(("Студент2", "Студент2", 23, "Mathematics", 3.9))
print("\nНовый список после удаления студента:")
print_students()

# Получаем количество студентов в множестве
print("\nОбщее колиство студентов:", count_students())
