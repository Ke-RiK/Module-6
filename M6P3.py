# Kirill Kaminskyi M6P3.py 9/23/2026

#input
cd_principle_amount = float(input("Enter principle amount of CD: "))
cd_year_maturity = int(input("Enter year of maturity: "))

#process
if cd_principle_amount > 100000 and cd_year_maturity == 5:
    interrest_rate  = 0.06
elif  50000 <= cd_principle_amount <= 100000 and cd_year_maturity == 10:
    interrest_rate = 0.05
elif  50000 <= cd_principle_amount <= 100000 and cd_year_maturity == 5:
    interrest_rate = 0.04
else:
    interrest_rate = 0.02

year_interest_rate = cd_principle_amount * interrest_rate

#output
print (f"Principle amount: ${cd_principle_amount:,.2f}")
print (f"Interest rate: {interrest_rate:.0%}")
print (f"Interest amount for first year: ${year_interest_rate:,.2f}")