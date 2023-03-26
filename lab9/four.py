def calculate_cost(street_name, product_price):
    delivery_cost = 0

    if street_name in ["Аль-Фараби", "Саина", "Ташкентская", "Достык"]:
        if product_price < 10000:
            delivery_cost = 500
    else:
        if product_price <= 10000:
            delivery_cost = 1000
        else:
            delivery_cost = 1000 + (product_price - 10000) * 0.1

    return delivery_cost


street = "Аль-Фараби"
price = 12000
total_cost = calculate_cost(street, price)
print("Total delivery cost:", total_cost)
