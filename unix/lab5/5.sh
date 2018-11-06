sed '1,3 s/|/:/g' tester.txt > $$
mv $$ tester.txt
sed '1i\<HTML>' tester.txt > $$
mv $$ tester.txt
sed '$a\</\HTML>' tester.txt > $$
mv $$ tester.txt
