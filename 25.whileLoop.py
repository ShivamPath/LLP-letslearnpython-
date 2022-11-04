'''sometimes we want to repeat a set of statement in our program, for instance: print 1 to 1000.
loops makes it easier for a programmer to tell the computer, which set of instructions to repeat and how'''

#types: while loop ||  for loop

##while loop : it will continue to check and execute a program until the condition becomes false. 
               #otherwise it will enter into infinite loop.  

number=0

while number<=5:
    print(number)
    number=number+1 # it will keep on executing until the condition is True.
print('done')  

