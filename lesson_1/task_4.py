"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""
byte_words = []
words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    byte_words.append(word.encode('utf-8'))

for word in byte_words:
    print(word.decode('utf-8'))
