#variable : name givem to a memory location or (data type) in a program, e.g Name, address, roll no, age etc
#data type: integer, string, floating points no, Booleans (True or False), None
#keywords: reserved words in a program. it's not recommended to use keywords for naming variable. 
'''e.g def, class (for oops), False,True, None, await, import,  and, as,
 assert, async, break, continue, del, elif, else, except, finally, for, from, global, if, in, lambda, nonlocal,
 not, or, pass, raise, return, try, while, with, yield '''

# ctrl+enter to get into new line without affecting the first line
# alt+shift+Down  to copy the current line subject in the next line
# alt+shift+ click on any line to make any adjustment as the arrow bring you there
#alt+up/down arrow : to move the to previous or next line
name=input("enter the name")
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    
    print("Hello, " + name + ". Good morning!")

greet(name) #Hello, Shivam. Good morning!