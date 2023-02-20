# Запросить у пользователя имена студентов через пробел
student_names = input("Введите имена студентов через пробел: ")

student_names_list = student_names.split()

# Создать кортеж из списка имен
student_names_tuple = tuple(student_names_list)

# Создать пустую строку для хранения имен, содержащих "ва"
names_with_va = ""

# Пройти по каждому имени в кортеже
for name in student_names_tuple:
    if "ва" in name:
        names_with_va += name + " "

# Вывести имена, содержащие "ва"
print("Имена, содержащие 'ва':", names_with_va)
