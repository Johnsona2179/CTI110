# Aijah Johnson

# March 13, 2024

# P3LAB_JohnsonAijah

# Write a program that takes in a year and determines whether that year is a leap year.

is_leap_year = False
   
input_year = int(input())

if input_year % 4 == 0:
    print(input_year, '- leap year')

else:
    print(input_year, '- not a leap year')
