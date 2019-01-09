#!/bin/bash

s=$(echo "scale=1; $1 * $2" | bc)
echo "Area of rectangle of sides $1, $2 = $s"	