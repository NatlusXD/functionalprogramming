from functools import reduce

numbers = [1, 2, 3, 4, 5]

result_map = list(map(lambda x: x * 2, numbers))

result_filter = list(filter(lambda x: x % 2 == 0, numbers))

result_reduce = reduce(lambda x, y: x + y, numbers)

print(result_map)
print(result_filter)
print(result_reduce)
