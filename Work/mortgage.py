# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
real_payment = 0 

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        real_payment = payment + extra_payment
    else:
        real_payment = payment
    
    if principal <= payment:
        real_payment = principal
        principal = 0
    else:
        principal = round(principal * (1+rate/12) - real_payment, 2)
    total_paid = total_paid + real_payment
    print(month , total_paid, principal)
    month = month + 1

#print('Total paid', total_paid)
#print('Total month', month)