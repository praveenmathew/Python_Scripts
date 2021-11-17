#Based on challenges put up by https://www.teclado.com/30-days-of-python/python-30-day-3-project 
#Simple script to read, calculate data with minimal arithmetic and display to output.


name = input("Please enter employee name: ").strip().title()
hourly_wage = float(input("Please enter hourly_wage: "))
work_hours = float(input("Please enter hours worked: "))


print(f"{name} earned ${hourly_wage * work_hours} this week")
