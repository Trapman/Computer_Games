#Create a 'Guess the Number' game
"""In short, the computer will think of a number from 1-20 and will ask the user to guess it. After each guess, the computer
will tell the user whether their guess was too high or too low. The user wins if they can guess the number within 6 tries."""

import random                                         #so we can call the randint() function later

guessesTaken = 0                                      #to store the number of guesses the player has taken, starting at 0

print('Greetings! What is your name, friend?')        #ask player their name, then store input in 'myName' variable
myName = input()

number = random.randint(1, 20)              #now we need to generate a random number, from 1-20, and store in 'number' variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20. Let's see if you can guess it.')

for guessesTaken in range(6):                         #just a for loop that will repeat 6 times, with the following logic
  print('Take a guess, friend!')
  guess = input()                                     #player input stored as 'guess' variable
  guess = int(guess)                                  #turns the input into a int (from a string)
  
  if guess < number:
    print('Your guess is too low, friend, try again.')
  
  if guess > number
    print('Your guess is too high, friend, try again.')
  
  if guess == number: 
    print('Correct!')
    break
    
if guess == number:                                                                               #only runs if the correct number is guessed
  guessesTaken = str(guessesTaken + 1)                                                            #adds 1 to the total number of 'guessesTaken' and converts to str so we can use it in the next line as a concat
  print('Good job, ' + myName + '! You guessed my number in' + guessesTaken + guesses!')          #concat these two variables
  
if guess != number:                                  #only runs if the incorrect number is guessed
  number = str(number)                               #again, turns the number into str so we can concat in the next line
  print('Nope. The number I was thinking of was ' + number + '.')
