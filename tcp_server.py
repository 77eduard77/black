import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#--1---binding connecteion to server.To start off, we pass in the IP address and port we want the server to listen on
server.bind((bind_ip, bind_port))

#--2--Next we tell the server to start listening v with a maximum backlog of connections set to 5.
server.listen(5)
 print "[*] Listening on %s:%d" % (bind_ip,bind_port)

 #this is our client-handling thread
 #--3--- The handle_client  function performs the recv() and then sends a simple message back to the client
 def handle_client(client_socket):
     #print out what the client sends
     request = client_socket.recv(1024)

     print "[*] Recieved: %s"% request

     #sends a packet back
     client_socket.send("ACK!")

     client_socket.close()

while True:
    #---4--When a client connects ,
#we receive the client socket into the client variable, and the remote connection details into the addr variable. We then create a new thread object that
#points to our handle_client function, and we pass it the client socket object as an argument

    client, addr = server.accept()

    print "[*] Accepted connection From:%s:%d"% (addr[0],addr[1])

    #spin up our client thread to handle incoming data

#--5--We then start the thread to handle the client connection ,and our main server loop is ready to handle another incoming connection
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

    
'''----------------------------------------------------------------------------
import socket
import threading

BIND_IP = '0.0.0.0'
BIND_PORT = 9090

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] Received: " + request
    client_socket.send('ACK')
    client_socket.close()

def tcp_server():
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    server.bind(( BIND_IP, BIND_PORT))
    server.listen(5)
    print"[*] Listening on %s:%d" % (BIND_IP, BIND_PORT)

    while 1:
        client, addr = server.accept()
        print "[*] Accepted connection from: %s:%d" %(addr[0], addr[1])
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    tcp_server()
'''----------------------------------------------------------------------------
