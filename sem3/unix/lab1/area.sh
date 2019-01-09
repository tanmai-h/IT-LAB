#!/bin/bash

echo "enter circle radius: "
read r

a=$(echo "scale=2;3.14159 * ($r * $r)" | bc)
echo "Area = $a"