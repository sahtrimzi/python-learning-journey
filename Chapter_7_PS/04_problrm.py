number = int(input("Enter a number: "))
if number<=1:
    print(" NOT a Prime Number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(" NOT a Prime Number")
            break    
    else:
        print("Prime Number")
        
         