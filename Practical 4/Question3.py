
hour = float(input("Enter working hours: "))
Overtimepay = 0
ragularpay = hour * 40
if hour > 35 and hour < 60:
    Overtimepay = ragularpay * 1.5

elif hour >= 60:
    Overtimepay = ragularpay * 2

else:
    print("It is not correct hour")

totalsalary = Overtimepay + ragularpay

print("Total salary   :",totalsalary)
print("-> Regular pay :",ragularpay)
print("-> Overtime pay:",Overtimepay)

    