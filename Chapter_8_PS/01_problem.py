# Problem 1: Write a program using functions to find the greatest of three numbers.
def gretest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 70
b = 60
c = 100
print(gretest(a,b,c))

