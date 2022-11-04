## relational operation are ==, >=, <= 

#logical operators use:-
''' and : if both the conditions are met) 
or      : if any of the condition is true, prints true else false
not     : inverts true to false and false to true  '''

#write a program which tells user if they can work with us or not with "and" relational operator  basis on their age. 
age=int(input("what's your age"))
if age>18 and age<40:
    print(" you are eligible to work with us")
else:
    print(" you're not eligible to work with us") 


#use of 'Or" logical operator

stack=input (" enter your web developement stack ")
if stack==("MERN") or stack==("MEAN"):
    print(" you are eligible for the project")
else:
    print(" Tumse no ho paega")

## use of "not" logical operator 
NaukariMilegi=True
print (not NaukariMilegi)




