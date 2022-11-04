##write a program using function to find gratest of three number entered by user.
n1=int(input("enter the first no: "))
n2=int(input("enter the second no: "))
n3=int(input("enter the third no: "))

def gratest(n1,n2,n3) :
    if n1>n2 and n1>n2:
        return(n1)
    elif n2>n1 and n2>n3:
        return(n2)
    else:
        return(n3)

print(f'The maximum value is {gratest(n1,n2,n3)}')
