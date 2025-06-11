principal = 0
rate = 0
years = 0
while principal <= 0:
    principal = int(input("What is your principal amount?: "))
    if principal <= 0:
        print("Principal amount can not be less than or equal to zero!")
while rate <= 0:
    rate = float(input("What is your interest rate?: "))
    if rate <= 0:
        print("Interest rate can not be less than zero!")
while years <= 0:
    years = int(input("Enter time in years?: "))
    if years <= 0:
        print("Years can not be less than zero!")
Total = principal*((1+(rate/100))**years)
print(f"Your total is: {Total:.2f}")