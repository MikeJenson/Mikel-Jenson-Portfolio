#!bin/bash
# Mikel Jenson / 8/9/2017
# This program is designed to make a backup copy of a specified file then open the original file in VIM if it exists

if test $# = 1 #This line takes what is typed in after the file is executed and puts it in parameter '1'
	then
	cp $1 $HOME/keep 
	vi $1
else
	echo "file not found. Please try again"
fi
else
	echo "you must specify a file name. Please try agian"
fi