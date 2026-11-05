'''
program to check user role (admin, user, guest) using match case.

'''
role = input("Enter your role: ").lower()

match role:
    case "admin":
        print("Welcome, Admin! You have full access.")

    case "user":
        print("Welcome, User! You have limited access.")

    case "guest":
        print("Welcome, Guest! You have guest access.")

    case _:
        print("Invalid role!")

