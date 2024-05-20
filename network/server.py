import socket
import threading

HOST = "127.0.0.1"
PORT = 12345
clients = set()
lock = threading.Lock()


def new_client(connection: socket.socket, addr) -> None:
    with connection:
        with lock:
            clients.add(connection)
        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"|{data.decode('utf-8')}| from {addr}")
                with lock:
                    for client in clients:
                        if client != connection:
                            client.sendall(data)
            with lock:
                clients.remove(connection)

        except ConnectionResetError:
            print('Connection error')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        connection_thread = threading.Thread(target=new_client, args=(conn, addr))
        connection_thread.start()
