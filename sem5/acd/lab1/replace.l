%{ 
    #include<stdio.h>
%}

%%
[a-zA-Z] {
    char s = yytext[0];
    int i = s;
    if(s <= 'z' && s >= 'a') {
        i -= 'a'; i = (i+5)%26;
        i += 'a';
        printf("%c", (char)i);
    }    
    else if(i <= 'Z' && i >= 'A'){
        i -= 'A'; i = (i+5)%26;
        i += 'A';
        printf("%c", (char)i);
    }
    else {
        ECHO;
    }
   
}
[^a-zA-Z] {
    ECHO;
}
%%

int main(int argc[],char **argv[]) {
    yyin = fopen("code.c","r");
    yylex(); 
    

    return 0; 
}