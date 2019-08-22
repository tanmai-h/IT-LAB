%{ 
    #include<stdio.h>
    int k = 0;
    char s[100], rev[100];
%}

%%
[a-zA-Z]+ {
    if(yyleng > k) {  
        k = yyleng;
        strcpy(s,yytext);
    }
}
%%

int main(int argc[],char **argv[]) {
    yyin = fopen("abc.txt","r");
    yylex(); 
    printf("largest: %d - %s\n",k, s);
    int n = strlen(s);
    for(int i = n-1; i >= 0; i--) 
        rev[i] = s[n-i-1];
    rev[n] = '\0';
    
    printf("\n%s\n", rev);

    return 0; 
}