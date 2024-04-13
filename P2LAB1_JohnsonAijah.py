 # Aijah Johnson

 # Febuary 28, 2024

  # P2LAB1_JohnsonAijah LAB: Driving Costs

  # Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.


miles = float(input('Enter a distance in miles: '))
cost_of_gas = float(input('Enter the cost of gas, dollars/gallon: '))
cost_mile = cost_of_gas / miles

mile_20 = cost_mile * 20
mile_75 = cost_mile * 75
mile_500 = cost_mile * 500

print(f'{mile_20:.2f} {mile_75:.2f} {mile_500:.2f}')
