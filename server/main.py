import datetime
import threading
from socket import *

from test_python_client import connect, disconnect, send

HOST = ''
PORT = 50007
TMP_PORT = 123


def message_receive_callback_function(data, address):
    while True:
        if data:
            data_as_stirng = data.decode()
            print('Received data: {}'.format(data_as_stirng))
            socket_object = connect(address[0], TMP_PORT)
            send(socket_object, message=data_as_stirng)
            disconnect(socket_object)


def dispatch_clients():
    socket_object = socket(AF_INET, SOCK_DGRAM)
    socket_object.bind((HOST, PORT))
    print('Server listening on host: {}, and port: {}'.format(HOST, PORT))
    while True:
        data, address = socket_object.recvfrom(1024)
        if address:
            print('Server connected by {} at {}'.format(
                address, datetime.datetime.now())
            )
            thread = threading.Thread(
                target=message_receive_callback_function, args=(data, address, )
            )
            thread.start()


if __name__ == '__main__':
    try:
        dispatch_clients()
    except KeyboardInterrupt:
        print('Server is out!')
        exit(0)
