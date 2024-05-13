# Aijah Johnson

# April 21, 2024

# P5LAB_JohnsonAijah

# Leap Year. Write a program that takes in a year and determines the number of days in February for that year.

if __name__ == '__main__':
    
    year = int(input("Enter a year: "))

def is_leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not a Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

if is_leap_year(year) == "Leap Year":
    print(f"{year} has 29 days in February.")
else:
    print(f"{year} has 28 days in February.")
