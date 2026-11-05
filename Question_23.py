'''
program to calculate electricity bill based on units consumed.

'''
unit=int(input("Enter a unit = "))

if unit<=10 and unit>=1:
    print("Electricity is 50rs")

elif unit>=11 and unit<=20:
    print("Electricity bill is 100rs")

elif unit >=21 and unit<=30:
    print("Electricity bill is 150rs")

elif unit>=31 and unit<=40:
    print("Electricity bill is 200rs")

else:
    print("Unit is not Invalid")
