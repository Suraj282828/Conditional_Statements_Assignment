'''
program to perform calculator operations using match case.

'''

num1=int(input("Enter a first number = "))
operator=(input("Enter operator:"))
num2=int(input("Enter a second number = "))


match operator:
    case "+":
        print("Result = ",num1+num2)
    case "*":
        print("Result = ",num1*num2)
    case "-":
        print("Result = ",num1-num2)
    case "/":
        print("Result = ",num1/num2)
    case _:
        print("Invalid")