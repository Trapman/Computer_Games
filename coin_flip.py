#basic program to flip a coin 1,000 times, and a player will guess how many times it's heads/tails

import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press ENTER to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
  if random.randint(0, 1) == 1:                 #might be worth building this out later to include tails as well
    heads = heads + 1
   flips = flips + 1
   
   if flips == 900:
    print('900 flips and there have been ' + str(heads) + ' heads.')
   if flips == 100:
    print ('At 100 flips, heads has come up ' +str(heads) + ' times so far.')
   if flips == 500: 
    print('Halfway done and heads have come up ' str(heads) + ' times.')
    
print()
print('Out of 100 coin tosses, heads came up ' +str(heads) + ' times!)
print('Were you close? Tbh?')
####
