#focus on more advanced uses of print() functions
#escape characters
#single/double quotes for strings
#using print()'s end key word parameter to skip new lines


print('What do you get when you cross a snowman with a vampire?')     #use the print() func call to ask and give the answers
input()                                                               #we don't want the user to immediately read the joke's punchline
print('Frostbite!')
print()                                                               #use a print() func here just to tell the program to print an empty line. This keeps the text looking clean.
print('What do dentists call an astronaut\'s cavity?')                #need to use an escape here (\) to add the apostrophe, otherwise the code would have been interpreeted as the end of the string.
input()
print('A black hole!')
print()
print('Knock knock.')
input()
print('Who's there?')
input()
print('Interupting cow.')
input()
print('Interupting cow wh', end='')               '''print() can have a second parameter, `end`. the blank string passed into 
print('-MOO!')                                       print() is a `keyword argument` , the `end` in `end=` is a `keyword parameter`.
                                                     To pass a keyword argument into this keyword parameter, you must type
                                                     `end=` before it so because we passed a blank string into the
                                                     end parameter, the print() function will add a blank
                                                     string instead of adding a new line.'''
                                                     
                                                  

