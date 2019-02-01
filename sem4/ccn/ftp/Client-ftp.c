// Client side C/C++ program to demonstrate Socket programming 
#include <stdio.h> 
#include <sys/socket.h> 
#include <stdlib.h> 
#include <netinet/in.h> 
#include <string.h> 
#define PORT 9001

int main(int argc, char const *argv[]) 
{ 
	struct sockaddr_in address; 
	int sock = 0, valread; 
	struct sockaddr_in serv_addr; 
	char *hello = "Hello from client\n";
	char message[100]; 
	char buffer[100000] = {0}; 
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
	{ 
		printf("\n Socket creation error \n"); 
		return -1; 
	} 

	memset(&serv_addr, '0', sizeof(serv_addr)); 

	serv_addr.sin_family = AF_INET; 
	serv_addr.sin_port = htons(PORT); 
	
	// Convert IPv4 and IPv6 addresses from text to binary form 
	if(inet_pton(AF_INET, "10.100.54.192", &serv_addr.sin_addr)<=0) 
	{ 
		printf("\nInvalid address/ Address not supported \n"); 
		return -1; 
	} 

	if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
	{ 
		printf("\nConnection Failed \n"); 
		return -1; 
	}
	printf("Enter File to be opened : ");
	gets(message);
	//send(sock , hello , strlen(hello) , 0 );
	//send(sock , "\n" , 2 , 0 );
	send(sock , message , strlen(message) , 0 ); 
	printf("File %s is displayed : \n\n\n",message); 
	valread = read( sock , buffer, 1000000); 
	int p = printf("%s\n",buffer ); 
	FILE *fp = fopen(message, "w");
	fwrite(&buffer, p,1, fp);
	fclose(fp);

	return 0; 
} 
