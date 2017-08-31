#!/bin/bash

secretname = jenny

name = noname

echo "try to guess the secret name!"
echo
until ["$name" = "$secretname"]
	do
		echo -n "Your guess: "
		read name
done