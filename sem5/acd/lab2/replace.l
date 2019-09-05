%{ 
    #include <stdio.h>
    char replace[100], replace_with[100];

%}

%%
[a-zA-Z]+ { 
    if(strcmp(yytext, replace)==0) 
        fprintf(yyout, "%s", replace_with); 
    else
        fprintf(yyout, "%s", yytext);} 
. {
    fprintf(yyout, "%s", yytext); 
}
%%

int main() {
    printf("word to replace: "); 
    scanf("%s", replace); 
    printf("replce with: ");
    scanf("%s",replace_with);
    
    yylex(); 
    
    return 0; 
}