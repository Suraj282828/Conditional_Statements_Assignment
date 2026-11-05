'''
program to find the smallest of three numbers.

'''
A=int(input("Enter a first number = "))
B=int(input("Enter a second number = "))
C=int(input("Enter a third number = "))

if A<=B and A<=C:
    print(A,"= Is smallest number")
elif B<=A and B<=C:
    print(B,"= Is smallest number")
else:
    print(C,"Is smallest number")