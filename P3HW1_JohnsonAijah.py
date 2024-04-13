# Aijah Johnson

# March 13, 2024

# P3HW1_JohnsonAijah

# Correct the code listed in the attached file P3HW1 . 

# I was supposed to put a comment here
# My Last Name

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

print()
print('-------------Results-------------')

print(f'Lowest Grade:      {min(grades)}')
print(f'Highest Grade:     {max(grades)}')
print(f'Sum of Grades:     {sum(grades)}')
print(f'Average:           {(mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6)/ 6:.2f}')

print('-----------------------------------------')
      
# determine letter grade for average

average = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6)/ 6

if average >= 90:
      print('Your grade is: A')

elif average >= 80 and average <= 89:
      print('Your grade is: B')

elif average >= 70 and average <= 79:
      print('Your grade is: C')

elif average >= 60 and average <= 69:
      print('Your grade is: D')

else:
    print('Your grade is: F') # TO DO: finish this





