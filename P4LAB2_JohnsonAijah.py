# Aijah Johnson

# P4LAB2_JohnsonAijah Output range with increment of 5

# April 4, 2024

# Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer


x = int(input())
y = int(input())

if x < y:
    for num in range(x, y+1, 5,):
        print(num, end=' ')
        
else:
    print('Second integer can\'t be less than the first.')
