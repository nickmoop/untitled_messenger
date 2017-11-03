import threading
from socket import *


SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 50007
TMP_PORT = 123


def receive(socket_object):
    while True:
        data = socket_object.recv(1024)
        if data:
            print('Received: {}'.format(data.decode()))


def send(socket_object, message=None):
    if message:
        print('Encode message: {}'.format(message))
        message = [message.encode()]
        print('Send message')
        for line in message:
            socket_object.send(line)
    else:
        print('Empty message')


def connect(hostname, port):
    socket_object = socket(AF_INET, SOCK_DGRAM)
    socket_object.connect((hostname, port))

    print('Connected to socket with host: {}, and port: {}'.format(
        hostname, port)
    )

    return socket_object


def disconnect(socket_object):
    print('Disconnect from socket')
    socket_object.close()


if __name__ == '__main__':
    import sys

    message_to_send = 'Test message for send to server'

    if len(sys.argv) >= 2:
        message_to_send = ' '.join(sys.argv[1:])

    test_receiving_socket = connect(SERVER_HOSTNAME, TMP_PORT)
    receiving_thread = threading.Thread(
        target=receive, args=(test_receiving_socket, ))
    receiving_thread.start()

    test_socket = connect(SERVER_HOSTNAME, SERVER_PORT)
    send(test_socket, message=message_to_send)
    disconnect(test_socket)
