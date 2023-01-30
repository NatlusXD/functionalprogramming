A = int(input("Enter A: "))
B = int(input("Enter B: "))

while A%2 != 1:
    A -= 1

for num in range(A, B-1, -2):
    print(num)