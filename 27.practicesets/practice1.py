##write a program to print multiplication table of a given number using for loop.
b=int(input('enter the number'))

for a in range (b,b*11,b):
   print(a)

##another way to do this:
for a in range (1,11):
     print(f"{b}*{a}={b*a}")  #we can enter avaluation in using "f" string