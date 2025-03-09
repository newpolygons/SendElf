# send .elf to ps5
import sys
import os
import socket


#ps5 ip
host = ''
#ps5 port
port = 0
#filepath relavtive to where script is being called
filename = ''


argumentList = sys.argv[1:]
for i in argumentList:
    if i == '-nc':
        os.system('nc {} {} < {}'.format(host, port, filename))
        exit()




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
fi = open(filename, 'rb')
sock.sendfile(fi)

fi.close()
sock.close()


