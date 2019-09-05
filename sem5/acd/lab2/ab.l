%{ 
    #include <stdio.h>
    int c = 0;
%}

%%
[a-zA-Z0-9]*ab[ \n\r] {
    c++;
}

<*>.|\n {
    continue;
}
%%

int main() {
    yylex(); 
    printf("Num words edning with ab: %d\n",c);
    return 0; 
}