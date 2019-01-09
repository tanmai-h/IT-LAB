#!/bin/bash
echo enter decimal number: ”
read dec
echo "decimal to bin"
echo "obase=2; ${dec}" | bc
echo enter binary number: ”
read a
echo "bin to dec"
echo "ibase=2; ${a}" | bc
echo enter binary number: ”
read d
echo "bin to hexa"
echo "obase=16;ibase=2; ${d}" | bc
echo enter hex number: ”
read c
echo "hexa to decimal"
echo "ibase=16; ${c}" | bc

