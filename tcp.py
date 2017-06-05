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
