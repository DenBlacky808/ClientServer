import json
from common.variables import max_pack_length, encoding


def get_message(client):
    encoded_response = client.recv(max_pack_length)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(encoding)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(encoding)
    sock.send(encoded_message)
