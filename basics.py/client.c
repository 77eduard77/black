#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<sys/fcntl.h>
#include<arpa/inet.h>
int main(int argc,char *argv[])
{
  fprintf(stderr, "usage a/os serverip filename port\n",argv[0] );

}
 serverip=argv[1];
 portno=atoi(argv[3]);
 sockfd=socket(AF_INET,SOCK_STREAM,0);
 if(sockfd<0)
 perror("error opening socket");
 printf("client online\n");
 bzero((char *)&serv_addr,sizeof(serv_addr));
 serv_addr.sin_family=AF_INET;
 serv_addr.sin_addr.s_addr=inet_addr(servip);
 serv_addr.sin_port=htons(portno);
 if(connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr))<0)
 perror("error connecting");
 write(sockfd,argv[2],strlen(argv[2])+1);
 bzero(buffer,4096);
 n=read(sockfd,buffer,4096);
 if(n<=0)
 {
   perror("file not found");
   exit(0);
 }
 write(1,buffer,n);
 }
