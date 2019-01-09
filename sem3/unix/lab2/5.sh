#!/bin/bash

t=1

while (($t <= 999))
do
	z=$t
	s=0
	while((z>0))
	do
		x=$(($z%10))
		s=$(($s+$x*$x*$x))
		z=$(($z/10))
	done
	if [ "$s" -eq "$t" ]
		then
		echo $t
	fi
	t=$(($t+1))
done