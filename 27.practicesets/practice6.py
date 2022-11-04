#write a factorial of n number
#Factorial: n!=1*2*3*4*5.......*n
# for eg: 5!=1*2*3*4*5

num=int(input("enter the number"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"the factorial of {num} is {factorial}")