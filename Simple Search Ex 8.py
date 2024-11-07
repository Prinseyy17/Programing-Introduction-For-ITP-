# Define a function to search for a name within a list
def search_name():
    # List of names to search through
    names = ["Rave", "Prinse", "Enzo", "John", "James", "Matthew"]
    
    # Variable to keep track of whether the name has been found
    found = False
    
    # Start a loop that continues until a name is found
    while not found:
        # Prompt the user to enter a name to search for
        search = input("Enter the name to search for: ")
        
        # Check if the entered name is in the list
        if search in names:
            # If found, print a message and set `found` to True to exit the loop
            print(f"{search} is found in the list!")
            found = True  # Exit loop when found
        else:
            # If not found, notify the user and repeat the loop
            print(f"{search} is not found. Try again.")

# Call the function to start the name search
search_name()
