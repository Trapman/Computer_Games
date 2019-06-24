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
 
 #now we need to print the secret word, but blank lines for the letters that have yet to be guessed.
 blanks = '_' * len(secretWord)              #creates the blanks variable full of _ using multiplication/replication, and ensures it'll be the same number of _ as secretWord has in letters
 
 for i in range(len(secretWord)):            #this will replace _ with correctly guessed letters (if it exists in correctLetters)
  if secretWord[i] in correctLetters:
    blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
#now we need to get the player's guesses
def getGuess(alreadyGuessed)
  #returns the letter the player has entered. Makes sure that the player entered a single letter and not something else. 
  while True:
    print('Guess a letter.')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1                         #forces the player to enter a single letter
      print('Please enter a single letter.')
    elif guess in alreadyGuessed:
      print('You have already guess this letter, choose a different letter.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':                    
      print('Please choose a LETTER from a-z')
    else:
      return guess
      
def playAgain():
  #this function returns True if the play wants to play again, otherwise it'll return False
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')
  
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
  displayBoard(missedLetter, correctLetters, secretWord)
  
  #let the player enter a letter.
  guess = getGuess(missedLetters + correctLetters)
  
  if guess in secretWord:
    correctLetters = correctLetters + guess
    
    #check if the player has won.
    foundAllLetters = True
    for i in range(len(secretWord)):
    
