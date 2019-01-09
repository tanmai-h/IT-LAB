#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main() {	   
    pid_t id;
    id=fork();
    if(id==0)
        printf("i am child process: %d\n", id);
    else if(id>0)
        printf("i am a parent process: %d\n", id);
    else
        printf("fork() has failed\n");
    
    id=fork();
    //id=fork();
    if(id==0)
        printf("i am child process: %d\n", id);
    else if(id>0)
        printf("i am a parent process: %d\n", id);
    else
        printf("fork() has failed\n");

    return 0;
}