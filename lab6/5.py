text = input("Введите казахский текст: ")

translit_dict = {
    "а": "a", "ә": "á", "б": "b", "в": "v", "г": "g",
    "ғ": "ǵ", "д": "d", "е": "e", "ё": "io", "ж": "j",
    "з": "z", "и": "i", "й": "ı", "к": "k", "қ": "q",
    "л": "l", "м": "m", "н": "n", "ң": "ń", "о": "o",
    "ө": "ó", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "ý", "ұ": "u", "ү": "ú", "ф": "f", "х": "h",
    "һ": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ъ": "", "ы": "y", "і": "i", "ь": "", "э": "e",
    "ю": "iu", "я": "ia"
}

translit_text = ""
for char in text:
    if char.lower() in translit_dict:
        if char.isupper():
            translit_text += translit_dict[char.lower()].capitalize()
        else:
            translit_text += translit_dict[char]
    else:
        translit_text += char

print("Казахский текст в латинице: ", translit_text)
