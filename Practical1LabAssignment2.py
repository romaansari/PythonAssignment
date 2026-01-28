# Vendor Purchase Report Program

# Taking vendor information as input
vendor_name = input("Enter vendor name: ")
year_of_association = input("Enter year of association: ")
contact_number = input("Enter contact number: ")
email_id = input("Enter email ID: ")

# Initialize a list to store monthly purchases
monthly_purchases = []

# Reading monthly purchases
print("\nEnter monthly purchase amounts:")
for month in range(1, 13):
    amount = float(input(f"Month {month}: Rs. "))
    monthly_purchases.append(amount)

# Calculate total and average purchases
total_purchase = sum(monthly_purchases)
average_purchase = total_purchase / 12

# Display vendor details and purchase report
print("\n--- Vendor Details ---")
print(f"Name: {vendor_name}")
print(f"Year of Association: {year_of_association}")
print(f"Contact Number: {contact_number}")
print(f"Email ID: {email_id}")

print("\n--- Annual Purchase Report ---")
for month in range(12):
    print(f"Month {month + 1}: Rs. {monthly_purchases[month]:.2f}")

print(f"\nTotal Annual Purchase: Rs. {total_purchase:.2f}")
print(f"Average Monthly Purchase: Rs. {average_purchase:.2f}")
