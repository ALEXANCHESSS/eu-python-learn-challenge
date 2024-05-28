import socket
import sys
import threading

HOST = "127.0.0.1"
PORT = 12345

lock = threading.Lock()


def connection_wrapper(connection: socket.socket, name_user: str) -> None:
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break

            sys.stdout.write('\r' + ' ' * len(name_user) + '\r')
            print(data.decode('utf-8'))
            sys.stdout.write(f'{name_user}: ')
            sys.stdout.flush()
        except ConnectionResetError as e:
            print(f'Connection error: {e}')
            break


def writer(connection: socket.socket, name_user: str) -> None:
    while True:
        data = input(f'{name_user}: ')
        if data == ':q':
            print("Logging out of the chat room")
            connection.close()
            break

        message = f"{name_user}: {data}"
        connection.sendall(message.encode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    name_user = input("Enter your name: ")
    s.connect((HOST, PORT))

    connection_thread = threading.Thread(target=connection_wrapper, args=(s, name_user))
    connection_thread.start()

    writing_thread = threading.Thread(target=writer, args=(s, name_user))
    writing_thread.start()

    connection_thread.join()
