#Write a python program to calculate the sum of the natural numbers

num = int(input("Enter a Number: ")) 
sum = 0
for i in range(1, num+1):
    sum = sum + i 
print(f"The sum of the first {num} natural numbers is {sum}")


    