#!/bin/bash

read -p "enter marks of Unix - " UNIX
read -p "enter marks of  Java - " JAVA
read -p "enter marks of DS - " DASA

sum=` expr $UNIX+$JAVA+$DASA `
#AVG=$((echo "$(($sum)) / 3.0" | bc))
#AVG=$(echo "scale=2; ($sum / 3)" | bc)
#echo $AVG
AVG=$(($sum/3))
if [ $AVG -ge 70 ];then
	echo "Distinction"
elif [ $AVG -ge 60 ];then
	echo "First class"
elif [ $AVG -ge 50 ];then
	echo "Second class"
elif [ $AVG -ge 40 ];then
	echo "Third class"
else
	echo "Failed"
fi
