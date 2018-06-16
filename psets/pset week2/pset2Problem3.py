def bal(balance, annualInterestRate, monthlyPayment, months):
    """
    balance: outstanding debt
    annualInterestRate: interest over one year
    monthlyPayment: annualInterestRate/12.0
    months: number of months
    """
    if months == 0:
        return balance
    else:
        return bal((balance - monthlyPayment)*(1 + ((annualInterestRate)/12)), annualInterestRate, monthlyPayment, months - 1)

balance = 999999
annualInterestRate = 0.18

high = (balance*(1+(annualInterestRate/12.0))**12)/12.0
low = balance/12.0

months = 12
monthlyPayment = (high+low)/2.0

epsilon = 0.00000001

while abs(bal(balance, annualInterestRate, monthlyPayment, months)) > epsilon:
    if bal(balance, annualInterestRate, monthlyPayment, months) > 0:
        low = monthlyPayment
    else:
        high = monthlyPayment
    monthlyPayment = (high+low)/2.0
    
print("Lowest Payment: ", round(monthlyPayment, 2))

    
