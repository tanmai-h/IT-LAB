#!/bin/bash
echo 'Enter Amount, Time, rate in %'
read p t r

si=` expr $p \* $t \* $r / 100 `
echo "Simple interst:  $si"