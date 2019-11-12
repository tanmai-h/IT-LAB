lex subc-compiler.l
yacc subc-compiler.y
gcc -w y.tab.c -ll -ly

