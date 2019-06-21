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

