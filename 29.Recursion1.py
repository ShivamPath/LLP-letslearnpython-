##factorial recursive


def a (n):
    if n==1 or n==0:
        return (1)
    return n*a(n-1)

print (a(4))