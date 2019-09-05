%{ 
    #include <stdio.h>
    int s = 0, m = 0 , i = 0;
%}

%%

"/*"[^\n]+"*/" {
    printf("%s\n", yytext);
    fprintf(yyout, "%s", " ");
    s++;
}

\/\/(.*) {
    printf("%s\n", yytext);
    fprintf(yyout, "%s", " ");
    s++;
}

"/*"([^*]|\*+[^*/])*\*+"/" { 
    printf("%s\n", yytext);
    fprintf(yyout, "%s", " ");
    m++;
}

"int "[a-zA-Z_][a-zA-Z_]*"" {
    if(strcmp("int main", yytext) != 0) {
        i++;
        printf("%s\n", yytext);     
    }
    fprintf(yyout, "%s", yytext);
}

<*>.|\n {
    fprintf(yyout, "%s", yytext);
}

%%

int main(int argc[],char **argv[]) {
    yyin = fopen("code.c","r");
    yyout = fopen("newcode.c", "w");

    yylex(); 
    
    printf("\nsingle: %d\n", s);
    printf("multi: %d\n", m);
    printf("identifiers: %d\n", i);
    fclose(yyout);

    return 0; 
}