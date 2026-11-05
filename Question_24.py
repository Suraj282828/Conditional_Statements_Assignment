'''
program to check exam results (Distinction, First Class, Pass, Fail).

'''
result=int(input("Enter a result = "))

match result:
    case result if result>=75:
        print("Distinction")
    case result if result>=60:
        print("First Class")
    case result if result>=40:
        print("Pass")
    case _:
        print("Fail") 