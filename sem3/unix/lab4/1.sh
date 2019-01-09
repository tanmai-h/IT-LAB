#!/bin/bash

if [ $# -eq 0 ]; then
    echo "give filename"
else
    od -b $1
fi