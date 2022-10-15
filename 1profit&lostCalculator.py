cost = int(input("input cost"))
income = int(input("input income"))

lost = 0
profit = 0

if income > cost:
	profit = int(income) - int(cost)
	print(profit)
else:
	lost = cost- income
	print(lost)

input("press anything to quit the program")
