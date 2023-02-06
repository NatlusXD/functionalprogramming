def string_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()

while True:
    s = input()
    print(string_case(s))
    print(string_case(s).isupper())
