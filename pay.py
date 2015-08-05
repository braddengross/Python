__author__ = 'brad'

hours = 0
rate = 0
try:
    hours = float(input("Please enter your hours: "))
except:
    print("hours must be a number")
    quit()

try:
    rate = float(input("Please enter your pay rate: "))
except:
    print("rate must be a number")
    quit()

overtime_pay = 0
if hours > 40:
    overtime_hours = hours - 40
    hours = hours - overtime_hours
    overtime_pay = overtime_hours * (rate * 1.5)

pay = hours * rate + overtime_pay
print(pay)