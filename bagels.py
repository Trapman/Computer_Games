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
                                           #augmented assignment: +=  is just a shortcut so you do not have to write the whole thing out
  
def getClues(guess, secretNum):                
  #Returns a strong with the Pico, Fermi, and Bagels cluse to the user.
  if guess == secretNum:
    return 'You guessed it correctly!'
    
  clues = []                            #start with an empty list
  for i in range(len(guess)):           #loop through each possible index
    if guess[i] == secretNum[i]:        #if it matches the exact position. Then appends Fermi
      clues.append('Fermi')
    elif guess[i] in secretNum:         #does no match exact position but is somewhere in the secretNum. Then apppends Pico
      clues.append('Pico')
   if len(clues) == 0:                  #if no match whatsoever, then append Bagel
      return 'Bagels'
    
clues.sort()                            #arranges the list items in alphabetical/numerical order. Do this to make it more difficult, otherwise they would be in order and the player would know
return ' '.join(clues)                  #returns a list of strings as a single string joined together. So we will get each string in CLUE combined with a single space between each string.

def isOnlyDigits(num):                  #just to make sure that the player has entered a number as their guess
  #returns True is num is a strong of only digits. Otherwise, returns False.
  if num == '':                         #checks to see if NUM is a blank string, and if so returns FALSE
    return False
  
  for i in num:                        #then if not blank, iterates through 0-9 to see if it is indeed a number that has been entered
    if i not in '0 1 2 3 4 5 6 7 8 9'.split():
      return False
    
    return True
  
print('I am thinking of a %s-digit number. Try to guess what it is.' %        #string interpolation: shortcut for using % placeholders instead of having to concat everything
      (NUM_DIGITS))                                                           #so %s just plugs in whatever value we have for NUM_DIGITS
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
