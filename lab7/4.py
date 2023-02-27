n = int(input('Кол-во сотрудников: '))
vacations = {}

for i in range(n):
    name, day, month = input('Введите имя, день и месяц через запятую: ').split()
    if month not in vacations:
        vacations[month] = []
    vacations[month].append(name)

requested_month = input('Введите месяц для поиска: ')
if requested_month in vacations:
    print(' '.join(vacations[requested_month]))
else:
    print('Нет сотрудников в отпуске в этом месяце')
