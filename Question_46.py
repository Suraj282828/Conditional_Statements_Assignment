'''
program to print grade description using match case.

'''
grade=input("Enter a grade =")

match grade:
    case "A":
        print(grade,"= Excellent")
    case "B":
        print(grade,"= Good")
    case "C":
        print(grade,"= Average")
    case "D":
        print(grade,"= Below average")
    case "F":
        print(grade,"= Fail")
    case _:
        print("Enter valid grade ")