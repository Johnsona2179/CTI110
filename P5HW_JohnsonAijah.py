# Aijah Johnson

# April 24, 2024

# P5HW_JohnsonAijah

# Write a program that gives simple math quizzes

import random

if __name__ == "__main__":
    def generate_numbers():
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        return num1, num2

    def add_numbers():
        num1, num2 = generate_numbers()
        correct_ans = num1 + num2
        guesses = 0
        
        print(f"\n{num1}\n+ {num2}\n")
        while True:
            guess = int(input("Enter Answer: "))
            guesses += 1
            if guess == correct_ans:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
            elif guess < correct_ans:
                print("Sorry, guess is too low.\n")
            else:
                print("Sorry, guess is too high.\n")

    def subtract_numbers():
        num1, num2 = generate_numbers()
        correct_ans = num1 - num2
        guesses = 0
        
        print(f"\n{num1}\n- {num2}\n")
        while True:
            guess = int(input("Enter Answer: "))
            guesses += 1
            if guess == correct_ans:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
            elif guess < correct_ans:
                print("Sorry, guess is too low.\n")
            else:
                print("Sorry, guess is too high.\n")

    def main():
        print("Welcome to Math Quiz")
        print()
        
        while True:
            print()
            print("MAIN MENU")
            print("------------------------")
            print("1. Adding Random Numbers")
            print("2. Subtracting Random Numbers")
            print("3. Exit")
            print()
            choice = input("Please choose one of the menu options: ")
            
            if choice == '1':
                add_numbers()
            elif choice == '2':
                subtract_numbers()
            elif choice == '3':
                print("Thank you for playing...")
                print("Bye!!")
                break
            else:
                print("Error: Invalid choice. Please enter a number from 1 to 3.")

    main()
