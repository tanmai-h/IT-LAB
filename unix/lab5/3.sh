echo "files that start with a vowel : "

ls -F | grep -v / | grep ^[aeiouAEIOU]
echo ""
echo "No. of blank lines in c.txt : "

grep -c "^$" c.txt