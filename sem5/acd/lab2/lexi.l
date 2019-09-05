%{ 
    #include <stdio.h>
    
%}
identifier [a-zA-Z][a-zA-Z0-9]*

%%
int" "|float" "|double" "|char" "|main" " {
    printf("%s - keyword\n", yytext);
}
"int "[a-zA-Z_][a-zA-Z_]*; {
    for(int i = 4; yytext[i]!='\n'; i++) printf("%c",yytext[i]);
    printf(" - identifier"); 
    printf("\n");
}
"double "[a-zA-Z_][a-zA-Z_]*; {
    for(int i = 7; yytext[i]!='\n'; i++) printf("%c",yytext[i]);
    printf(" - identifier"); 
    printf("\n");
    
}
"float "[a-zA-Z_][a-zA-Z_]*; {
    for(int i = 6; yytext[i]!='\n'; i++) printf("%c",yytext[i]);
    printf(" - identifier");
    printf("\n");
}
#.* {
    printf("%s - preprocessor\n", yytext);
}

"/+|*|%|-|/|/" {
    printf("%s - operator\n", yytext);
}

"/*"[^\n]+"*/"|\/\/(.*) {
    printf("%s - single line comment\n", yytext);
}

"/*"([^*]|\*+[^*/])*\*+"/" {
    printf("%s - multi line comment\n", yytext);
}

[0-9]+ {
    printf("%s - int literal\n", yytext);
}

[0-9]+"."[0-9]+ {
    printf("%s - floating literal\n", yytext);
}

{identifier}[0-9_]+ {
    printf("%s - identifier\n",yytext);
}

<*>.|\n {
    continue;
}
%%

int main() {
    yyin = fopen("ip.txt", "r");
    yylex(); 
    
    return 0; 
}