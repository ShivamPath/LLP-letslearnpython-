'''write a program to find out whether a student is pass or fail, if requires total 40% and
atleast 33% in each to pass. Assume 3 subjects and take marks as an input from the user'''

Maths=int(input("enter Maths mark: "))
Science=int(input("Enter science mark:"))
English=int(input("enter English marks"))

marksPercentage=(Maths+Science+English)*100/100

if marksPercentage>=40*100/100 and Maths>=33 and Science>=33 and English>=33:
    print("Pass")
else:
    print("Fail")