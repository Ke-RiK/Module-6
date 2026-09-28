# Kirill Kaminskyi M6P4.py 9/28/2026

#input
number_of_tickets = int(input("Enter number of tickets: "))

#process
if number_of_tickets >= 25:
    price_per_ticket = 50
elif 10 <= number_of_tickets <= 24:
    price_per_ticket = 60
elif 5 <= number_of_tickets <= 9:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = price_per_ticket * number_of_tickets

#output
print (f"Number of tickets: {number_of_tickets}")
print (f"Price per ticket: ${price_per_ticket:,.2f}")
print (f"Total cost: ${total_cost:,.2f}")
