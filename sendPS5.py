# send .elf to ps5

import socket

#ps5 ip
host = ''
#ps5 port
port = 
#filepath
filename = ''


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


fi = open(filename, 'rb')

sock.sendfile(fi)

fi.close()
sock.close()
