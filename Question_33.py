'''
program to check whether a person can apply for a loan.

'''
age=int(input("Enter a age = "))
sal=int(input("Enter a sal = "))

if age>=22:
    if sal>=25000:
        print("You can apply for a loan ")
    else:
        print("Your salary should be more than 25000 ")
else:
    print("Your age is not enough to apply a loan")

