# Создание словаря с резюме студентов
resumes = {
    "Гоша": "Я опытный инженер-программист, специализирующийся на веб-разработке.",
    "Саша": "Я недавний выпускник со степенью в области компьютерных наук и опытом анализа данных.",
    "Паша": "Я программист-самоучка со страстью к машинному обучению и ИИ.",
    "Вова": "Я младший разработчик с опытом фронтенд-разработки и острым взглядом на дизайн.",
    "Алибек": "Я опытный разработчик, обладающий опытом работы с внутренними системами и послужным списком успешных проектов"
}

def print_keys(dictionary):
    print("\nКлючи: ")
    for key in dictionary.keys():
        print(key)

def print_values(dictionary):
    print("\nЗначения: ")
    for value in dictionary.values():
        print(value)

def print_items(dictionary):
    print("\nВывод ключ-значение: ")
    for key, value in dictionary.items():
        print(key, ': ', value)

def add_resume(dictionary, name, resume):
    dictionary[name] = resume
    print(f"\nДобавление новой записи для студента с именем: {name}")

def remove_dict(dictionary, name):
    del dictionary[name]
    print(f"\nУдаление записи для студента с именем: {name}")

def update_dict(dictionary, name, resume):
    dictionary[name] = resume
    print(f"\nОбновление записи для студента с именем: {name}")



print_keys(resumes)
print_values(resumes)
print_items(resumes)

add_resume(resumes, "Асель", "Я недавний выпускник со степенью в области компьютерной инженерии.")
print_items(resumes)

remove_dict(resumes, "Паша")
print_items(resumes)

update_dict(resumes, "Вова",
              "Я джуниор-разработчик с опытом фронтенд-разработки и страстью к UX-дизайну.")
print_items(resumes)
