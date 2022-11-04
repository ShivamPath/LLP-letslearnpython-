# Set is a collection of non repetative elements, {}
#unordered, unindexed, hashable, non mutable, no duplicacy. 
#can not put a list within Set as list is unhashable but we can put Tuple as tuple is also hashable. 

Topper={'Manoj', 'Manish', 'Shivam', 'Farhan', 'Richel', 'Gavisha', 'Shivam'}
print(Topper) #result {'Farhan', 'Manoj', 'Manish', 'Richel', 'Shivam', 'Gavisha'} #eliminated repeated Shivam.
print(type(Topper)) #class:set

Winner={} # empty dictionary not empty set
print(type(Winner)) #result: dict

#an empty set can be created using the below syntax:
Rankholder=set()
print(type(Rankholder)) #result: set`-` 