''' 
a spam comment is defined as a text containing following keywords:
"make a lot of money", "buy now", "subscribe this", "click this" 
'''
comment = input("enter your massage")

if "make a lot of money"  in comment:
    spam= True
elif "buy now" in comment:
    spam=True
elif "subscribe this" in comment:
    spam= True
elif "click this" in comment:
    spam=True
else:
    spam=False

if (spam):
    print("Alert! This is a spam!")
else:
    print(comment)

