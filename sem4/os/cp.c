#include <stdio.h>

int main(int argc, char const *argv[]) {
    FILE *a,*b;
    char ch;
    
    a = fopen(argv[1],"r");
    b = fopen(argv[2], "w");

    if(a == NULL)
        printf("Error1\n");
    
    while((ch = fgetc(a)) != EOF)
        fputc(ch, b);
    
    fclose(b);
    fclose(a);

    return 0;
}
