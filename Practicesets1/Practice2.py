#write a program to store seven fruits in a list entered by user by removing already made list[1,2,3,4,5,6,7] 
Fruits=[1,2,3,4,5,6,7]
fruit1=input("enter the first fruit")
fruit2=input("enter the second fruit")
fruit3=input('enter the third fruit')
fruit4=input('enter the fourth fruit')
fruit5=input('enter the fifth fruit')
fruit6=input('enter the sixth fruit')
fruit7=input('enter the seventh fruit')

Fruits.insert(0,fruit1)
Fruits.insert(1,fruit2)
Fruits.insert(2,fruit3)
Fruits.insert(3,fruit4)
Fruits.insert(4,fruit5)
Fruits.insert(5,fruit6)
Fruits.insert(6,fruit7)
Fruits.remove(1)
Fruits.remove(2)
Fruits.remove(3)
Fruits.remove(4)
Fruits.remove(5)
Fruits.remove(6)
Fruits.remove(7)
print(Fruits)



