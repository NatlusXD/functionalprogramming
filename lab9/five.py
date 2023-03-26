def compose_functions(f, g):
    def h(x):
        return f(g(x))

    return h


def add_two(x):
    return x + 2


def multiply_by_three(x):
    return x * 3


composed_function = compose_functions(add_two, multiply_by_three)
result = composed_function(5)
print(result)
