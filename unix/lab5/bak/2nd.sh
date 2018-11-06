echo Enter filename
read name
echo Enter your choice
read ch

case $ch in
  1) echo Details
     read id
     read n
     read sem
     read m0
     read m1
     read m2
     echo $id | $n | $sem | $m0 | $m1 | $m2 >> $name
  ;;
  2) echo Enter the id to delete
     read id
     grep -v $id $name > $$
     mv $$ $name
     cat $name
  ;;
  3) echo Enter the id to find
     read id
     grep "$id" $name
  ;;
  *) exit
  ;;
esac
