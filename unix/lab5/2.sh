echo Enter db name
read name
echo Enter your choice
echo "1. enter (id,name,sem,m1,m2,m3)"
echo "2.delete"
echo "3.find by id"
echo "4.exit"
read ch

case $ch in
  1) echo enter id,name,sem,m1,m2,m3
     read id
     read n
     read sem
     read m0
     read m1
     read m2
     echo "$id | $n | $sem | $m0 | $m1 | $m2" >> $name
  ;;
  2) echo Enter  id to del
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
