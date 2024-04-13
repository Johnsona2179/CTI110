# Aijah Johnson

# March 7, 2024

# P2HW2_JohnsonAijah

# Create a program that will ask users to place in their module grades

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print()
print('-------------Results-------------')

print(f'Lowest Grade:      {min(grades)}')
print(f'Highest Grade:     {max(grades)}')
print(f'Sum of Grades:     {sum(grades)}')
print(f'Average:           {(mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6)/ 6:.2f}')

print('-----------------------------------------')
