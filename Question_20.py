'''
program to check ticket price based on age.

'''
age=int(input("Enter a age = "))

if age>=18:
    print(age," = Your age is greater so 18 you have to pay 100rs")

elif age<=18:
    print(age," = Your age is less than so 18 than you have to pay only 25rs")

elif age>=50 and age<=110:
    print(age,"= Your age is greater than 50 so you have to pay only 25rs")
    
else:
    print(age," = Enter a valid age")
