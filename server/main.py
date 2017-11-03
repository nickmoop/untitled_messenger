import datetime
import threading
from socket import *


HOST = ''
PORT = 50007


def message_receive_callback_function(connection):
    while True:
        data = connection.recv(1024)
        if data:
            print(data)


def dispatch_clients():
    socket_object = socket(AF_INET, SOCK_STREAM)
    socket_object.bind((HOST, PORT))
    socket_object.listen(5)
    print('Server listening on host: {}, and port: {}'.format(HOST, PORT))
    while True:
        connection, address = socket_object.accept()

        print('Server connected by {} at {}'.format(
            address, datetime.datetime.now())
        )
        thread = threading.Thread(
            target=message_receive_callback_function, args=(connection,)
        )
        thread.start()


if __name__ == '__main__':
    try:
        dispatch_clients()
    except KeyboardInterrupt:
        print('Server is out!')
        exit(0)
