'''
program to print result status using match case.

'''
result = input("Enter your result (Pass, Fail, ATKT): ").lower()

match result:
    case "pass":
        print("Congratulations! You passed.")

    case "fail":
        print("Sorry! You failed.")

    case "atkt":
        print("You have an ATKT.")

    case _:
        print("Invalid result status!")
