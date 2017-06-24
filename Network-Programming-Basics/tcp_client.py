#Auther- Tikam Alma
#Python Socket-Programming---[tcp-client]
import socket

target_host = "www.google.com"
target_port = 80

#1-create a socket object
client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#-2-Connect the client
client.connect((target_host,target_port))

#-3-send some data
client.send("GET/HTTP/1.1\r\nHOST:google.com\r\n\r\n")

#-4-recieve data
response = client.recv(4096)

print response

'''-----------------------------------------------------------------------------

import socket

HOST = 'www.google.com'
PORT = 80
DATA = 'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'

def tcp_client():
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect(( HOST, PORT ))
    client.send(DATA)
    response = client.recv(4096)
    print response

if __name__ == '__main__':
    tcp_client()
'''--------------------------------------------------------------------------
