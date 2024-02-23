 # Aijah Johnson

 # February 21, 2024

 # P1HW2_JohnsonAijah

 #  With Pseudocode,create a program that does some basic math on numbers that are entered. 

# Logic Start

# Input section
# Input 'This program calculates and displays travel expenses' 
print('This program calculates and displays travel expenses')
print()
    
# input 'Enter Budget:'into user_bud 
user_bud = int(input('Enter Budget:'))
print()

# input 'Enter your travel destination:' into user_loc
user_loc = input('Enter your travel destination:')
print()

# input 'How much do you think you will spend on gas?:' into user_gas
user_gas = int(input('How much do you think you will spend on gas?:'))
print()

# input 'Approximately, how much will you need for accomodation/hotel?:' into user_acc
user_acc = int(input('Approximately, how much will you need for accomodation/hotel?:'))
print()

# input 'Last, how much do you need for food?:' into user_food
user_food = int(input('Last, how much do you need for food?:'))
print()

# Processing Section
print('----------Travel Expenses----------')

# display 'Location:' + user_loc
print('Location:', user_loc)

# display 'Initial Budget:' + user_bud
print('Initial Budget:', user_bud)
print()

# display 'Fuel:' + user_gas
print('Fuel:', user_gas)

# display 'accomodation:' + user_acc
print('Accomodation:', user_acc)

# display 'Food:' + user_food
print('Food:', user_food)
print()

#display "remaining balance" + remaining balance 
print('Remaining Balance:',user_bud - user_gas - user_acc - user_food)

# End of process
        

