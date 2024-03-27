print("Welcome to calculator project Day_02:")

print("Enter total Bill.")
bill = int(input())

print("Enter tip in percent of total bill.")
tip_percent = float(input())
tip = float(bill * (tip_percent / 100))

print("In how many people you want to split the bill?")
split = int (input ())

total_bill = float((bill + tip)/split)

print("Amount per person is : ",round(total_bill,2))
