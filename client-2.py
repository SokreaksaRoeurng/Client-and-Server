import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50005
sock.connection(('0.0.0.0', port))
msg = sock.recv(1024)
# msg 
#b'Hello, Thank For Connecting!
msg_decoded = msg.decode('utf-8')
#msg_decoded 
#'Hello. Thank For Connecting!
print('Message from server: '+ msg_decoded)
msg_back = input('Do You Want To Respone To The Server?')
msg_back_encoded = msg_back.encode('utf-8')
sock.send(msg_back_encoded)

sock.send(msg_back_encoded)
