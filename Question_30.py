'''
program to check the type of number (single, double, or three digit).

'''
# single=9
# double=99
# three_digit=999

num=int(input("Enter a number = "))

if num>=0 and num<=9:
    print("This is a single digit number = ",num)
elif num>=10 and num<=99:
    print("This is a double digit number = ",num)
elif num>=100 and num<=999:
    print("Third digit number = ",num)
else:
    print("Multi digit Number")