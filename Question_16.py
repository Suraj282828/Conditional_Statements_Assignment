'''
program to find the greatest of three numbers.

'''
A=int(input("Enter a first number = "))
B=int(input("Enter a second number = "))
C=int(input("Enter a third number = "))

if A>=B and A>=C:
    print("Greater number is:", A)
elif B>=A and B>=C:
    print("Greater number is:", B)
else:
    print("Greater number is:", C)