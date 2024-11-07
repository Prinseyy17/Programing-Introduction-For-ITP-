# Define a dictionary with countries as keys and their capitals as values
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo"
}

# Loop through each country-capital pair in the dictionary
for country, capital in questions.items():
    # Prompt the user for the capital of the current country, removing extra spaces and ignoring case
    answer = input(f"What is the capital of {country}? ").strip().lower()
    
    # Check if the user's answer matches the capital (ignoring case)
    if answer == capital.lower():
        # If correct, display a confirmation message
        print("Correct!")
    else:
        # If incorrect, display the correct answer
        print(f"Wrong! The correct answer is {capital}.")
