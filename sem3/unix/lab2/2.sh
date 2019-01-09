#!/bin/bash
pwd
whoami
d=`date +%m-%d-%Y`
echo "Today is: " $d
u=`users | wc -w`
t=`tty`
echo "Num users loggd in: " $u
echo "Terminak: "$t
