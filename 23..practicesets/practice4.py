#write a program to find whether a given username contains less than 10 character or not

username=input("enter username")

if len(username) > 10:
    print("this username is invalid, there should be less than 10 character")
else:
    print(username)

    