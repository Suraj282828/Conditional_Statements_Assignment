'''
program to check login status based on username and password.

'''
username = 1234
password = 123

user=int(input("Enter a username = "))
passw=int(input("Enter a password = "))

if username==user and password==passw:
    print("Login Successful")

elif username!=user and password!=passw:
    print("Login Unsuccessfull")

# elif password!=passw:
#     print("Please enter valid password",passw)

# elif password!=passw and username!=user:
#     print("Enter valid Username and Password",user,passw)

else:
    print("Invalid Format")