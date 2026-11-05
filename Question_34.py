'''
program to check whether a year is a leap year and century year

'''
year=int(input("Enter a year = "))

if year%4==0:
    if year %100==0:
        print(year,"Is a centure year and leap year")
    else:
        print(year,"Is a not a centure year")
else:
    print(year,"Is not a leap year")