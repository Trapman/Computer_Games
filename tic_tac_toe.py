#build in basic AI to play against the player
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

#Part IV: Placing a mark on the Board:
"""We will use 3 parameters here to pass into the function. 
    BOARD: is the list with 10 strings that represents the state of the board.
    LETTER: is the player's letter (X or O).
    MOVE: is the place on the board where the player wants to go (which is an integer 1 to 9)."""
def makeMove(board, letter, move):
  board[move] = letter
  
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
  #makes a copy of the board list and returns it.
  boardCopy = []                                 #starts with an empty list
  for i in board:
    boardCopy.append(i)                          #iterates through all of the stuff on the board and appends it to the copy
  return board Copy
          
def isSpaceFree(board, move):
  #returns True is the move passed in is free on the current board.
  return board[move] == ''

def getPlayerMove(board):
  #lets the player enter their move.
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
          
if len(possibleMoves) != 0:
  return random.choice(possibleMoves)
else:
  return None

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
  
