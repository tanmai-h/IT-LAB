#!/bin/bash

echo "Enter n"
read n
s=$(echo "scale=0;$n*($n+1)/2" | bc)
echo "Sum of numbers 1 to n = $s"