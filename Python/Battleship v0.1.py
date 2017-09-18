from random import randint

#this will be turned into the rows and cols of "O"s that are being shown
board = []

#this creates the list of "O"s used for the board
for x in range(5):
  board.append(["O"] * 5)

#this cleans up the list being shown
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

#this random row and col are where the "Enemy ship" is created
#this is also the numbers that the player wants to guess
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#these lines are for debugging the code and show where the ship is
#I've added 1 to make it more easy for someone not used to python lists
#they generally start with a zero
#print ship_row + 1
#print ship_col + 1

#this first for loop takes the input from the player and subtracts 1 from the number typed
#I've subtracted 1 to make it more easy for someone not used to python lists
#they generally start with a zero
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: ")) - 1
  guess_col = int(raw_input("Guess Col: ")) - 1

#this if loop will check where the player has "shot" and will return the correct outcome
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
#this elif checks to see if the shot was already selected, if so it will tell the player
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
#this else statement will put an X on the board where the player has shot and return that this was a miss
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
#this final if loop will check the turn count and allow the player 4 shots
    if turn == 3:
      print "Game Over"
      
  print_board(board)