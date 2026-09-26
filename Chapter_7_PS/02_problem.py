#write a program to greet all the person names stored in a list l and which start with the letter S
l = ["Sayyam", "Adarsh", "Saim", "Syed Ali Haider Trimzi", "Aditya", "Sanjay", "Aman"]
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")
