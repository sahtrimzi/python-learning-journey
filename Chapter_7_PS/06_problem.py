#Write a python program to calculate the factorial of a given number

num = int(input("Enter a Number: "))
fac = 1
for i in range(1, num+1):
    fac = fac * i 
print(f"The factorial of {num} is {fac}")