import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNumber():
  #Returns a string of unique random digits that is NUM_DIGITS long.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum
  
def getClues(guess, secretNum):
  #Returns a strong with the Pico, Fermi, and Bagels cluse to the user.
  if guess == secretNum:
    return 'You guessed it correctly!'
    
  clues = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:        #if it matches the exact position
      clues.append('Fermi')
    elif guess[i]
