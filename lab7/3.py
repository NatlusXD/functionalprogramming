n = int(input('Кол-во номеров: '))

phone_book = {}

for i in range(n):
    phone, name = input('Введите номер телефона и контакт: ').split()
    phone_book[name] = phone

person = input('Поиск по контакту: ')

if person in phone_book:
    print(phone_book[person])
else:
    print("Нет в телефонной книге")
