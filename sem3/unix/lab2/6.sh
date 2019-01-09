#!/bin/bash
echo -n "Num files: "&& ls | wc -l
ls -l
echo "Files Count : $(find $1 -maxdepth 1 -type f | wc -l)"
echo "Directory Count : $(find $1 -maxdepth 1 -type d | wc -l)"
