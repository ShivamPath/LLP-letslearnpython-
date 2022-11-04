# input function : this function allows the user to take input from the keyboard as a "string"


a = input("enter you name:")
print (type(a))  # terminal will ask to enter name with the same string"enter your name:" 

#output of input is always string even numbers are entered. 

b= input("enter your class")
b=int(b)    #changing the input type from string to int
print(type(b)) # to check type of variable

Name=input("enter your father's name\n")
print(Name)
