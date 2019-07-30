#build in basic AI to play against the player
#need to finish explaining all of the different functions
#work on AI stuff

#the basic strucure of the flowchart:
"""program starts by asking player to choose X or O. Program then randomly chooses who goes first.
   Then the player and computer take turns making moves. After the player or the computer makes a move, the program
   will check whether they won or caused a tie, and then the game switches turns. After the game is finished, the program
   will ask the player if they want to play again."""

#basic lay out of code:
'''the first step is to represent the board as data in a variable. It'll be similar to ASCII art used in Hangman. 
   Each string represents one of the nine spaces on the board. The strings are either 'X', 'O', or ' ' (for a blank space).

import random

#Part I: Draw the Board
  """This function will draw the board for us. Remember, the board is represented as a list of 10 strings, where the string at
      index 1 is the mark on space 1 and so on. The string at index 0 is ignored. We can build functions that will work by
      passing a list of 10 strings as the board."""
  
def drawBoard(board):
  #this function will print the 'board' that you pass in
  
  #the way we make the 'board' is essentially by creating a list of 10 strings representing the board (ignore the index 0).
 print(board[7] + '|' + board[8] + '|' + board[9])
 print('-+-+-')
 print(board[4] + '|' + board[5] + '|' + board[6])
 print('-+-+-')
 Print(board[1] + '|' + board[2] + '|' + board[3])
 
 #Part II: Letting the player choose X or O
  """This function will ask the player to be X or O. So we start with an empty variable, this use a while loop to 
      evaluate it until the player makes a choice (between X and O). Use .upper()
 def inputPlayerLetter():
  #this is how we get the player to enter X or O.
  #this will then return a list with the player's letter as the first item and computer's letter as the second item.
  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print('Do you want to be X or O?')
    letter = input().upper()
    
 #the first element in the list is the player's letter; the second is the computer's letter.

if letter == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']

#Part III: Deciding Who Goes First
"""create a function that uses randint() to choose whether the computer or the player moves first."""
def whoGoesFirst():
  #Randomly choose which player goes first.
  if random.int(0,1) == 0:
    return 'computer'
  else:
    return 'player'

#Part IV: Placing a Mark on the Board:
"""We will use 3 parameters here to pass into the function. 
    BOARD: is the list with 10 strings that represents the state of the board.
    LETTER: is the player's letter (X or O).
    MOVE: is the place on the board where the player wants to go (which is an integer 1 to 9).
    When a list value is passed for the BOARD parameter, the function's local variable is really a
    copy of the reference list, and not a copy of the list itself. So even though BOARD is a local variable,
    the makeMove() function modifies the original list. The LETTER and MOVE parameters are copies of the 
    string and integers that you pass, and since they are copies of values, so if you modify LETTER or MOVE in 
    ths functin, the original variables you used when you called makeMove() aren't modified"""
def makeMove(board, letter, move):
  board[move] = letter . #build this out and explain list references here
  
#Part V: Checking Whether the Player Won:  
'''basically all of the isWinner function is just one really long RETURN statement.
   The BO and LE names are shortcuts for the BOARD and LETTER parameters, just makes for less typing.
   We're just spelling out all of the 8 possible ways you can win in Tic-Tac-Toe, so each line checks
   whether th 3 spaces for a given line are equal to the letter provided and then we combine each line
   using OR to check for the 8 different ways to win. So only 1 of the 8 ways must be TRUE to win'''
def isWinner(bo, le):
  #given a board and a player's letter, this function returns True if that player has won.
  #we use 'bo' instead of 'board' and 'le' instead of 'letter' to cut down typing.
  return ((bo[7] == le and bo[8] == le and bo[9] == le) or #Across the top
          (bo[4] == le and bo[5] == le and bo[6] == le) or #Across the middle
          (bo[1] == le and bo[2] == le and bo[3] == le) or #Across the bottom
          (bo[7] == le and bo[4] == le and bo[1] == le) or #Down the left side
          (bo[8] == le and bo[5] == le and bo[2] == le) or #Down the middle
          (bo[9] == le and bo[6] == le and bo[3] == le) or #Down the right side
          (bo[7] == le and bo[5] == le and bo[3] == le) or #Diagonal
          (bo[9] == le and bo[5] == le and bo[1] == le) or #Diagonal 
          
def getBoardCopy(board):
'''ths function allows you to easily make a copy of the board given the 10-string list that represents it.  The reason 
   for this is becaause when the AI algo is planning its move, it'll need to make modifications to a temp copy of the board
   without making changes to the actual board. In these instances we need to call this function to make a copy of the board's
   list. So boardCopy starts as an empty list, then the FOR LOOP will iterate over the BOARD parameter and append a copy of
   the string values in the actual board to the duplicate board. After getBoardCopy() function builds up a copy of the actual
   board, it returns a reference to this new board in boardCopy, not to the original one in BOARD.''' 
  #makes a copy of the board list and returns it.
  boardCopy = []                                 #starts with an empty list
  for i in board:
    boardCopy.append(i)                          #iterates through all of the stuff on the board and appends it to the copy
  return board Copy
          
def isSpaceFree(board, move):   
  #returns True is the move passed in is free on the current board. If the space's index isn't equal to ' ' then it's not free.
  return board[move] == ''

def getPlayerMove(board):
  #lets the player enter their move.
  '''player enters a number for the space they want to move to. The loop makes sure that the execution doesn't move forward until
      the player enters an integer between 1 and 9. It also checks to make sure the space is free, given the board passed to the
      function for the BOARD parameter. We just use split() because it makes it easier to write out'''
  move = ''
  while move not in '1 2 3 4 5 6 7 8 9'.split() or
          not isSpaceFree(board, int(move)):
  return int(move)

defchooseRandomMoveFromList(board, movesList):
  #returns a valid move from the passed list on the passed board. Basically our 'AI'.
  #returns None if there is no valid move.
  possibleMoves = []
  for i in movesList:
    if isSpaceFree(board, i):
      possibleMoves.append(i)
  '''first this checks that the space is available to make a move on. possibleMoves starts as a blank list, the for loop then
      iterates over movesList. The moves that cause isSpaceFree() to return TRUE are added to possibleMoves with append().
      At this point, the possibleMoves list has all of the moves that were in movesList that are also free spaces. The program
      then checks whether the list is empty using the following below:'''
          
if len(possibleMoves) != 0:
  return random.choice(possibleMoves)
else:
  return None
'''if the list isn't empty, then there's at least one possible move that can be made on the board.'''
def getComputerMove(board, computerletter):
  #given a specific board and the computer's letter, this determines where to move and then returns that move.
if computerLetter == 'X':
  playLetter = 'O'
else:
  playLetter = 'X'

#This is the algo for the Tic-Tac-Toe AI:
#First, check if we can win in the next move.
for i in range(1, 10):
  boardCopy = getBoardCopy(board)
  if isSpaceFree(boardCopy, i):
    makeMove(boardCopy, playerLetter, i)
    if isWinner(boardCopy, computerLetter):
      return i

#Check if the player could win on their next move, and if so, block them
for i in range(1, 10):
  boardCopy = getBoardCopy(copy)
  if isSpaceFree(boardCopy, i):
    makeMove(boardCopy, playerLetter, i)
    if isWinner(boardCopy, playerLetter):
      return i

#Try to take one of the corners, if they are free.
move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
if move != None:
  return move

#Try to take the center, if it's free.
if spaceFree(board, 5):
  return 5

#Move on one of the sides.
return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
  #return True if every space on the board has been taken, otherwise, return False.
  for i in range(1, 10):
    if isSpaceFree(board, i):
      return False
    return True

print('Welcome to Tic-Tac-Toe! Buckle up!!')

while True:
  #reset the board.
  theBoard = [' ']*10
  playLetter, computerLetter = inputPlayerLetter()
  turn = whoGoesFirst()
  print('The ' + turn + ' will go first.')
  gameIsPlaying = True
         
  while gameIsPlaying:
    if turn == 'player':
      #Player's turn
      drawBoard(theBoard)
      move = getPlayerMove(theBoard)
      makeMove(theBoard, playerLetter, move)

      if isWinner(theBoard, playerLetter):
           drawBoard(theBoard)
           print('Congrats! You have won the game!')
           gameIsPlaying = False
      else:
          if isBoardFull(theBoard):
              drawBoard(theBoard)
              print('The game is a tie!')
              break
          else:
              turn = 'computer'

      else:
          #Computer's Turn
          move = getComputerMove(theBoard, computerLetter)
          makeMove(theBoard, computerLetter, move)

          if isWinner(theBoard, computerLetter):
              drawBoard(theBoard)
              print('The computer has beaten you. You lose!')
              gameIsPlaying = 'False'
          else:
              if isBoardFull(theBoard):
                  drawBoard(theBoard)
                  print('This game is a tie!')
                  break
              else:
                  turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break


            


          #need to figure out rest of lay out and next steps
  
