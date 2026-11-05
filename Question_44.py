'''
program to check traffic signal actions using match case.

'''
actions=input("Enter a actions = ")

match actions:
    case "Red":
        print(actions,"= Stop your vehicle")
    case "Yellow":
        print(actions,"= Prepare to stop when safe")
    case "Green":
        print(actions,"= Go when the road is clear")
    case _:
        print("= Action is invalid")