#write a program to find whether a given number is prime or not. 
number=int(input("enter the no"))
for i in range(2,number):
    if number%i==0:
        print("This is a not a prime no")
        break
    else:
        print("this is a prime no")
        break
