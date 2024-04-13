# Aijah Johnson

 # 2/29/2024

 # P2LAB2_JohnsonAijah LAB: Simple Statistics

 # Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point number

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

value_1 = num1 * num2 * num3 * num4
value_2 = ((num1 + num2 + num3 + num4) /4)

print(f'{value_1:.0f} {value_2:.0f}')
print(f'{value_1:.3f} {value_2:.3f}')
