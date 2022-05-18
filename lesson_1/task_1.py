"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
"""

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'

words = [word_1, word_2, word_3]

for word in words:
    print(type(word), word)

words_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    ]
for word in words_unicode:
    print(type(word), word)