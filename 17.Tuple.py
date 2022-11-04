# a tuple is an "immutable" date type in python hence can not be manipulated. 
# friends=() empty tuple
# friends=(Praveen,) tuple with single element needs a commaa,
# friends= (Vishal, Praveen, Manoj, Shilpa) tuple with more than one element

friends=('Vishal', 'Praveen', 'Manoj', 'Shilpa', 'Vishal')
friends=friends.count('Vishal')
 
print(friends) #result 2 as the vishal has 2 occurences. 

Fruits=('Orange', 'Papaya', 'Grapes', 'Pineapple')
Fruits= Fruits.index('Pineapple')

print(Fruits) #result 3 as pineapple comes at 3rd index

