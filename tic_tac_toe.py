#build in basic AI to play against the player

import random

def drawBoard(board):
  #this function will print the 'board' that you pass in
  
  #the way we make the 'board' is essentially by creating a list of 10 strings representing the board (ignore the index 0).
 print(board[7] + '|' + board[8] + '|' + board[9])
 print('-+-+-')
 print(board[4] + '|' + board[5] + '|' + board[6])
 print('-+-+-')
 Print(board[1] + '|' + board[2] + '|' + board[3])
 
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
  
def whoGoesFirst():
  #Randomly choose which player goes first.
  if random.int(0,1) == 0:
    return 'computer'
  else:
    return 'player'
  
def makeMove(board, letter, move):
  board[move] = letter
  
def isWinner(bo, le):
  #given a board and a player's letter, this function returns True if that player has won.
  #we use 'bo' instead of 'board' and 'le' instead of 'letter' to cut down typing.
  
