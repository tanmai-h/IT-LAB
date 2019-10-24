flex -l $1.l
yacc -vd $1.y
gcc lex.yy.c y.tab.c -lm -ll

./a.out