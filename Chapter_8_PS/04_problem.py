#writ a recursive function to calculate  the  sum of first n natural numbers:
def calculate_sum(n):
    if n <= 1:
        return n
    else:
        return n + calculate_sum(n - 1)


# User se input lein
num = int(input("Enter the number : "))

# Function call karein aur result print karein
print("Sum is:", calculate_sum(num))

