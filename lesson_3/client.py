import sys
import json
import socket
import time
from common.variables import action, presence, time_var, user, acc_name, \
    response, error, ip_address, port
from common.utils import get_message, send_message


def create_presence(account_name='Guest'):

    out = {
        action: presence,
        time_var: time.time(),
        user: {
            acc_name: account_name
        }
    }
    return out


def process_ans(message):

    if response in message:
        if message[response] == 200:
            return '200 : OK'
        return f'400 : {message[error]}'
    raise ValueError


def main():

    try:
        server_address = sys.argv[2]
        server_port = int(sys.argv[3])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = ip_address
        server_port = port
    except ValueError:
        print('порт может быть от 1024 до 65535.')
        sys.exit(1)

    trans_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trans_sock.connect((server_address, server_port))
    msg_to_serv = create_presence()
    send_message(trans_sock, msg_to_serv)
    try:
        answer = process_ans(get_message(trans_sock))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не получилось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
