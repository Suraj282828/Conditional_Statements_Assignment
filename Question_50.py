'''
program to build a simple ATM menu using a match case.

'''
print("1. Check Balance")
print("2. Depoisit Money")
print("3. Withdraw Money")
print("4. Exit")
choice=int((input("Enter your choice :")))

balance=5000
match choice:
    case 1:
        print("Your balance is = ",balance)
    case 2:
        amount=float(input("Enter a deposite amount = "))
        balance += amount
        print(amount," = amount deposite successfully")
        print("your total balance is = ",balance)
    case 3:
        amount=float(input("Enter a deposite amount = "))
        if amount<=balance:
            balance -= amount
            print("Please collect your cash")
            print("Remaining balance = ",balance)
        else:
            print("Insufficient balance ")
    case 4:
        print("Thank you for using our ATM")
    case _:
        print("Invalid choice")
