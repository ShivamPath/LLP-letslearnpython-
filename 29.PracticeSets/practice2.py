##write a python program to convert celsius to fahrenheit using function.

from calendar import c


cel=int(input("enter celsius: "))
def celfehr(cel):
        return ((cel*(9/5))+32)

print(celfehr(cel))
