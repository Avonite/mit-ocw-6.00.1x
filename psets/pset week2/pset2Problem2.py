def bal(balance, annualInterestRate, monthlyPayment, months):
    """
    balance: outstanding debt
    annualInterestRate: interest over one year
    months: number of months
    """
    if months == 0:
        return balance
    else:
        return bal((balance - monthlyPayment)*(1 + ((annualInterestRate)/12)), annualInterestRate, monthlyPayment, months - 1)

months = 12
monthlyPayment = 10

while True:
    if bal(balance, annualInterestRate, monthlyPayment, months) <= 0:
        break
    else:
        monthlyPayment += 10

print("Lowest Payment: ", monthlyPayment)
        



    