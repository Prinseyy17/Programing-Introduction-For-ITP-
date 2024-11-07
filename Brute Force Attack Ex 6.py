# Define a function to check password attempts
def check_password(correct_password, max_attempts):
    # Initialize the attempt counter
    attempts = 0
    # Loop until the maximum number of attempts is reached
    while attempts < max_attempts:
        # Prompt the user to enter the password
        entered_password = input("Enter the password: ")
        # Check if the entered password matches the correct password
        if entered_password == correct_password:
            print("Access granted!")
            return True  # Exit the function if the password is correct
        else:
            # Increment the attempt counter if the password is incorrect
            attempts += 1
            # Calculate remaining attempts
            remaining_attempts = max_attempts - attempts
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
    # Print a message if maximum attempts are reached
    print("Maximum attempts reached. Authorities have been alerted!")
    return False  # Return False if all attempts are used

# Set the correct password and the maximum number of attempts
correct_password = "09172006"
max_attempts = 5

# Call the function to check password
check_password(correct_password, max_attempts)
