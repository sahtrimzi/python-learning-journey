for i in range(100):
    if i == 45:
        break     # skip the rest of the loop
    print(i)
else:
    print("Loop is finished")

for i in range(100):
    if i == 45:
        continue  #skip the current iteration
    print(i)
else:
    print("Loop is finished")