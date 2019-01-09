# !/bin/bash
 
echo "Enter 2 nums : "
read a b
 
echo "Enter option :"
echo "+ Add"
echo "- Substrct"
echo "* Multiply"
echo "/ Div"
read ch

case $ch in
	+)res=`echo $a + $b | bc`
	;;
	-)res=`echo $a - $b | bc`
	;;
	/)res=`echo "scale=2; $a / $b" | bc`
	;;
	*)res=`echo $a \* $b | bc`
	;;
esac

echo "$a $ch $b = $res"

