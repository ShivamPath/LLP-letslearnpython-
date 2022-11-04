'''Write a program to create a dictionary of Hindi words with values as their english translation and 
    provide user with an option to look it up.''' 

hinditoenglish= {'sham':'evening',
'subah':'morning', 'ratri':'Night'
}

print("my options are" ,hinditoenglish.keys())
a=input('Enter the Hindi word\n')

print('meaning:',hinditoenglish[a]) #result as per the key, but throws an "error" if the key is wrong. 
print('Meaning:', hinditoenglish.get(a))# result as per the key but, throws "none" if the key is wrong. 


