# Aijah Johnson

# April 13, 2024

# P4HW1_JohnsonAijah

# Build from p2hw2 using loops to display letter grades



# Prompt user to place in number of scores
scorenumbs = int(input("How many scores would you like to enter? "))

# list
scores = []

print()

# create a loop for scores
for i in range(scorenumbs):
    while True:
        
        score = int(input(f"Enter score #{i+1}: "))

        if 0 <= score <=100:
            scores.append(score)
            break
        else:
            print()
            print('INVALID score entered!!!! \nScore should be between 0 and 100')

print()
print()
print('-------------Results-------------')
# show lowest score. Refer to Chapter 8 "Types" in Zybooks
lowest_score = min(scores)
print(f'Lowest Score    : {lowest_score:.1f}')

# Remove lowest score and create a modified list. Refer to chapter 8 "Types" in Zybooks. 

mod_list = scores
mod_list.remove(lowest_score)
print('Modified List   :', mod_list)
      
# Calculate average 
average_score = sum(scores) / len(scores)
print(f'Scores Average  : {average_score:.2f}')

# Determine letter grade for the average score. Refer to Chapter 9 "Branching" in Zybooks
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the letter grade
print('Grade         :', letter_grade)
print('---------------------------------')
