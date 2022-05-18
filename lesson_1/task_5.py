"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
в строковый тип на кириллице.
"""
import subprocess
import chardet

ping_results = ''

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results = chardet.detect(line)
    print(ping_results)
    line = line.decode(ping_results['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
