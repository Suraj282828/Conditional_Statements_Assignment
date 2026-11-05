'''
program to check whether a number lies between 10 and 50.

'''

start_number=int(input("Enter start_number = "))

if start_number>=10:
    if start_number<=50:
        print(start_number ,"Is lies between 10 and 50")
    else:
        print(start_number, "Is greater then 50")
else:
    print("Number is less than 10 ")