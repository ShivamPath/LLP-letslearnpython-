#need to write a letter with input function and replace function and show a result
from ast import LShift


letterExample='''Dear Name,

I'm Happy to tell you about your selection in Amazon. 
It's always day one. 

Regards
Sendername
Date'''
Name=input("enter your name")
Date=input("enter date")
Sender=input("enter sender's name")

letterExample=letterExample.replace("Name", Name)
letterExample=letterExample.replace("Date", Date)             
letterExample=letterExample.replace("Sendername", Sender)
print(letterExample)
 
