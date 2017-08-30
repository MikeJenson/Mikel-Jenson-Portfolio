#!/bin/bash/

# Mikel Jenson
# 8/18/2017
# This program is presented as a menu for a user to select from in order to run
# basic unix commands more easily
# CS140U Assignment 6

until [ "$answer" = "j" ] # This until loop will return the user to the commands menu unless they choose the "j" option to quit
	do
		clear # This will clear the screen before drawing the "Command Menu". This simply makes the menu look more clean and professional
echo -e "\n		Command Menu\n"
echo " a. Emailer Program"
echo " b. Users Currently Logged On"
echo " c. Current Date and Time"
echo " d. This months Calendar"
echo " e. name of the Working Directory"
echo " f. Contents of the Working Directory"
echo " g. Find the IP of a Web Address"
echo " h. See your Fortune"
echo " i. Print a file (on the screen)"
echo -e " j. Exit\n"
# All of the echo commands above simply print a string to the screen
read -p "Please enter a letter to select an option: " answer 
# This read command will print the question then look for what the user types and store this in the variable titled "answer"
echo 
case "$answer" in
# The case command will take the variable that we read earlier and apply it to the following cases	
	a|A) 
		clear
		echo -n "Please enter the subject of your email: "
		read subject
		echo -n "Please enter the email address: "
		read address
		echo -n "Please enter a file name to attach: "
		read attach
# These echo and read commands do the same as above but this time we are gathering 3 variables to plug into the below "mail" command
		mail -s "$subject" "$address"<"$attach"
# This mail command will take the 3 variables that we gathered above and send an email with those variables filled in
		echo
		read -n 1 -s -p "Press any key to continue"
# This read command will wait until a key is pressed and will accept any 1 key input 		
		clear
# I am running clear before and after each command in order to keep the page looking cleaner and making it easier to see what command what chosen
		;;
	b|B)
		clear
		who | more
# The who command is run with a pipe to more just in case there is more than one page of users online
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	c|C)
		clear
		echo -n "The current time and date is: "
		date
# The date command will print the current date and time to screen
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	d|D)
		clear
		echo " Here is your calendar for this month: "
		cal
# The cal command will print a calendar of the current month to the screen
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	e|E)
		clear
		echo "The current working directory is below: "
		pwd
# The pwd command will print the current working directory to the screen
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	f|F)
		clear
		ls | more
# The ls command will print the contents of the current folder to the screen this is piped to "more" just in case there is more than one page of files in the folder
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	g|G)
		clear
		echo -n "Please enter a web address whos IP you would like to see: "
		read ip 
# This echo and read command work as above but we are gathering the variable called ip that will be passed into the "host" command below
		host "$ip"
# This command will run an IP trace on the website that is received in the variable "ip" on the previous line
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	h|H)
		clear
		echo "This program will now show you a fortune: "
		fortune
# This is a built in command that will usually display a quote or remark
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	i|I)
		clear
		echo -n "Please type a file name: "
		read file1
# This echo and read command work as above but we are gathering the variable called file1 this will be passed to the more command to display the contents of the chosen file
		echo
		more "$file1"
# The "more" command will display the contents of the variable file if it exists, if the file typed does not match something that is currently in the folder then it will return an error
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
	j)
		echo "Thank you for using this Command Menu!"
# For this option we only have an echo and no other command because the until loop will end at this point and exit the program
		;;
	*)
# The above line is called a "Catch-all" meaning if the user inputs anything besides the options above then they will receive the below message
		clear
		echo "Bad command selection: $answer"
		echo "Please try again or choose j to exit"
# This is the message that the user will receive if they input any command that is not specified
		echo
		read -n 1 -s -p "Press any key to continue"
		clear
		;;
esac
# This line will end or close the case (syntax)
clear
done
# This line will end or close the until loop (syntax)