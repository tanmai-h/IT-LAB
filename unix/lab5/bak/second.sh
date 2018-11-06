ls | grep "^a"
ls | grep "^e"
ls | grep "^i"
ls | grep "^o"
ls | grep "^u"
ls | grep "^A"
ls | grep "^E"
ls | grep "^O"
ls | grep "^I"
ls | grep "^U"

echo "The file is:"
cat b.txt
echo "The no. of blank lines:"
grep -c "^$" b.txt
