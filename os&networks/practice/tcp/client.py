import socket

host,port='127.0.0.1',8081
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,port))
conn.send(input('|').encode())
print(conn.recv(1024).decode())
