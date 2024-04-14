# Aijah Johnson

# April 14, 2024

# P4HW2_JohnsonAijah

# calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.


# Varibales for calculated totals 
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0

# Loop to gather employee information
emp_name = ""
while emp_name != "Done":
    # Input 'Enter employee's name or Done to terminate "break": '
    emp_name = input('Enter employee\'s name or "Done" to terminate: ')
    
# if user wants to terminate type "Done" chapter 10 "Break"
    if emp_name == "Done":
        break
    
    # Input 'How many hours did emp work? '
    hours_wrk = float(input(f'How many hours did {emp_name} work? '))
    
    # Input 'What is the emp's pat rate? '
    pay_rate = float(input(f'What is {emp_name}\'s pay rate? '))
    
    print()
    
    # display 'Employee's name' + emp_name
    print('Employee\'s name:', emp_name)
    print()
    
    # display 'Hours Worked      Pay Rate      OverTime     OverTime Pay      RegHour Pay      Gross Pay'
    print('Hours Worked      Pay Rate      OverTime     OverTime Pay      RegHour Pay      Gross Pay')
    print('-----------------------------------------------------------------------------------------------------')
    
    # detect overtime and overtime_pay. Refer to Chapter 9 in Zybooks. Branching.
    if hours_wrk > 40:
        overtime_hours = hours_wrk - 40
        reg_hours = 40
    else:
        overtime_hours = 0
        reg_hours = hours_wrk
    
    if hours_wrk > 40:
        overtime_pay = pay_rate * 1.5 * overtime_hours
    else:
        overtime_pay = 0
    
    regular_hours_pay = reg_hours * pay_rate
    
    gross_pay = regular_hours_pay + overtime_pay
    
    # totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_hours_pay
    total_gross_pay += gross_pay
    total_employees += 1
    
    # display the hours worked, pay rate, overtime, overtime pay, regular hours paid, and gross income based on the employee input
    print(f'{hours_wrk:<18.1f} {pay_rate:<15.1f} {overtime_hours:<9.1f} {overtime_pay:<17.2f} ${regular_hours_pay:<17.2f} ${gross_pay:.2f}')
    print()

print()

# Display Total of Emps, OT pay, Reg Hours, and Gross.
print("Total number of employee\'s entered:", total_employees)
print(f"Total amount paid for overtime: {total_overtime_pay:.2f}")  #ensure to use 2 decimal places
print(f"Total amount paid for regular hours: {total_regular_pay:.2f}")
print(f"Total amount paid in gross: {total_gross_pay:.2f}")

