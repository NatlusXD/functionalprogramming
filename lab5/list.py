def find_longest_word(list):
    return max(list, key=len)

def find_shortest_word(list):
    return min(list, key=len)

def count_words(list):
    return len(list)

def reverse_list(list):
    return list[::-1]

def sort_list(list):
    return sorted(list)

words = input("Введите слова списка через пробел: ").split()
print("Список: ", words)

longest_word = find_longest_word(words)
print("Самое длинное слово в списке: ", longest_word)

shortest_word = find_shortest_word(words)
print("Самое короткое слово в списке: ", shortest_word)

word_count = count_words(words)
print("Количество слов в списке: ", word_count)

reversed_list = reverse_list(words)
print("Список наоборот: ", reversed_list)

sorted_list = sort_list(words)
print("Отсортированный список: ", sorted_list)
