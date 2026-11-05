'''
program to print language choice using match case.

'''
choice = int(input("Choose a language (1. English, 2. Hindi, 3. Marathi) "))

match choice:
    case 1:
        print("You selected English.")

    case 2:
        print("You selected Hindi.")

    case 3:
        print("You selected Marathi.")

    case _:
        print("Invalid choice!")
