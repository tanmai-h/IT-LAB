#!/bin/bash

echo "matrix order"
read a
x=()
y=()
s=()

echo "first: "
for ((i=0; i<a; i++))
do
    for((j=0;j<a;j++))
    do
        read tmp
        n=$(($a*$i + $j))
        x[$n]=$tmp
    done
done

echo "second: "
for ((i=0; i<a; i++))
do
    for((j=0;j<a;j++))
    do
        read tmp
        n=$(($a*$i + $j))
        y[$n]=$tmp
    done
done

echo "1:  "
for ((i=0; i<a; i++))
do
    for((j=0;j<a;j++))
    do
        n=$(($a*$i + $j))
        printf ${x[$n]}
        printf " "
    done
    echo ""
done

echo ""
echo "2: "
for ((i=0; i<a; i++))
do
    for((j=0;j<a;j++))
    do
        n=$(($a*$i + $j))
        printf ${y[$n]}
        printf " "
    done
    echo ""
done

echo ""
echo "sum: "
for ((i=0; i<a; i++))
do
    for((j=0;j<a;j++))
    do
        n=$(($a*$i + $j))
        tmp=$((${x[$n]} + ${y[$n]}))
        s[$n]=$tmp
        printf ${s[$n]}
        printf " "
    done
    echo ""
done


