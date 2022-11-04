'''create an empty dictionary and allow 4 friends to enter their favorite language as values
and use keys as their names. Assume that the names are unique'''

from re import A


favLang={}
a=input("enter ishika favorite language")
b=input("enter sumit favorite language")
c=input("enter Manoj Favorite language")
d=input("enter Harish favorite language")

favLang['Ishika']=a
favLang['Sumit']=b
favLang['Manoj']=c
favLang['Harish']=d

print(favLang)

#if the key is same then latest entry will prevail.
 