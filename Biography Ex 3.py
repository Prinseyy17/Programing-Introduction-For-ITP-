# Prompt the user for their name
name = input("Enter your name: ")

# Prompt the user for their hometown
hometown = input("Enter your hometown: ")

# Prompt the user for their age, and store it as an integer
age = int(input("Enter your age: "))

# Store the user's information in a dictionary with keys: Name, Hometown, and Age
bio = {"Name": name, "Hometown": hometown, "Age": age}

# Print each piece of user information on separate lines
print(f"Name: {bio['Name']}\nHometown: {bio['Hometown']}\nAge: {bio['Age']}")
