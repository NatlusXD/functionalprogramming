commentators = {}

while True:
    input_str = input('Введите имя и комментарий, через (:) : ')
    if not input_str:
        break
    name, comment = input_str.split(':')
    commentators[name] = comment

print(commentators)
print(len(commentators))
