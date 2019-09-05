%{ 
    #include <stdio.h>
    int simple = 1;
%}

%%
"and"|"or"|"And"|"Or" {
    simple = 0;
    return -1;
}

<*>.|\n {
    continue;
}
%%

int main() {
    yylex(); 
    if(simple) {
       printf("Simple sentence\n");
    }
    else
        printf("Complex sentence\n");
    return 0; 
}