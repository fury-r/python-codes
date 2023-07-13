import socket

host='127.0.0.1'
port=8080
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.bind((host,port))
conn.listen()
con,addr=conn.accept()

while True:
    print('Connected by',addr)
    data=con.recv(2048)
    print(data.decode())
    con.sendall('No you are Not'.encode())
