##wite a program to find greatest of four numbers entered by the user

no1=int(input("write no 1"))
no2=int(input("write no 2"))
no3=int(input("write no 3"))
no4=int(input("write no 4"))

if no1>no2 and no1>no3 and no1>no4:
    print(no1)
elif no2>no1 and no2>no3 and no2>no4:
    print(no2)
elif no3>no1 and no3>no2 and no3>no4:
    print(no3)
else:
    print(no4)
    