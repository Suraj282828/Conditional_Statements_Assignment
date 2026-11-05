'''
program to calculate discounts based on total shopping amount.

'''
# 1000
# 50%=500
# 20%=800
# 70%=300
# 90%=100


dis=int(input("Enter the discount = "))
total_amount=1000
match dis:
    case dis if dis == 10:
        print("Amount is 900rs")
    case dis if dis== 20:
        print("Amount is 800rs")
    case dis if dis == 30:
        print("Amount is 700rs")
    case dis if dis == 40:
        print("Amount is 600rs")
    case dis if dis == 50:
        print("Amount is 500rs")

    case dis if dis == 60:
        print("Amount is rs 400")
    case dis if dis== 70:
        print("Amount is 300rs")
    case dis if dis == 80:
        print("Amount is 200rs")
    case dis if dis == 90:
        print("Amount is 100rs")
    case dis if dis==100:
        print("Product is free for you")
    case _:
        print("Invalid Discount Offer please check the discount")
