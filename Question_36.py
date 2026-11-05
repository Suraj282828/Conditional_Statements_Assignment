'''
program to check whether a person is eligible for a driving license.

'''

age=int(input("Enter a age = "))
has_licence=bool(input("Has_licence = "))

has_licence

if age>=18:
    if has_licence != False:
        print("You can drive")
    else:
        print("You should first apply for a licence")
else:
    print("You age is not enough")
