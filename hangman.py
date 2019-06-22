#We will use lists, in, methods such as split(), lower(), upper(), startswith(), and endswith(), elif

import random  #since we'll want to randomly select a secret word for the player to guess

#make a constant variable with a list() for the hang man shapes (in ASCII)

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
      |
      |
     ===''', '''
  +---+
  0   |
  |   |
      |
     ===''', '''
  +---+
  0   |
 /|   |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 /\   |
     ===''', ''']

words = 'ant buford bulldog henley emi holly thai tut chase bradley dan tim felix zbo arlo'.split() #use split() here to make all of these words their own string instead of writing them all out manually like 'ant', 'buford', etc..

def getRandomWord(wordList):
  #this function returns a random string from the list of strings you pass into it.
  wordIndex = random.randint(0, len(wordList) - 1)
  return wordList(wordIndex)

def displayBoard(missedLetter, correctLetters, secretWord:
  #this function prints the Hangman board on the screen and displays how many letters the player has correctly/incorrectly guessed
  print(HANGMAN_PICS[len(missedLetters)])
  print()
  #so we have 3 parameters to pass into the func displayBoard
 
 print('Missed letters:' ends=' ')
 for letter in missedLetters:                #for loop to iterate over each character in missedLetters and display it on screen
  print(letter, end=' ')                     #use end=' ' to put a single space between every letter
 print()
