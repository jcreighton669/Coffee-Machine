income = int(input())
calculated_tax = 0
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
elif income >= 132407:
    percent = 28

calculated_tax = round(income * percent / 100)
print("The tax for {} is {}%. That is {} dollars!".format(income, percent,
                                                           calculated_tax))
