myDict={'bhagwan':'Bramha',
'devta':'Indra',
5:572}

#methods:
print(myDict.keys()) #result: bhagwan, devta, 5 # prints all the keys

print(myDict.values()) #result: ['bhagwan', 'devta', 5] # prints all the Values

print(myDict.items())#result:([('bhagwan', 'aham bramhashmi'), ('devta', 'Indra'), (5, 572)]), #Tuple return

print(type(myDict.keys()))  #result: <class 'dict_keys'>, #prints the data type

print(list(myDict.keys())) # to convert variable type dict_keys to list 

updateDict={'K.G.F': "Tanna ni na re na re nare",5:899}
myDict.update(updateDict) # to update(add or change) the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("bhagwan")) 
print(myDict["bhagwan"])  # prints associate value,  both does the same job.
# Difference, get: prints "none" if the key is wrong, whereas the later one prints error.

#for more methods, need to search google: python dictionary methods
