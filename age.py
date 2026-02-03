# Ask the user for their Name
name = input("Enter your Name: ")

# Ask the user for their Current Age
age_input = input("Enter your Current Age: ")

# Convert the age to an integer
age = int(age_input)

# Calculate their age in 2030 (current year 2026, add 4 years)
age_in_2030 = age + 4

# Output: Print a message
print(f"Hey {name}, you will be {age_in_2030} years old in 2030!")