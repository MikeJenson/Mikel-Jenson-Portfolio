#!/bin/bash

alpha = "A B C D E F"
count = 0

for letter in alpha
	do
		count = expr $count + 1
		echo "Letter $count is [$alpha]"
done