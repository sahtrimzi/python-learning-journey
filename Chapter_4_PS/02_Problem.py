# Write a program to accept marks of 6 student and display the marks in sorted manner. 

a = int(input("Enter the marks of student 1: "))
b = int(input("Enter the marks of student 2: "))
c = int(input("Enter the marks of student 3: "))
d = int(input("Enter the marks of student 4: "))
e = int(input("Enter the marks of student 5: "))
f = int(input("Enter the marks of student 6: "))

list = [a,b,c,d,e,f] # storing the marks in a list

list.sort() # sorting the list

print(list) # printing the sorted list

