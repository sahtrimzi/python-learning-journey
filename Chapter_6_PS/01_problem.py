# To find the greates number among the four numbers

a = int(input("Enter the number "))
b = int(input("Enter the number "))
c = int(input("Enter the number "))
d = int(input("Enter the number "))
if(a>b and a>c and a>d):
    print("a is greates number")
elif(b>a and b>c and b>d):
    print("b is greates number")
elif(c>a and c>b and c>d):
    print("c is greates number")
else:
    print("d is greates number")

