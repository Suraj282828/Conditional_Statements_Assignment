'''
program to check whether a number is positive and even using nested if.

'''

num1=int(input("Enter a number = "))


if num1%2==0:
    print(num1,"Is Even")
    if num1>=0:
        print(num1,"Is positive")
    else:
        print(num1,"Is negative")
else:
    print(num1,"Is odd")
