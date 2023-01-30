n = int(input("Total cards: "))

sum = n * (n + 1) // 2

total_sum = 0
for i in range(n - 1):
    card_number = int(input("Enter card number: "))
    total_sum += card_number


missing_card = sum - total_sum
print("Missing card: ", missing_card)
