'''
program to check blood donation eligibility based on age and weight.

'''
age=18
weight=50

Age=int(input("Enter a age = "))
Weight=int(input("Enter a weight = "))

if Age>=18 and Weight>=50:
    print("You are eligible for the blood donation")
else:
    print("You are not eligible for the blood donation")