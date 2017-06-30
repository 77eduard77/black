#Author - Tikam Alma
#Date - 28-June-2017

import sys,socket,getopt,threading,subprocess,argparse

#globals used for options
listen=False
command=False
upload=None
execute=None
target=None
upload_destination=None
port=None

def main():
    global target
    global port
    global listen
    global execute
    global command
    global upload_destination

    #set-up argument parsing
    parser = argparse.ArgumentParser(description="Simple Netcat-Programm")
    parser.add_argument("port",type=int,help="target port")
    parser.add_argument("-t","--target_host",type=str,help="target host",default="0.0.0.0")
    parser.add_argument("-l","--listen",help="listen on [host]:[port] for incomming connections",action="store_true",default=False)
    parser.add_argument("-e","--execute",help="--execute=file_to_run execute the given file upon recieving a connection")
    parser.add_argument("-c","--command",help="intialize a command shell",action="store_true",default=False)
    parser.add_argument("-u","--upload",help="--upload=destination upon recieving connection upload a file and write to [destination]")
    args=parser.parse_args()

    #parse ArgumentParser
