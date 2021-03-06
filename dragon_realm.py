'''Premise: game in which the player decides between two caves, which hold either treasure or certain doom

The play is in a land full of dragons. All dragons live in caves with sultan-like treasures. Some dragons are friendly and 
will share their treasure with the player, while other dragons will kill the player upon entering the cave. The player has 
to decide between two caves. The challenge is that the player does not know what kind of dragon he will encounter in either of
the caves

We'll make use of a few different tools and techniques here:
_________________________________________________________________________
(1) flowcharts                            (8) global/local variable scope
(2) def functions                         (9) parameters and arguments
(3) multiline strings                     (10) sleep() function
(4) while statements
(5) and / or Boolean operators
(6) truth tables
(7) return keyword
__________________________________________________________________________


FLOWCHART
_______________
start--> prompt 1--> player choice a/b--> prompt 2/3 (dependent upon player choice)...--> ending 1/2

basically a visualization of what happens in each step. Helps keep everything in place especially when things gets complex.

import random       #needed for the randomint()function we'll use later
import time         #needed for time-related functions

def displayIntro():       #run this in a function so we can call the function anytime we need it instead of rewriting it each time. All it really does is run the print() call
  print('''You are in a land filled with dragons. Some of these dragons are friendly, some are hungry for human flesh. 
  Alas, you see two caves in front of you. In one cave, the dragon is friendly and will share his treasure with you. In the
  other, the dragon is greedy and hungry, and will eat you on sight.''')      #multiline strings, using ''' at the beginning allow you to write out longer sentences
  print()                            #just for linespacing to keep things clean
  
def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':                             #just use a while loop here to make sure the player makes a choice between 1 and 2
    print('Which cave will you venture into, friend? (1 or 2)')
    cave = input()
    
    return cave     #once the def function runs, it will return a value of 1 or 2
    
 def checkCave(chosenCave):                   #parameter usage 
  print('You approach the cave...')
  time.sleep(2)                               #the time module has a function, sleep() that pauses the program. It'll pause here for 2 seconds to add suspense. 
  print('It is dark and hard to see inside this cave...')
  time.sleep(2)
  print('A large dragon appears in front of you with a commanding stature. He opens his jaws...')
  print()
  time.sleep(2)
  
  friendlyCave = random.randint(1,2)        #just a call for the randint() function to decide which cave is friendly
  
  if choseCave == str(friendlyCave):       #to check the player's selection
    print('and tells you he will share his treasure!')
  else:
    print('tears you limb from limb!')
    
 playAgain = 'yes'
 while playAgain == 'yes' or playAgain == 'y':
  displayIntro()                                    #this is why we built the def above, so we could reuse it again later
  caveNumber = chooseCave()                         #basically everything starts over and we play again
  checkCave(caveNumber)
  
  print('Do you want to play again? (yes or no)')
  playAgain = input()
    


