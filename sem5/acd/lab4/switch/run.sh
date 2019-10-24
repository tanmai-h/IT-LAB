flex -l $1.l
yacc $1.y
gcc y.tab.c -ll -ly

./a.out