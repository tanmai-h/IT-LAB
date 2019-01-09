#!/bin/bash
echo "Entrer basic salary"
read b
dp=`expr $b/2`
b=`expr $b+$dp`
fin=$(echo "scale=2;$b *(1+0.35 + 0.08 + 0.03 - 0.1)"  | bc)
echo "final salary = $fin"
