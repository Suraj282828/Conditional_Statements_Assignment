'''
program to check whether a student passed all subjects.

'''
phy=int((input("Enter a physics marks = ")))
che=int((input("Enter a chemestry marks = ")))
math=int((input("Enter a math marks = ")))
bio=int((input("Enter a biology marks = ")))

match(phy >=35 and che>=35 and math >=35 and bio >=35):
    case True:
        print("Student passed all subject ")
    case false:
        print("Student failed ")