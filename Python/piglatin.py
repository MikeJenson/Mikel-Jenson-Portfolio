#Simple Pig Latin Translator

pyg = 'ay'

#input from user
original = raw_input('Please enter a word and I will translate it to Pig Latin for you:')

#start if loop to find out if something was typed in and make sure that it only contains letters
if len(original) > 0 and original.isalpha():
  #Makes the input all lower case
  word = original.lower()
  #pulls the first letter of the input word
  first = word[0]
  #Creates the new word to be printed
  new_word = word[1:len(new_word)] + first + pyg
  print new_word
#if nothing is put in or if there is a non-alpha character this will be run  
else:
    print 'empty'