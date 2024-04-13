# Aijah Johnson

 # March 6, 2024

 # P2HW1_JohnsonAijah

 # align the outputs from P1HW2

# Logic Start

# Input section
# Input 'This program calculates and displays travel expenses' 
print('This program calculates and displays travel expenses')
print()
    
# input 'Enter Budget:'into user_bud 
user_bud = float(input('Enter Budget:'))
print()

# input 'Enter your travel destination:' into user_loc
user_loc = input('Enter your travel destination:')
print()

# input 'How much do you think you will spend on gas?:' into user_gas
user_gas = float(input('How much do you think you will spend on gas?:'))
print()

# input 'Approximately, how much will you need for accomodation/hotel?:' into user_acc
user_acc = float(input('Approximately, how much will you need for accomodation/hotel?:'))
print()

# input 'Last, how much do you need for food?:' into user_food
user_food = float(input('Last, how much do you need for food?:'))
print()

# Processing Section
print('-------------Travel Expenses-------------')

# display 'Location:' + user_loc
print('Location:          ', user_loc)

# display 'Initial Budget:' + user_bud
print(f'Initial Budget:     ${user_bud:.2f}')

# display 'Fuel:' + user_gas
print(f'Fuel:               ${user_gas:.2f}')

# display 'accomodation:' + user_acc
print(f'Accomodation:       ${user_acc:.2f}')

# display 'Food:' + user_food
print(f'Food:               ${user_food:.2f}')

print('---------------------------------------------')

#display "remaining balance" + remaining balance 
print(f'Remaining Balance:  ${user_bud - user_gas - user_acc - user_food:.2f}')

# End of process
        


