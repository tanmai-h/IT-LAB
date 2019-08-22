%{ 
    #include<stdio.h>
    int s = 0, p = 0;
%}

%%
[a-zA-Z]+ {
    if(strcmp(yytext, "scanf") == 0) {
        s++;
        printf("readf");
    }
    else if(strcmp(yytext, "printf") == 0) {
        printf("writef");
        p++;
    }
    else {
        ECHO;
    }
}
[^a-zA-Z]+ {
    ECHO;
}
%%

int main(int argc[],char **argv[]) {
    yyin = fopen("code.c","r");
    yylex(); 
    
    printf("\n\nscanfs: %d, printfs: %d\n", s, p);
    printf("\n");

    return 0; 
}