def find_longest_word(lst):
    return max(lst, key=len)

def find_shortest_word(lst):
    return min(lst, key=len)

def count_words(lst):
    return len(lst)

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

words = input("Введите слова списка через пробел: ").split()
print("Список: ", words)

longest_word = find_longest_word(words)
print("Самое длинное слово в списке: ", longest_word)

shortest_word = find_shortest_word(words)
print("самое короткое слово в списке: ", shortest_word)

word_count = count_words(words)
print("Количество слов в спискке: ", word_count)

reversed_list = reverse_list(words)
print("Список наоборот: ", reversed_list)

sorted_list = sort_list(words)
print("Отсортированный список: ", sorted_list)
