# Define a function to check if a number is even or odd
def check_even_or_odd(number):
    # Use modulus operator to determine if the number is even or odd
    if number % 2 == 0:
        return "even"  # Return "even" if the number is divisible by 2
    else:
        return "odd"  # Return "odd" if the number is not divisible by 2

# Main function to handle user input and display results
def main():
    # Prompt user to enter a number and convert input to an integer
    number = int(input("Enter a number: "))
    
    # Call the check_even_or_odd function with the user's number and store result
    result = check_even_or_odd(number)
    
    # Output whether the number is even or odd based on the function's result
    print(f"The number is {result}.")

# Call the main function to run the program
main()
