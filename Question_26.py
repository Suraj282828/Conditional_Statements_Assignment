'''
program to check month names based on month number.

'''
month_number=int(input("Enter a month number = "))

match month_number:
    case month_result if month_number==1:
        print("JAN")
    case month_result if month_number==2:
        print("FEB")
    case month_result if month_number==3:
        print("MARCH")
    case month_result if month_number==4:
        print("APRIL")
    case month_result if month_number==5:
        print("MAY")
    case month_result if month_number==6:
        print("JUNE")
    case month_result if month_number==7:
        print("JULY")
    case month_result if month_number==8:
        print("AUGUST")
    case month_result if month_number==9:
        print("SEPETEMBER")
    case month_result if month_number==10:
        print("OCTOBER")
    case month_result if month_number==11:
        print("NOVEMBER")
    case month_result if month_number==12:
        print("DECEMBAR")
    case _:
        print("Invalid Month")
    
    
