#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int sockfd;
    struct sockaddr_in server , client;
    int portno=8080,num_conections=5,n;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd < 0) {
        printf("Error opening socket");
        return EXIT_FAILURE;
    }

    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_family = AF_INET;
    server.sin_port = htons(portno);

    n = bind(sockfd,(struct sockaddr *) &server,len(server));
    if(n < 0) {
        printf("Cant bind socket");
        return EXIT_FAILURE;
    }
    if(listen(sockfd, num_conections)) {
        printf("cant listen");
        return EXIT_FAILURE;
    }
    
    int newsockfd = accept(socket, (struct sockadd *) &client, sizeof(client));
    if(newsockfd < 0) {
        printf("cant accept");
        return EXIT_FAILURE;
    }

    char buffer[256];
    n = read(newsockfd, buffer, sizeof(buffer));
    if(n < 0) {
        printf("cant read"); 
        return EXIT_FAILURE;
    }
    
    char msg = "gotit";
    n = write(newsockfd, msg, sizeof(msg));
    if(n < 0) {
        printf("cant write");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}