# Define a function to get the number of days in a given month, with an optional leap year adjustment
def get_days_in_month(month, leap_year=False):
    # Dictionary mapping each month number to its standard number of days
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    # Check if the month is February and adjust for leap year if applicable
    if month == 2 and leap_year:
        return 29  # February has 29 days in a leap year
    # Return the number of days for the given month, or an error message if the month is invalid
    return month_days.get(month, "Invalid month")

# Prompt the user to enter the month number
month = int(input("Enter the month number (1-12): "))

# Check if the month is February to ask about leap year
if month == 2:
    # Ask the user if it's a leap year, converting input to lowercase for consistency
    leap_year = input("Is it a leap year? (yes/no): ").lower() == "yes"
    # Output the number of days in February based on leap year status
    print(f"Days in February: {get_days_in_month(2, leap_year)}")
else:
    # Output the number of days for the selected month
    print(f"Days in month {month}: {get_days_in_month(month)}")
