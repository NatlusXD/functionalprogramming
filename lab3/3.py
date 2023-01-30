from random import random, randint, randrange

a = randint(0, 100)
print(a)

if a % 2 == 0:
    list_test = list(range(randrange(0, 50)))
    print(list_test)

else:
    b = random() * 10
    print(b)

text = 'Georgii'
for char in enumerate(text):
    print(char)
