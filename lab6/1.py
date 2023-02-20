import random

#Функция для создания кортежа случайных целых чисел в диапазоне от start до end.
def create_tuple(length, start, end):

    return tuple(random.randint(start, end) for i in range(length))

tuple1 = create_tuple(10, 0, 5)
tuple2 = create_tuple(10, -5, 0)

tuple3 = tuple1 + tuple2

print("Третий кортеж: ", tuple3)
print("Количество нулей в третьем кортеже: ", tuple3.count(0))
