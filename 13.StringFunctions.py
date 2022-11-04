Story="once upon a time, there was a king, whose name was Dashrath and Dashrath was very kind"
print(len(Story)) #len is used to count the characters used in a string.

Shivam=" Jai maharashtra"
print(len(Shivam)) #result: 16

Dham= "Badrinath"
print(len(Dham)) #result: 9

print(Story.endswith("Dashrath")) #Result: True
print(Story.endswith("Ram")) #Result: False
   
print(Story.count("t")) #result:3, as this para has 3 t in it. 

print(Story.count("whose")) #1, as whose appreared only once in this para. 

print(Story.capitalize()) #it capitalised the first word in the string.

print(Story.find("Dashrath"))  #it get the index of string. only catches first occurence.

print(Story.replace("Dashrath","Ram")) #Dashrath replaced with Ram in all occurence of string.



