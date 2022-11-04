#write a program to find the sum of first n natural number using while loop.
##traditional way
num=int(input("enter the number:  "))
print ((num*(num+1))/2)    

##using for loop
num=int(input("enter the no: "))
sum=0
for i in range(1, num+1):
    sum=sum+i
print(f"the sum of {num} is {sum}")
