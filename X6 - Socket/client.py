import socket

host = socket.gethostname()
port = 5903

client_socket = socket.socket()
client_socket.connect((host, port))

while (True):
    print("type input")
    str = input()
    client_socket.send(str.encode())
