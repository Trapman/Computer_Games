#We will use lists, in, methods such as split(), lower(), upper(), startswith(), and endswith(), elif

import random  #since we'll want to randomly select a secret word for the player to guess

#make a constant variable with a list() for the hang man shapes (in ASCII)
#note:if you ever want to add more guesses, just build more 'pics' to this HANGMAN_PICS list

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
     ===''', '''
     +---+
 [0   |
 /|\  |
 /\   |
     ===''', '''
     
     +---+
 [0]  |
 /|\  |
 /\   |
     ===''', ''']

#use dict to create the words in the Hangman game
words =  {'Colors': 'red orange yellow blue green black white brown tan violet'.split(),
          'Shapes': 'square triangle circle rectangle octogon pentagon chevron'.split(),
          'Fruits': 'apple grape orange watermelon pineapple blueberry tangerine lime lemon cherry'.split(),
          'Animals': 'bulldog cat dog rat tiger bull turtle wolf sheep'.split()}

#use choice() from random module to randomly choose a list 
def getRandomWord(wordList):
  #this function returns a random string from the passed dictionary of lists of strings and its key.
  #first: randomly select a key from the dict:
  wordKey = random.choice(list(wordDict.keys()))
  
  #second: randomly select a word from the key's list in the dictionary:
  wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
  
  return [wordDict[wordKey][wordIndex], wordKey]
  
#so the function now chooses a random key in the wordDict dictionary by calling random.choice()
#the function returns a list with two items: (1) wordDict[wordKey][wordIndex], (2) wordKey


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

difficultly = 'X'                                           #build in difficulty feature
while difficulty not in 'EMH':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard')
  difficulty = input.upper()
if difficulty == 'M':
  del HANGMAN_PICS[8]                     #deletes these indecies from the list
  del HANGMAN_PICS[7]
if difficulty == 'H':
  del HANGMAN_PICS[8]
  del HANGMAN_PICS[7]
  del HANGMAN_PICS[6]
  del HANGMAN_PICS[5]
  
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)   #basically using a 'multiple assignment' to assign the two returned values from getRandomWord(words) to secretWord and secretSet
gameIsDone = False

while True:
  print('The secret word is in the set: ' + secretSet)         #this gives the player a hint which set of words they're trying to guess
  displayBoard(missedLetter, correctLetters, secretWord)
  
  #let the player enter a letter.
  guess = getGuess(missedLetters + correctLetters)
  
  if guess in secretWord:
    correctLetters = correctLetters + guess
    
    #check if the player has won.
    foundAllLetters = True
    for i in range(len(secretWord)):
      if secretWord[i] not in correctLetters:
        foudAllLetters = False
        break
      if foundAllLetters:
        print('Congrats, the secret word is "' + secretWord + '"! You've won the game.')
        gameIsDone = True
      
      else: 
        missedLetters = missedLetters + guess
        
        #check to see if the player has guessed too many times and has lost the game
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
          displyBoard(missedLetters, correctLetters, secretWord)
          print('You've run out of guesses!\nAfter ' + 
            str(len(missedLetters)) + ' missed guesses and ' +
            str(len(correctLetters)) + ' correct guesses,
          the word was "' + secretWord + '"')
          gameIsDone = True
          
    #ask the player if they want to play again (but only if the game is actually done)
    if gameIsDone:
      if playAgain():
        missedLetters = ' '
        correctLetters = ' '
        gameIsDone = False
        secretWord, secretSet = getRandomWord(words)
    else:
         break
          
    
