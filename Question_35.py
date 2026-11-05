'''
program to check whether a number is divisible by 3 and 5.

'''
number=int(input("Enter the number = "))
if number%3==0:
    if number%5==0:
        print("Number is divisible by 3 and 5")
    else:
        print(number,"Is not divisible by 5")
else:
    print(number,"Is not divisible by 3")