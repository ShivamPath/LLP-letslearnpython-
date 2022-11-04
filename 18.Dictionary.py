#Dictionary= collection of key-value pairs
#it is unordered, mutable, indexed, can't contain duplicate keys
#myDict={'Ashram':'Japnam'} Ashram= Key, Japnam=Value

myDict={'Ashram':'Japnam',
'GOW':'Etna badi ho gyi ho, biyah nhi hua hai', 
'Mirzapur':'Bhaiya me Bhaiya Munna Bhaiya',
'Kitne admi the':[1,2,3],#it can include list as well
'AshramParts':{'Ashram1':'Japnam Japnam', 'Ashram2':'Baba Layenge Kranti', 'Ashram3':'Bhagwan'}} #dictionary within dictionary


print(myDict['Ashram']) #result: Japnam
print(myDict['Kitne admi the']) #Result: [1, 2, 3], it can print list as well
print(myDict['AshramParts']['Ashram2']) #Result: Baba Layenge Kranti # dictionary within dictionary

myDict['Kitne admi the']=['Pata nhi bhaiya'] #making changes 
print(myDict['Kitne admi the'])#result: Pata nhi bhaiya #Yeah! it is mutable 

