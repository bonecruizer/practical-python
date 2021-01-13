# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0
month = 0

# user defined variables
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    payment = 2684.11
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = payment + extra_payment

    if (principal * 1+rate/12) <= payment:
        total_paid = total_paid + (principal * (1+rate/12))
        principal = 0
    else:

        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    print("Month: ", month, "Payed: ", total_paid, "Left: ", principal)

print('Total paid', round(total_paid,2))
print("Months to complete", month)