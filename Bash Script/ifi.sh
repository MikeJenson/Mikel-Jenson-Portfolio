#!/bin/bash

echo -n "word 1: "
read word1

echo "word 2: "
read word2

if test "$word1" = "word2"
	then
	echo "match"
else
	echo "these do not match"
fi
echo "end of program."