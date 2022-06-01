import sys
import json
import socket
import time
import argparse
import logging
from errors import ReqFieldMissingError
import logs.config_client_log

from common.variables import action, presence, time_var, user, acc_name, \
    response, error, ip_address, port
from common.utils import get_message, send_message

CLIENT_LOGGER = logging.getLogger('client')


def create_presence(account_name='Guest'):
    out = {
        action: presence,
        time_var: time.time(),
        user: {
            acc_name: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {presence} сообщение для пользователя {account_name}')
    return out


def process_ans(message):
    CLIENT_LOGGER.debug(f'Cообщение от сервера: {message}')
    if response in message:
        if message[response] == 200:
            return '200 : OK'
        return f'400 : {message[error]}'
    raise ReqFieldMissingError(response)


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=ip_address, nargs='?')
    parser.add_argument('port', default=port, type=int, nargs='?')
    return parser


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    if server_port < 1024 or server_port > 65535:
        CLIENT_LOGGER.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
            f' порт может быть от 1024 до 65535.')
        sys.exit(1)

    CLIENT_LOGGER.info(f'Запущен клиент с парамертами: '
                       f'адрес сервера: {server_address}, порт: {server_port}')

    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        answer = process_ans(get_message(transport))
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}')
        print(answer)
    except json.JSONDecodeError:
        CLIENT_LOGGER.error('Не получилось декодировать сообщение сервера.')
    except ReqFieldMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле '
                            f'{missing_error.missing_field}')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}, '
                               f'конечный компьютер отверг запрос на подключение.')


if __name__ == '__main__':
    main()
