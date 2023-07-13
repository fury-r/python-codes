import socket

host='127.0.0.1'
port=8080

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,port))
while True:
    conn.sendall(input('Enter something ').encode())
    data=conn.recv(2048)

    print(f'Recieved {data.decode()}')
    if (input('press x to exit and enter to continue ')=='x'):
        break