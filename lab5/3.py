numbers = []

while True:
    number = int(input('Введите число: '))
    if number == 0:
        break
    numbers.append(number)

numbers.sort()

for num in numbers:
    print(num)