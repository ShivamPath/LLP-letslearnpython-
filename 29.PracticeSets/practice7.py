##write a python function to remove a given word from a list and strip it at the same time.

'''
this='   Shivam is learning python     '
print(this)
print(this.strip())  #it removes unwanted space.   

 '''


def remove(a):
    return a.strip()

a=input("enter the word")

print (remove(a))