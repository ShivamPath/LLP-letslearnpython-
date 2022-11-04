# a function is a group of statements performing a specific task
''' when a program gets bigger in size and it's complexity grows and it gets difficult for a programmer
to keep track on, which piece of code is doing what?'''
# a fuction can be reused by the programmer in a given program any number of times. 
'''two types of functions in python: a-built in function [e.g=greet, multiply etc]and 
b- user defined functions [e.g=print,sum, range etc]  '''


def average(marks):
    return ((marks[0]+marks[1]+marks[2])/3)

marks2=[20,30,56]
print(average(marks2))


# name=input("enter your name")
def greet (name):
    print('Hello '+name+'! Very good morning to you!')

greet('Shivam')
   

##multiplicaton function
def multiply(a):
    return (a[0]*a[1]*a[2]*a[3]*a[4])

letsmultilpy= [2,3,5,5,3]
print(multiply(letsmultilpy))

# factorial functions 
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return (product)

print(factorial(4))
