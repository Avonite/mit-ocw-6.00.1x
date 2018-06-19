P = 10000.0
n = 12.0
r = 0.08
t = float(input("How many years will the money be compounded for?"))

final_amount = P*(1+(r/n))**(n*t)

print("Final amount: ", round(final_amount, 2))