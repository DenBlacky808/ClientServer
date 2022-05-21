"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

"""
import csv
import re


def get_data():
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    data_list = []
    for i in range(1, 4):
        with open(f'info_{i}.txt') as txt_f:
            spam_list = []
            for line in txt_f:
                for reg in main_data:
                    if re.match(reg, line) is not None:
                        spam_list.append(line.strip().split(':')[1].strip())

        spam_list[0], spam_list[1], spam_list[2], spam_list[3] = spam_list[2], ' '.join(spam_list[0].split()[1:3]), \
                                                                 spam_list[1], \
                                                                 ' '.join(spam_list[3].split()[0:1])
        data_list.append(spam_list)
        with open('main_data', 'w') as main_file:
            i = 1
            for line in data_list:
                main_file.write(f'{i},' + ','.join(line) + '\n')
                i += 1
    return main_data


def write_to_csv(name):
    main_data_list = [get_data()]
    with open('main_data') as main_data_file:
        for line in main_data_file:
            main_data_list.append(line[:-2].split(','))
    print(main_data_list)
    with open(name, 'w', newline='\n') as f_n:
        f_n_writer = csv.writer(f_n)
        for line in main_data_list:
            f_n_writer.writerow(line)


write_to_csv('data_report.csv')
