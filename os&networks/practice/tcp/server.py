import socket

host='127.0.0.1'
port=8081
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.bind((host,port))
conn.listen()
print('Running')
conn,addr=conn.accept()
print(f"Connected: {addr}")
print(conn.recv(1024).decode())
conn.send('okay'.encode())
conn.close()