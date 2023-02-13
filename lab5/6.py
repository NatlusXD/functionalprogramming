def is_sorted(numbers):
    return numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)


numbers = list(map(int, input("Введите числа через пробел: ").split()))
if is_sorted(numbers):
    print("Список отсортирован")
else:
    print("Список не отсортирован")