# exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
while principal > 0:
    month += 1
    if month <= 12:
        pm = 1000+payment
    else:
        pm = payment
    principal = principal * (1+rate/12) - pm
    total_paid = total_paid + pm
print('Total paid', total_paid)