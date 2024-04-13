# Aijah Johnson

# March 20, 2024

# P3HW2_Salary_JohnsonAijah

# Create a program that calculates an employees ay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay

#Logic Start

# Input Section
# Input 'Enter employee's name: '
emp_name = input('Enter employee\'s name: ')

# Input 'Enter number of hours worked: '
hours_wrk = float(input('Enter number of hours worked: '))

# Input 'Enter employee's pay rate: '
pay_rate = float(input('Enter employee\'s pay rate: '))

# output
print('----------------------------------------')

# display 'Employee's name' + emp_name
print('Employee\'s name: ', emp_name)
print()

# display 'Hours Worked      Pay Rate      OverTime     OverTime Pay      RegHour Pay      Gross Pay'
print('Hours Worked      Pay Rate      OverTime     OverTime Pay      RegHour Pay      Gross Pay')
print('-----------------------------------------------------------------------------------------------------')


# detect overtime and overtime_pay using branches
if hours_wrk > 40:
    overtime = hours_wrk - 40
else:
    overtime = 0

if hours_wrk > 40:
    overtime_pay = pay_rate * 1.5 * overtime
else:
    overtime_pay = 0

reghour = 40 * pay_rate

gross = reghour + overtime_pay


# display the hours worked, pay rate, overtime, pvertime pay, regular hours paid, and gross income based on the employe input
print(f'{hours_wrk:<18.1f} {pay_rate:<15.1f} {overtime:<9.1f} {overtime_pay:<17.2f} ${reghour:<17.2f} ${gross:.2f}')
