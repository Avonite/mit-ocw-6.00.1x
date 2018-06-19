def bal (balance, monthlyPaymentRate, annualInterestRate, months):
    if months == 0:
        return balance
    else:
        return bal(((balance - (monthlyPaymentRate*balance)))*(1 + (annualInterestRate/12)), monthlyPaymentRate, annualInterestRate, months - 1)
     
months = 12
print("Remaining balance: ", round(bal(balance, monthlyPaymentRate, annualInterestRate, months), 2))


    """
    balance: amount of debt
    annualInterestRate: rate of interest per year over balance
    monthlyPaymentRate: mandatory payment per month over balance
    months: number of months after which the balance is calculated
    """ 

