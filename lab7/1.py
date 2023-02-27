n = int(input("Количество записей: "))
rivers = {}
for i in range(n):
    country, river = input("Введите страну и реку: ").split()
    rivers[river] = country

print("Реки в странах:")
for river, country in rivers.items():
    print(f"{river} - {country}")

search_river = input("river search: ")
if search_river in rivers:
    print("Река найдена.")
else:
    print("Река не найдена.")

new_country, new_river = input("Добавить страну и реку: ").split()
rivers[new_river] = new_country

print("Новая страна или река была добавлена: ")
for river, country in rivers.items():
    print(f"{river} - {country}")
