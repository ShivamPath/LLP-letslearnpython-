##add
Rankholder={'Manoj', 'Shivam', 'Shreya'}
Rankholder.add('Amol')
Rankholder.add('Manoj')
Rankholder.add('Amol')
print(Rankholder) #Result: {'Shreya', 'Manoj', 'Shivam', 'Amol', Himesh}

#list can not be added in Set as list is mutable 
# Rankholder.add(['Happy' 'Roy' 'Koti'])
# print(Rankholder) #result: TypeError: unhashable(mutable) type: 'list'

#Tuple can be added in Set
Rankholder.add(('Happy', 'Roy','Koti')) #{'Amol', 'Shivam', ('Happy', 'Roy', 'Koti'), 'Manoj', 'Shreya'} 
print(Rankholder)

#Dictionary also can not be added in Set  as it is unhashable(mutable)
# Rankholder.add({5:2})
# print(Rankholder) #result: TypeError: unhashable type: 'dict'
 

##len method
print(len(Rankholder)) #result 5, printed the length of Set.

##remove Method
Rankholder.remove("Shivam") 
print(Rankholder) # shivam removed from Set

## pop Method
Rankholder.pop()
print(Rankholder) #remove an arbitrary element
 
##clear method: emptize the set
# Rankholder.clear()
# print(Rankholder) #result: set()

##union method "|": returns a new set with all item from both sets
Topper={'Praveen', 'Naveen', 'Prashant'}
print(Rankholder|Topper) #result: {'Prashant', 'Praveen', 'Naveen', 'Manoj', 'Shivam', 'Shreya'}

##Intersection : returns a set which contains only items in both sets
classMonitor={'Rajat', 'Naveen', 'Shivam'}
print(Topper.intersection(classMonitor)) #result: Naveen

