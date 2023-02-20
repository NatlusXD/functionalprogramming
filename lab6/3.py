days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
categories = ['Транспорт', 'Завтрак', 'Обед', 'Ужин', 'Другое']

# Создаем пустой список для хранения расходов
expenses = []

# Заполняем список расходов с помощью вложенного цикла
for day in days:
    daily_expenses = []
    print(f"Введите затраты в {day}:")
    for category in categories:
        expense = float(input(f"{category}: "))
        daily_expenses.append(expense)
    expenses.append(daily_expenses)

# Выводим общий объем расходов за неделю
total_expenses = 0
for daily_expenses in expenses:
    total_expenses += sum(daily_expenses)
print(f"Общий объем затрат: {total_expenses}")
