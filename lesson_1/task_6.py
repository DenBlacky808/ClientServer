"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и
 вывестbи его содержимое.
"""

from chardet import detect

with open('test_file.txt', 'rb') as file_obj:
    content_bytes = file_obj.read()
detected = detect(content_bytes)
encoding_type = detected['encoding']
content_text = content_bytes.decode(encoding_type)
with open('test_file.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write(content_text)

with open('test_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()
print(content)
