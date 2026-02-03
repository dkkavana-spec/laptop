# Ask for the Total Bill Amount (float)
total_bill = float(input("Enter the Total Bill Amount: "))

# Ask for the Number of People (int)
num_people = int(input("Enter the Number of People: "))

# Calculate the Share per Person
share_per_person = total_bill / num_people

# Output the result
print(f"Total Bill: [{total_bill}]. Each person pays: [{share_per_person}]")

# Bonus: Verify the data types of variables
print(f"Type of total_bill: {type(total_bill)}")
print(f"Type of num_people: {type(num_people)}")
print(f"Type of share_per_person: {type(share_per_person)}")