A TCP Proxy

A TCP proxy can be very useful for forwarding traffic and when assessing network-based softwares (for example, when you cannot run Wireshark or you cannot load drivers or tools in the machine you are exploiting).

To create a proxy we need to verify if we need to first initiate a connection to the remote side.
This will request data before going into our main loop and some server daemons expect you to do this first (for instance, FTP servers send a banner first). We call this information receive_first.


################################################################################
The Main Function

So let us start with our main function. First we define the usage, which should have four more arguments together with receive_first. Then we check these arguments to variables and start a listening socket:

import socket
import threading
import sys

def main():
    if len(sys.argv[1:]) != 5:
        print "Usage: ./proxy.py <localhost> <localport> <remotehost> <remoteport> <receive_first>"
        print "Example: ./proxy.py 127.0.0.1 9000 10.12.122.1 9999 True"
        sys.exit()

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    if sys.argv[5] == 'True':
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

##################################################################################
    The Server Loop Function

    Like before we start creating a socket and binding this to a port and a host. Then we start a loop that accepts incoming connections and spawns a thread to the new connection:

    def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server.bind(( local_host, local_port))
        except:
            print "[!!] Failed to listen on %s:%d" % (local_host, local_port)
            sys.exit()

        print "[*] Listening on %s:%d" % (local_host, local_port)
        server.listen(5)

        while 1:
            client_socket, addr = server.accept()
            print "[==>] Received incoming connection from %s:%d" %(addr[0], addr[1])

            # start a thread to talk to the remote host
            proxy = threading.Thread(target=proxy_handler, \
                args=(client_socket, remote_host, remote_port, receive_first))
            proxy.start()

###############################################################################
The Proxy Handler Functions

In the last two lines of the above snippet, the program spawns a thread for the function proxy_handler which we show below. This function creates a TCP socket and connects to the remote host and port. It then checks for the receive_first parameter. Finally, it goes to a loop where it:

    reads from local host (with the function receive_from),
    processes (with the function hexdump),
    sends to remote host (with the function response_handler and send),
    reads from remote host (with the function receive_from),
    processes (with the function hexdump), and
    sends to local host (with the function response_handler and send).


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(( remote_host, remote_port ))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        remote_buffer = response_handler(remote_buffer)

        # if we have data to send to client, send it:
        if len(remote_buffer):
            print "[<==] Sending %d bytes to localhost." %len(remote_buffer)
            client_socket.send(remote_buffer)

    while 1:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print "[==>] Received %d bytes from localhost." % len(local_buffer)
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print "[==>] Sent to remote."

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print "[==>] Received %d bytes from remote." % len(remote_buffer)
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print "[==>] Sent to localhost."

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print "[*] No more data. Closing connections"
            break

#################################################################################

The receive_from function takes a socket object and performs the receive, dumping the contents of the packet:

def receive_from(connection):
    buffer = ''
    connection.settimeout(2)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer

################################################################################

The response_handler function is used to modify the packet contents from the inbound traffic (for example, to perform fuzzing, test for authentication, etc). The function request_handler does the same for outbound traffic:

def request_handler(buffer):
    # perform packet modifications
    buffer += ' Yaeah!'
    return buffer

def response_handler(buffer):
    # perform packet modifications
    return buffer

###################################################################################

Finally, the function hexdump outputs the packet details with hexadecimal and ASCII characters:

def hexdump(src, length=16):
    result = []
    digists = 4 if isinstance(src, unicode) else 2
    for i in range(len(src), lenght):
        s = src[i:i+length]
        hexa = b' '.join(['%0*X' % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append(b"%04X %-*s %s" % (i, length*(digits + 1), hexa, text))

Firing Up our Proxy

Now we just need to run our script with some server. For example, for a FTP server at the standard port 21:

$ sudo ./tcp_proxy.py localhost 21 ftp.target 21 True
[*] Listening on localhost:21
(...)
