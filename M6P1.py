# Kirill Kaminskyi M6P1.py 9/23/2026

#input
num_of_widgets = int(input("Enter number of widgets: "))

#process
if num_of_widgets > 10000:
    price = 10
elif num_of_widgets < 5000:
    price = 30
else:
    price = 20

extended_price = price * num_of_widgets
tax = extended_price * 0.07
total_price = extended_price + tax
#output
print (f"Extended price: ${extended_price:,.2f}")
print (f"Tax amount: ${tax:,.2f}")
print (f"Total: ${total_price:,.2f}")