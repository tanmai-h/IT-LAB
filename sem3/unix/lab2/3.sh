#!/bin/bash
echo "enter 5 num"
ar=()
t=0
for((i=0;i<5;i++))
do
	read t
	ar[`expr $i`]=$t
done
m=${ar[0]}
M=${ar[0]}
f=0
for((i=1;i<5;i++))
do
	if(($m > ${ar[`expr $i`]}))
	then
		m=${ar[`expr $i`]}
	fi
	if(($M < ${ar[`expr $i`]}))
	then
		M=${ar[`expr $i`]}
	fi
done

a=0
b=0
for((i=0;i<5;i++))
do
	if(($M == ${ar[`expr $i`]}))
		then
		a=$((a+1))
	fi
	if(($m == ${ar[`expr $i`]}))
		then
		b=$((b+1))
	fi
done
echo "max: " $M " occurs " $a " time(s)"
echo "min: " $m " occurs " $b " time(s)"
