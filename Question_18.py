'''
program to check whether a number is positive, negative, or zero.

'''
number=int(input("Enter a number = "))
if number>0:
    print(number,"Is positive")
elif number<0:
    print(number,"Is Negative")
elif number==0:
    print(number,"Is zero")
else:
    print(number,"Is invalid")