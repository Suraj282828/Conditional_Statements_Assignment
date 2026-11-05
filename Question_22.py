'''
program to check salary bonus based on years of service.

'''
year=int(input("Enter a years of service = "))

if year>=10 and year<=1:
    print("Salary bonus will be 20k")

elif year<=11 and year>=20:
    print("salary bonus will be 5K")

elif year==0:
    print("There will be no bonus for s fresher")

else:
    print("Enter a valid year of service")


