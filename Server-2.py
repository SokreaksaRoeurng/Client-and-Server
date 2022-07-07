import socket 
from datetime import datetime

HOST = "0.0.0.0"
PORT = 6789
max_size = 1024

print("Starting The Client At: ", datetime.now())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    message_to_server = input("Enter Message To Server: ")
    message_to_encoded = message_to_server.encode('utf-8')
    s.send("message_to_server_encoded")
    if message_to_server == 'q':
        break
    data = s.recv(max_size)
    if data.decode('utf-8')== 'q':
        break
    print("At", datetime.now(), "server replied with", data.decode('utf-8'))

s.close()