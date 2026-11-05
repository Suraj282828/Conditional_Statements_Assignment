'''
program to check whether a student is eligible for an exam (attendance + marks).

'''
attendance = int(input("Enter a attendance = "))
marks=int(input("Enter a marks = "))

if attendance >=75:
    if marks>=35:
        print("Eligible for an exam")
    else:
        print("Your are marks is not enough to pass")
else:
    print("Your attendance is not more than 75%")