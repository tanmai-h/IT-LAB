#!/bin/bash
p=0
z=0
n=0

t=10

for((i=0;i<10;i++))
do
	read t
	echo $t >> test
	if [ "$t" -gt "0" ]; then
		p=$(echo "$p+1" | bc)
	elif [ "$t" -lt "0" ];	then
		n=$(echo "$n+1" | bc)
	else
		z=$(echo "$z+1" | bc)
	fi 
done

echo "+ve, -ve, zeroes: " $p, $n, $z
echo `sort -n test`