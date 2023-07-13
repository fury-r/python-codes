
import socket
host='127.0.0.1'
port=8081

conn=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
conn.bind((host,port))
data=conn.recvfrom(2048)
print(f'Connected by {data[1]} \nMessage:{data[0].decode()}')
conn.sendto('okay'.encode(),data[1])
conn.close()