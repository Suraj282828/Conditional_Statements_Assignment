'''
program to check whether a number is greater than 0 and less than 100.

'''
number=int(input("Enter a number = "))

if number>=0:
    if number<=100:
        print(number,"= Is greter than 0 and less than 100")
    else:
        print(number,"= Is greater than 100")
else:
    print(number,"Is less than 0 ")