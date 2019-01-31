import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
name_dict = [b'caoxiang',b'liulin',b'ganggang']
for x in name_dict:
    s.sendto(x,("127.0.0.1",9999))
    print(s.recv(1024).decode('utf-8'))
s.close()