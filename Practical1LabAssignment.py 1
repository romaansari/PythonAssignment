# Employee Salary Program

# Taking employee information as input
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary: "))

# Calculating allowances
DA = 0.92 * basic_salary  # Dearness Allowance
HRA = 0.58 * basic_salary # House Rent Allowance
TA = 0.30 * basic_salary  # Travel Allowance

# Deductions
LIC = 500  # Fixed monthly deduction

# Total salary calculation
gross_salary = basic_salary + DA + HRA + TA
net_salary = gross_salary - LIC

# Displaying employee details and salary
print("\n--- Employee Details ---")
print(f"Name: {name}")
print(f"Employee ID: {emp_id}")
print(f"Department: {department}")

print("\n--- Salary Details ---")
print(f"Basic Salary: Rs. {basic_salary:.2f}")
print(f"Dearness Allowance (DA): Rs. {DA:.2f}")
print(f"House Rent Allowance (HRA): Rs. {HRA:.2f}")
print(f"Travel Allowance (TA): Rs. {TA:.2f}")
print(f"LIC Deduction: Rs. {LIC:.2f}")
print(f"Net Salary: Rs. {net_salary:.2f}")
