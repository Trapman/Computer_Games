# write in a bit more detail about each function

import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNumber():
  #Returns a string of unique random digits that is NUM_DIGITS long.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(NUM_DIGITS):              #so this iterates NUM_DIGITS amount of times (in this case 3 times)
    secretNum += str(numbers[i])           #each iteration in for loop, the integer at index i is pulled from the shuffled list 
  return secretNum                         #and converted to a string, then concatenated to the end of secretNUM
                                           #augmented assignment: +=  is just a short cut 
  
def getClues(guess, secretNum):
  #Returns a strong with the Pico, Fermi, and Bagels cluse to the user.
  if guess == secretNum:
    return 'You guessed it correctly!'
    
  clues = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:        #if it matches the exact position
      clues.append('Fermi')
    elif guess[i] in secretNum:
      clues.append('Pico')
   if len(clues) == 0:
      return 'Bagels'
    
clues.sort()
return ' '.join(clues)

def isOnlyDigits(num):
  #returns True is num is a strong of only digits. Otherwise, returns False.
  if num == '':
    return False
  
  for i in num: 
    if i not in '0 1 2 3 4 5 6 7 8 9'.split():
      return False
    
    return True
  
print('I am thinking of a %s-digit number. Try to guess what it is.' %
      (NUM_DIGITS))
print('The clues I am giving are...')
print('When I say:   That means:')
print('   Bagels      None of the digits is correct.')
print('   Pico        One digit is correct but in the wrong position.')
print('   Fermi       One digit is correct and in the right position.')

while True:
  secretNum = getSecretNum()
  print('I have thought of a number, and you have %s guesses to get it.' %
        (MAX_GUESS))
  
  guessesTaken = 1
  while guessTaken <= MAX_GUESS:
    guess = ''
    while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
      print('Guess #%s: ' % (guessesTaken))
      guess = input()
      
      print(getClues(guess, secretNum)
            guessesTaken += 1
            
            if guess == secretNum:
              break
            if guessesTaken > MAX_GUESS:
              print('You ran out of guesses. The answer was %s.' %
                    (secretNum))
            
      print('Do you want to play again (yes or no)')
      if not input().lower().startswith('y'):
            break
