#write a program to calculate the grade of a student from his marks from the following scheme.
mathsMark=int(input("enter your mark"))

if mathsMark>=90 and mathsMark<=100:
    print("A+")
if mathsMark>=80 and mathsMark<90:
    print("A")
if mathsMark>=70 and mathsMark<80:
    print("B")
if mathsMark>=60 and mathsMark<70:
    print("C")
if mathsMark>=50 and mathsMark<60:
    print("D")
if mathsMark<50:
    print("E")


