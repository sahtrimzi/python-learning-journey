#write a program to check whether a student is pass or fail, if it requires total 40% and minimum 33% in each subject to pass.

subj1 = int(input("Enter Maths marks : "))
subj2 = int(input("Enter computer marks : "))
subj3 = int(input("Enter physics marks : "))
total_per = (subj1 + subj2 + subj3)/300*100
if(subj1>33 and subj2>33 and subj3>33 and total_per>=40):
    print("pass")
else:
    print("Fail")
    