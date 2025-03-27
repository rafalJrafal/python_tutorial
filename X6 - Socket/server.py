import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5903

print(host)

server_socket = socket.socket()

server_socket.bind((host, port))

server_socket.listen(2)

connection, address = server_socket.accept()
print("connection from", str(address))

while(True):
    data = connection.recv(8).decode()
    print(data)