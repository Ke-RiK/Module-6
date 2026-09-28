# Kirill Kaminskyi M6P5.py 9/28/2026

#input
last_name = input("Enter your last name: ")
salary = float(input("Enter your salary: "))
job_level = int(input("Enter your job level: "))

#process
if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = bonus_rate * salary

#output
print (f"Last Name: {last_name}")
print (f"Bonus: ${bonus:,.2f}")