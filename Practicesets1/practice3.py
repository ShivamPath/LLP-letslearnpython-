#write a program to accept marks of 6 students and display them in a sorted manner

M1=int(input("enter the mark of student no 1"))
M2=int(input("enter the mark of student no 2"))
M3=int(input("enter the mark of student no 3"))
M4=int(input("enter the mark of student no 4"))
M5=int(input("enter the mark of student no 5"))
M6=int(input("enter the mark of student no 6"))

Marks=[M1,M2,M3,M4,M5,M6]
Marks.sort()
print(Marks)
 