# List can be created by using []

Friends= ["Vishal", "Praveen", "Lalit", "Nazim", "Gagan"]
print(Friends[0]) #Vishal
print(Friends[2]) #Lalit
print(Friends[3]) #Nazim


#to change list value

Friends[3]="Naveen Ji"
print(Friends[3])

# We can create a list with different data type

Lists= 5, False, 25.5, "Shivam"
print(Lists[3]) #result: Shivam
print(type(Lists[2])) #result: float

#list slicing 
print(Friends[0:3]) #result: ['Vishal', 'Praveen', 'Lalit']
print(Friends[-4:]) #result: ['Praveen', 'Lalit', 'Naveen Ji', 'Gagan']



