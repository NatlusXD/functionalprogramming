def get_data() -> tuple:
    data_list = [1, 2, 3, 4, 5]
    data_tuple = ("jotaro", "johnathan", "josuke")
    data_dict = {"name": "giorno", "age": 17, "city": "rome"}
    return data_list, data_tuple, data_dict


my_list, my_tuple, my_dict = get_data()
print(my_list)
print(my_tuple)
print(my_dict)
