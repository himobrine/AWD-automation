import socket

HOST = '192.168.21.1'
PORT = 2022
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print('等待客户端连接...')

client_socket, addr = server_socket.accept()
print('客户端已连接：', addr)

data = client_socket.recv(1024)
print('接收到数据：', data.decode())
client_socket.sendall(data)
client_socket.close()
server_socket.close()