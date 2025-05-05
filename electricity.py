units=int(input("the number of units consumed"))
if units<50:
    amount=units*2.60
    extended_money=255
elif(units<=100):
    amount=130+ ((units-50) * 3.25)
    extended_money=35
elif(units<=200):
    amount=130+162.50 + ((units-100) * 5.26)
    extended_money=45
else:
    amount= 130+162.50 + ((units-200) * 8.45)
    extended_money=75
print("total bill amount ",amount+extended_money)