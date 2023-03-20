def is_string_in_list(string):
    street_list = ['Аль-Фараби', 'Саина', 'Ташентского', 'Достык']
    if string in street_list:
        return True
    else:
        return False


def calculate_delivery_cost(street, product_price):
    if is_string_in_list(street):
        if product_price < 10000:
            return 500
        else:
            return 0
    else:
        if product_price < 10000:
            return 1000
        else:
            return 0


delivery_cost = calculate_delivery_cost("Достык", 5000)
print(delivery_cost)

delivery_cost = calculate_delivery_cost("Саина", 12000)
print(delivery_cost)

delivery_cost = calculate_delivery_cost("Абая", 5000)
print(delivery_cost)
