#write a program to print multiplication table of a given number using while loop. 

number=int(input('enter the no'))
print( 'multiples of', number, 'are: ')
i=1
while i<=10:
    print(number,'x',i,'=', number*i)
    i=i+1
