##for loop is used to iterate through a sequece like list, tuple or string[iterables]

fruits=['apple','mango','guava','kiwi','banana']
for item in fruits:
    print(item)

##same thing with while loops is tedius, lets see:
''' 
fruits=['apple','mango','guava','kiwi','banana']
a=0
while a<len(fruits):
    print(fruits[a])
    a=a+1  
'''

##range function in python is used to generate a sequence of numbers.
##we can also specify the start, stop and step-size : range(start,stop,step-size)
for a in range(1,10,3):
    print(a) #result:1,4,7
else:
    print('else is optional')

##break statement
#used to come out of the loop when encountered. It instructs the program to exit the loop now. 

for a in range (8):
    print(a)
    if a==6:
        break  #puts break in the middle of a program

else:
    print('done re baba')  ## couldn't execute as it executes only on the successful termination of a program.

## continue statement
#used to skip a value
for a in range (9):
    if a==3:
        continue
    print(a)  ##result: it will ignore 3 and then continue to print. 