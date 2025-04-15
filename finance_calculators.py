# At the top of the file include import math
import math

# Choose a calculation method between investment or bond

user_choose = str(input("Enter method of calculation, investment or bond: "))\
    .lower()

# For bond calculation method
if user_choose == "bond":
    present = int(input("Enter your present value: "))
    i = float(input("Enter monthly interest rate in percentage: "))/100/12
    number_months = int(input("Enter number of months to pay the bond: "))
    repayment = (i/100/12 * present)/(1 - (1 + i/100/12)**(-number_months))
    print(repayment)

# For investment calculation method
elif user_choose == "investment":
    p = int(input("Enter the deposit amount: "))
    r = float(input("Enter the interest rate in percentage: "))/100
    t = int(input("Enter the number of years the money is being invested: "))

    interest_type = input("Enter your desired interest type, simple or\
        compound: ").lower()
# Calculate the total amount for simple and compund interest
    if interest_type == "simple":
        total_amount = p * (1 + r*t)
        print(f"This is the total amount of the simple interest:\
            {total_amount}")
    elif interest_type == "compound":
        total_amount = p * math.pow((1+r), t)
        print(f"This is the total amount of the compound interest:\
            {total_amount}")
    else:
        print("Wrong input")

else:
    print("Wrong input, try again: ")
