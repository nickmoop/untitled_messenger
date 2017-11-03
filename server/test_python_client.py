from socket import *

SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 50007


def send(socket_object, message=None):
    if message:
        print('Encode message: {}'.format(message))
        message = [message.encode()]
        print('Send message')
        for line in message:
            socket_object.send(line)
    else:
        print('Empty message')


def connect():
    socket_object = socket(AF_INET, SOCK_STREAM)
    socket_object.connect((SERVER_HOSTNAME, SERVER_PORT))

    print('Connected to socket with host: {}, and port: {}'.format(
        SERVER_HOSTNAME, SERVER_PORT)
    )

    return socket_object


def disconnect(socket_object):
    print('Disconnect from socket')
    socket_object.close()


if __name__ == '__main__':
    import sys
    import time

    message_to_send = 'Test message for send to server'
    if len(sys.argv) >= 2:
        message_to_send = ' '.join(sys.argv[1:])

    test_socket = connect()
    send(test_socket, message=message_to_send)
    time.sleep(3)
    send(test_socket, message='I will disconnect now')
    disconnect(test_socket)
