'''
program to print month days using match case.

'''
month=input("Enter a month = ")

match month:
    case "January":
        print(month,"= 31 days")
    case "February":
        print(month,"= 28 days")
    case"March":
        print(month,"= 31 days")
    case "April":
        print(month,"= 30 days")
    case "May":
        print(month,"= 31 days")
    case "June":
        print(month,"= 30 days")
    case "July":
        print(month,"= 31 days")
    case "Auguest":
        print(month,"= 31 days")
    case "September":
        print(month,"= 30 days")
    case "October":
        print(month,"= 31 days")
    case "November":
        print(month,"= 30 days")
    case "December":
        print(month,"= 31 days")
    case _:
        print("Invalid")
