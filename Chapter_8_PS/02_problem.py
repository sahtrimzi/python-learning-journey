
# Problem 2: Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(f):
    f = int(input("Enter temprature in F"))
    return 5*(f-32)/9
f = int(input("Enter the temprature in F : "))
print(f_to_c(f))