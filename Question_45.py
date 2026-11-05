'''
program to print menu-based food selection using match case.

'''
number=int(input("Enter a number = "))

match number:
    case 1:
        print(number,".Samosa")
    case 2:
        print(number,".Vadapav")
    case 3:
        print(number,".Misal")
    case 4:
        print(number,".biryani")
    case 5:
        print(number,".chicken")
    case _:
        print("Not avalabile")
