#!/bin/bash
if [ $# -lt 2 ];then
	echo "need args!"
else
	if [ "$1" -le "0" ] || [ "$2" -le "0" ]
	then
		echo "need +ve Whole numbers"
	else
		if (($1>$2)); then
			e=$(echo "scale=2; $2 / $1 " | bc)
			echo "$2/$1" = $e
		else
			e=$(echo "scale=2; $1 / $2 " | bc)
			echo "$1/$2" = $e
		fi
	fi
fi