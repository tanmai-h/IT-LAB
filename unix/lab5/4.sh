echo "file:"
cat html

echo
echo "tags...."
sed -i '1 i <HTML>' html
sed -i '$ a </HTML>' html
echo
echo "file:"
cat html

#-------------------------
echo "replace (|)with(:)  in 1st 3 lines..."
cat abc
sed  -i '1,3 s/|/:/g' abc
cat abc