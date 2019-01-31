import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 9999))
print("9999 port has been bind")
while True:
    data,adr = s.recvfrom(1024)
    print("recieved data from %s:%s" % adr)
    s.sendto(b'hello %s' % data, adr)