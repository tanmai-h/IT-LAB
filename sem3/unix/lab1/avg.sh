#!/bin/bash

echo "enter size , n"
read n
s=0
for((i=0;i<n;i++))
do
	read x
	s=`expr $x + $s`
done
avg=`echo "$s / $n" | bc -l`
echo "avg of list = $avg"