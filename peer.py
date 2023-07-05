import socket
import threading


class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

    def connect(self, peer_host, peer_port):
        try:
            self.socket.connect((peer_host, peer_port))
            self.connections.append(self.socket)
            print(f"Connected to {peer_host}:{peer_port}")
        except socket.error as e:
            print(f"Failed to connect to {peer_host}:{peer_port}. Error: {e}")

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f"Listening for connections on {self.host}:{self.port}")

        receive_thread = threading.Thread(target=self.receive_data)
        receive_thread.start()

    def send_data(self, data):
        for connection in self.connections:
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f"Failed to send data. Error: {e}")

    def start(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()

    def receive_data(self):
        connection, address = self.socket.accept()
        self.connections.append(connection)
        print(f"Accepted connection from {address}")
        while True:
            data = connection.recv(1024).decode()
            print(f"Received data: {data}")
