def factorial(n): # Function definition
    if n == 1 or n == 0: # Base case
        return 1 # Return 1 if n is 1 or 0
    else: # Recursive case
        return n * factorial(n-1) # Return n multiplied by factorial of n-1

a = int(input("Enter your number = ")) # Getting input from user

print("Factorial of", a, "is", factorial(a)) # Printing factorial
