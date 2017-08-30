Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> c = 30
>>> d = 40
>>> print("hello world")
hello world
>>> print("hello world")
hello world
>>> print("hello world")
hello world
>>> print "hello world"
hello world
>>> print(hello world)
SyntaxError: invalid syntax
>>> j=50
>>> print(j)
50
>>> print(J)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(J)
NameError: name 'J' is not defined
>>> Print("Hello There!")

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Print("Hello There!")
NameError: name 'Print' is not defined
>>> 1 + 1
2
>>> K = 5
>>> print(j+K)
55
>>> J = 50
>>> A = "John is Happy"
>>> A
'John is Happy'
>>> J
50
>>> K
5
>>> print(A)
John is Happy
>>> B = 10.75
>>> B
10.75
>>> type(B)
<type 'float'>
>>> type(A)
<type 'str'>
>>> B = 5
>>> type(A)
<type 'str'>
>>> type(B)
<type 'int'>
>>> 25 > 10
True
>>> 10 > 25
False
>>> J is 59
False
>>> J is 50
True
>>> J is not 50
False
>>> M = 50
>>> J is M
True
>>> id(M)
40597140
>>> id(K)
40597680
>>> id(J)
40597140
>>> id(50)
40597140
>>> 10 == 10
True
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
55
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
55
>>> C:/Python27/Scripts/TTA class.py
SyntaxError: invalid syntax
>>> if J > 25
SyntaxError: invalid syntax
>>> if J > 25:
	print("J is greater than 25")

	
J is greater than 25
>>> if J > 25:
	print("J is the winner")

	
J is the winner
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 5, in <module>
    if B == 20:
NameError: name 'B' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
20 is equal to B
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
20 is not equal to B
>>> name = 'Ashley'
>>> print(name.lower())
ashley
>>> print(name.upter())

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(name.upter())
AttributeError: 'str' object has no attribute 'upter'
>>> print(name.uper())

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(name.uper())
AttributeError: 'str' object has no attribute 'uper'
>>> print(name.upper())
ASHLEY
>>> name = 'Ashley'.lower()
>>> print name
ashley
>>> print(name.upper())
ASHLEY
>>> name = 'Ashley'
>>> name = name.upper()
>>> print name
ASHLEY
>>> print(name[0])
A
>>> print(name[2])
H
>>> L = ['mother', 'father', '1970', '1965']
>>> print L
['mother', 'father', '1970', '1965']
>>> print(L[3])
1965
>>> print(L)
['mother', 'father', '1970', '1965']
>>> tupA = ('brother", "sister", "1990", "1992", "1993", "1995")
	
SyntaxError: EOL while scanning string literal
>>> tupA = ("brother", "sister", "1990", "1992", "1993", "1995")
>>> print(tupA[1:4])
('sister', '1990', '1992')
>>> L = ['mother', 'father', ["a", "b", "c"], '1970', '1965']
>>> print(L[3])
1970
>>> print(L[2])
['a', 'b', 'c']
>>> print(L[2,2])

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(L[2,2])
TypeError: list indices must be integers, not tuple
>>> print(L[2:2])
[]
>>> print(L[2:1])
[]
>>> print(L[2;1])
SyntaxError: invalid syntax
>>> print(L[2.1])

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(L[2.1])
TypeError: list indices must be integers, not float
>>> print(L[2][2])
c
>>> print(L[2][1])
b
>>> print(L[3][1])
9
>>> L = ['mother', 'father', ["abc", "bcd", "cde"], '1970', '1965']
>>> print(L[3][1])
9
>>> print(L[2][1])
bcd
>>> Q = 2
>>> print(L[Q][1])
bcd
>>> mylist = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
>>> set(mylist)
set([1, 2, 3, 4, 5, 6])
>>> date = "3/13/2017"
>>> split_the_date = date.split('/')
>>> print (split_the_date)
['3', '13', '2017']
>>> split_the_date = date.split(',')
>>> date = "3, 13, 2017"
>>> print (split_the_date)
['3/13/2017']
>>> date = "3/13/2017"
>>> split_the_date = date.split('/')
>>> print (split_the_date)
['3', '13', '2017']
>>> print (split_the_date[0])
3
>>> name = "Mikel Jenosn"
>>> print(name.swapcase())
mIKEL jENOSN
>>> name = "Mikel Jenson"
>>> print(name.swapcase())
mIKEL jENSON
>>> color = "	this color is blue      "
>>> print(color.strip())
this color is blue
>>> color = "	this color 		 is     blue      "
>>> print(color.strip())
this color 		 is     blue
>>> color = "	this color is blue      "
>>> print(color.strip())
this color is blue
>>> 10 >= 10
True
>>> 11 >= 10
True
>>> 5 >= 10
False
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
Play again
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
Quitting Game
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
Please enter Yes or No
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
Please enter the date: 8/26/2017
The date you entered is 8/26/2017
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
Please enter the date: 08262017
The date you entered is 08262017
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
you like candy?
Do you like candy?: yes
You like candy
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
you like candy?
Do you like candy?: no
You dont like candy?!
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
you like candy?
Do you like candy?: maybe
Please enter Yes or No
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
you like candy?
Do you like candy?: YES
You like candy
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
1

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 39, in <module>
    time.sleep(.5)
NameError: name 'time' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
1
2
3
4
5
6
7
8
9
10
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
10
9
8
7
6
5
4
3
2
1
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
jeans
pants
jacket
shoes
belt
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
jeans
pants
jacket
shoes
belt
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
jeans
pants
jacket
shoes
belt
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
0
1
2
3
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
4
3
2
1
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
3
2
1
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
3
2
1
0
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
8
6
4
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
8
6
4
2
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
one
two
three
four
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
1
2
3
4
5
6
7
8
9
10
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
you like candy?
Do you like candy?: yes
You like candy
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 25, in <module>
    while Candy != quit:
NameError: name 'Candy' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
Do you like candy?: yes
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
you like candy?
Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 28, in <module>
    print("you like candy?")
  File "C:\Python27\lib\idlelib\PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
['beatle', 'Rolling', 'Led', 'Hendrix']
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 64, in <module>
    print(Best_bands_list + "These are the best bands!")
TypeError: can only concatenate list (not "str") to list
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
beatleThese are the best bands!
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
beatle is the best bands!
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
['beatle', 'Rolling', 'Led', 'Hendrix', 'temp']
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
['beatle', 'Rolling', 'James Brown', 'Hendrix', 'temp']
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
beatle are great bands
Rolling are great bands
James Brown are great bands
Hendrix are great bands
temp are great bands
>>> Birth_Diction={"Emily" : "June 1950","Maxine" : "March 1962","Kelly" : "May 1955","Violent" : "Jan 1948"}
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violent': 'Jan 1948', 'Emily': 'June 1950'}
>>> print(Birth_Diction['Maxine'])
March 1962
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violent': 'Jan 1948', 'Emily': 'June 1950'}
>>> Birth_Diction={"Emily" : "June 1950","Maxine" : "March 1962","Kelly" : "May 1955",/n "Violent" : "Jan 1948"}
SyntaxError: invalid syntax
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violent': 'Jan 1948', 'Emily': 'June 1950'}
>>> Birth_Diction['emily']='December 1975'
>>> print(Birth_Diction
      
KeyboardInterrupt
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'emily': 'December 1975', 'Violent': 'Jan 1948', 'Emily': 'June 1950'}
>>> Birth_Diction['Emily']='December 1975'
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'emily': 'December 1975', 'Violent': 'Jan 1948', 'Emily': 'December 1975'}
>>> Birth_Diction={"Emily" : "June 1950","Maxine" : "March 1962","Kelly" : "May 1955",/n "Violent" : "Jan 1948"}
SyntaxError: invalid syntax
>>> Birth_Diction={"Emily" : "June 1950","Maxine" : "March 1962","Kelly" : "May 1955","Violent" : "Jan 1948"}
>>> Birth_Diction['Emily']='December 1975'
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Violent': 'Jan 1948', 'Emily': 'December 1975'}
>>> print("Kelly's Birthday is: " + Birth_Diction['Kelly']
      
KeyboardInterrupt
>>> print("Kelly's Birthday is: " + Birth_Diction['Kelly'])
Kelly's Birthday is: May 1955
>>> Birth_Diction['Sara']='November 1980'
>>> print(Birth_Diction)
{'Kelly': 'May 1955', 'Maxine': 'March 1962', 'Sara': 'November 1980', 'Violent': 'Jan 1948', 'Emily': 'December 1975'}
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 75, in <module>
    Print(Sub(20, 10))
NameError: name 'Print' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 75, in <module>
    Print(Subtraction(20, 10))
NameError: name 'Print' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 76, in <module>
    Print(Subtraction(20,10))
NameError: name 'Print' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
10
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
10
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 85, in <module>
    print("you are: " + age)
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
you are: 5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
5
you are: 5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
5
you are: 5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
you are: 5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
<type 'int'>
you are: 5
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
<type 'int'>
you are: 5
<type 'int'>
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
<type 'int'>
you are: 5
<type 'str'>
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
<type 'int'>
you are: 5
<type 'int'>
>>> print age
5
>>> del age
>>> print age

Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    print age
NameError: name 'age' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
What is your age? 5
<type 'int'>
you are: 5
<type 'int'>

Traceback (most recent call last):
  File "C:/Python27/Scripts/TTA class.py", line 95, in <module>
    print age
NameError: name 'age' is not defined
>>> 
================= RESTART: C:/Python27/Scripts/TTA class.py =================
beatle are great bands
Rolling are great bands
James Brown are great bands
Hendrix are great bands
temp are great bands
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
2
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
5
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
5
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
4
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
1
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
3
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================

Traceback (most recent call last):
  File "C:/Python27/Scripts/importmodule.py", line 2, in <module>
    from PythonModule import subtract_5
ImportError: cannot import name subtract_5
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================

Traceback (most recent call last):
  File "C:/Python27/Scripts/importmodule.py", line 2, in <module>
    from PythonModule import subtract_5
ImportError: cannot import name subtract_5
>>> 
================ RESTART: C:/Python27/Scripts/importmodule.py ================
5
15
8
5
>>> import sleep

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    import sleep
ImportError: No module named sleep
>>> import sleep

Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    import sleep
ImportError: No module named sleep
>>> import time
>>> time.sleep(5)
>>> 
