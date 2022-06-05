import logging

port = 7777
ip_address = '127.0.0.1'
max_connect = 5
max_pack_length = 1024
encoding = 'utf-8'
logging_level = logging.DEBUG

action = 'action'
time_var = 'time'
user = 'user'
acc_name = 'acc_name'
sender = 'sender'
destination = 'to'

presence = 'presence'
response = 'response'
error = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
exit_var = 'exit'

# Словари - ответы:
# 200
RESPONSE_200 = {response: 200}
# 400
RESPONSE_400 = {
    response: 400,
    error: None
}