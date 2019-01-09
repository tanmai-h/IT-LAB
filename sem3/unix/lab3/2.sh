#!/bin/bash
if [ $# -ne 2 ];then
	echo "Error, provide 2 files as arg"
else
	if [ -f $1 -a -f $2 ];then
		cat $1 >> $2
	else
		echo "files dont exist"
	fi
fi