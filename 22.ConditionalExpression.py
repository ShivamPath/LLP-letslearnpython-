# if/elif(Elseif),else ladder..

# it will print the first true statement and disregard the other if, elif and else statement.
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
#The else keyword catches anything which isn't caught by the preceding conditions.

 

price= 100

##if-elif-else ladder 
if price <=40:
 print("price is less than 40")
elif price==200:    #"==" is being used becuase single "=" is assignment operator. 
 print("price is 100")
elif price>400:
    print("price is less than 400")

else:
    print(420)

##multiple 'if' statement : 'if' is an independent statement, it does not form ladder. 
if price<110:
    print("price is less than 110") #price is less than 110

if price<120:
    print("price is less than 120") #price is less than 120

if price<150:
    print("price is less than 150") #price is less than 150


## write a program to print yes when the age entered by the user is greater than or equal to 18.

age=int (input("enter your age"))
age=int(age)
if age>= 18:
    print('Yes')

else:
    print("No")







