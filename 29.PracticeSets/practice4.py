# write a recursive function to calculate the sum of first n natural number
n=int(input('write the number: '))
def sum(n):
    if n==1 or n==0:
        return(1)
    return (n+(sum(n-1)))

print(sum(n))