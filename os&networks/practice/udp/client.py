import socket
host='127.0.0.1'
port=8081

conn=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
conn.sendto(input('').encode(),(host,port))
data=conn.recvfrom(2048)
print(f'message {data[0].decode()}')