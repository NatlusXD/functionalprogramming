import random
#Функция для создания кортежа случайных целых чисел в диапазоне от start до end.
def create_tuple(length, start, end):

    return tuple(random.randint(start, end) for _ in range(length))

# Создаем два кортежа с помощью функции create_tuple
tuple1 = create_tuple(10, 0, 5)
tuple2 = create_tuple(10, -5, 0)

# Объединяем два кортежа в третий кортеж с помощью оператора +
tuple3 = tuple1 + tuple2

# Используем метод count() для подсчета количества нулей в третьем кортеже
count_zeroes = tuple3.count(0)

# Выводим третий кортеж и количество нулей в нем
print("Третий кортеж: ", tuple3)
print("Количество нулей в третьем кортеже: ", count_zeroes)
