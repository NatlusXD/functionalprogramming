from functools import reduce

nums = [1, 8, 6, 4, 12]
squared_numbers = list(map(lambda x: x ** 2, nums))
print(squared_numbers)

nums = [1, 8, 6, 4, 12]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

nums = [1, 8, 6, 4, 12]
prod = reduce(lambda x, y: x * y, nums)
print(prod)
