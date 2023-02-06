def input_number():
    while True:
        number = input("Введите число: ")
        if number.isdigit():
            return int(number)
        else:
            print("Введено не число, попробуйте еще раз")

num1 = input_number()
num2 = input_number()
print("Сумма чисел:", num1 + num2)