import socket
import sys

s = socket.socket()
print('Socket Succussful create')
port = 56454

s.bind(('', port))
print(f'socket binded tto port{port}')

s.listen(5)
print('Socket is listening')

while True:
    c, addr = s.accept()
    print("Get connention From", addr)
    message = "Thank you for your Connection"
    c.send(message.encode())
    c.close()

